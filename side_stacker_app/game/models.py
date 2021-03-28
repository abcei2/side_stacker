from django.db import models
import random
import uuid
# # Create your models here.

class TemporalGame(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    room_name = models.TextField(max_length=1024,null=False)
    player_x = models.TextField(max_length=1024,default="None")
    player_y = models.TextField(max_length=1024,default="None")
    columns = models.IntegerField(default=3)
    rows = models.IntegerField(default=3)
    