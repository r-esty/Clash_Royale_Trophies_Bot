import requests
import os
import json
from dotenv import load_dotenv
from battlelog import battlelog_call


opponent_tag = battlelog_call()

#new_opponent_tag = opponent_tag[:1]

#print(battlelog_call)


# Function to call opponent's player endpoint
def players_call():

    

    load_dotenv()

    clash_api_key = os.getenv('clash_api_key')

    player_endpoint = (f"https://api.clashroyale.com/v1/players/%23{opponent_tag}")

    r=requests.get(f"{player_endpoint}", headers={"Accept":"application/json", "authorization":f"Bearer {clash_api_key}"})
    #print(json.dumps(r.json()))
    
    opponent_data = r.json()
    
    oponnent_trophy = opponent_data['bestPathOfLegendSeasonResult']['trophies']
    
    
    
    print(opponent_data['bestPathOfLegendSeasonResult']['trophies'])
    
    
    
   
    
    
    #opponent_trophy = opbestPathOfLegendSeasonResult"]["trophies"]
    
    # x = opponent_data
    
    # c = type(x)
    
    # print(c)
    
    
players_call()