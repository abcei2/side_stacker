from django.views.generic import View
from django.shortcuts import render, redirect

from game.models import TemporalGame

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

import random
import json


def create_game(request, host_name):

    if request.method == "POST":
        #CREATE GAME
        player_name=request.POST.get("player_name")
        rows=request.POST.get("rows")
        columns=request.POST.get("columns")
        rand_indx=str(random.randint(100, 999))
        temp_game=TemporalGame(room_name=f"{player_name}_{rand_indx}_room",rows=rows, columns=columns)
        temp_game.save()       
        
        return redirect(f"/game/{player_name}_{rand_indx}_room")
 
def connect_game(request, host_name):
    current_game_query=TemporalGame.objects.filter(room_name=f"{host_name}")
    current_game=current_game_query.values()
    if len(current_game)>0:
        columns=current_game[0]['columns']
        rows=current_game[0]['rows']
        hostip=request.get_host().split(":")
        if(len(hostip)==1):
            hostip=hostip+":8000"
        else:
            hostip=request.get_host()
        print(hostip)
        if current_game[0]['player_x']=="None":
            current_game_query.update(player_x="Groundhog_"+str(random.randint(100, 999)))
            return  render(request, "game.html", {"hostip":hostip,"host_name":host_name, "player":"X","ammount_squares":rows*columns,"rows":rows,"columns":columns})
        elif current_game[0]['player_y']=="None":
            current_game_query.update(player_y="RoyalEagle_"+str(random.randint(100, 999)))
        
            return  render(request, "game.html", {"hostip":hostip,"host_name":host_name,"player":"O","ammount_squares":rows*columns,"rows":rows,"columns":columns})
        else:        
            return redirect(f"/")
    else:
        return redirect(f"/")

@sync_to_async
def check_users(host_name):    
    current_game=TemporalGame.objects.filter(room_name=f"{host_name}").values()
    TemporalGame.objects.filter(room_name=host_name).delete()
    return "DELETED!"

@sync_to_async
def delete_game(host_name):    
    TemporalGame.objects.filter(room_name=host_name).delete()
    return "DELETED!"

    
class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context={
            "games":list(TemporalGame.objects.filter(player_y="None").values('room_name','player_x','player_y')),
  
        }

        return render(
            request,
            self.template_name,
            context,
        )
class GameSideStacker(AsyncWebsocketConsumer):
    recieve_end_flag=False
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "%s" % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "game_command",
                "game_event": "USER_DISCONECTED",
                "message":  "user disconnected, game is over, you won!!",
            },
        )
     
        await delete_game(self.room_group_name) 
        
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
       
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "game_command",
                "game_event": text_data_json["game_event"],
                "message": text_data_json["message"],
            },
        )

    async def game_command(self, event):
        game_event = event["game_event"]
        message = event["message"]

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "type": "game_command",
                    "game_event": game_event,
                    "message": message,
                }
            )
        )