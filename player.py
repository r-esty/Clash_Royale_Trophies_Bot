import requests
import os
import json
from dotenv import load_dotenv
from battlelog import battlelog_call

opponent_tag = battlelog_call()

# Function to call opponent's player endpoint
def players_call():
    load_dotenv()
    clash_api_key = os.getenv('clash_api_key')
    opponent_tag = battlelog_call()  
    player_endpoint = (f"https://api.clashroyale.com/v1/players/%23{opponent_tag}")
    r = requests.get(f"{player_endpoint}", headers={"Accept": "application/json", "authorization": f"Bearer {clash_api_key}"})
    opponent_data = r.json()
    oponnent_trophy = opponent_data['bestPathOfLegendSeasonResult']['trophies']
    opponent_league = opponent_data['bestPathOfLegendSeasonResult']['leagueNumber']
    new_opponent_tag = opponent_data['tag']
    opponent_name = opponent_data['name']
    return(f"{oponnent_trophy} {opponent_league} {new_opponent_tag} {opponent_name}")
    
    
players_call()