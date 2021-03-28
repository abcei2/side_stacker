# SideStacker app

## With docker-compose
git clone https://github.com/abcei2/side_stacker  
cd side_stacker  
docker-compose up --build  
### ENJOY!

## Without docker compose  
Proved on python3.9  

### Clone a install python packages
git clone https://github.com/abcei2/side_stacker  
cd side_stacker  
pip install -r requirements.txt

### Install redis  
In this url you can get more detailing information about redis installation and setup; https://www.digitalocean.com/community/tutorials/como-instalar-y-proteger-redis-en-ubuntu-18-04-es    
After installation go to **side_stacker_app/settings.py** and change the channel_layer host **redis** to **localhost** or the ip and the port of redis host that you are using (default localhost:6379).

```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}
```

### Makemigrations and migrate

python side_stacker_app/manage.py makemigrations && python side_stacker_app/manage.py migrate

### Run project

python side_stacker_app/manage.py runserver 0.0.0.0:8000

### ENJOY!



### REF:  
**Django-channels and websockets:**  
https://blog.logrocket.com/django-channels-and-websockets/  
**repo:** https://github.com/krazygaurav/Django-channels-Tic-Tac-Toe  
**Async chat tutorial (in spanish)**  
https://programadorwebvalencia.com/django-chat-usando-websockets-con-salas-y-async/  

### There are many thing left to this repo:
- To add .env file, to secure secret keys and db credentials.
- Improve styles.
- Websockets in lobby section, to enable users detect new available public games without reload page.
- When some user left game the game is over so i put an alert to show that other user logout, but sometimes that alert do not stop the js flow and users doesn't know what happen with the game because the alert fails to show.
