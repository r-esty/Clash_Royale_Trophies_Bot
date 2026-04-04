import requests
import os
import json
from dotenv import load_dotenv
from  battlelog import battlelog_call
from player import players_call
import time
 
last_opponent = None

while True:
    try:
        value = players_call()
        value_list = value.split()
        rating = value_list[0]
        league = value_list[1]
        opponents_tag = value_list[2]
        opponents_name = value_list[3]
        
        if last_opponent != opponents_tag:
            print(f"You recently faced {opponents_name} with the tag ({opponents_tag}) their highest rating is {rating} and highest league is {league}")
            last_opponent = opponents_tag
    
    except Exception as e:
        print(f"Error: {e}")
        
        
    
    time.sleep(5)