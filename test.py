# import requests
# import os
# import json
# from dotenv import load_dotenv

# player_tag = "2RCR8PJV"

# load_dotenv()

# clash_api_key = os.getenv('clash_api_key')

# player_endpoint = (f"https://api.clashroyale.com/v1/players/%23{player_tag}/battlelog")

# r=requests.get(f"{player_endpoint}", headers={"Accept":"application/json", "authorization":f"Bearer {clash_api_key}"})
        
# battlelog_data = r.json()
               
# opponent_tag = battlelog_data[13]["opponent"][0]["tag"]

# new_opponent_tag = opponent_tag.replace("#","")

# print(new_opponent_tag)
               

# clash_api_key = os.getenv('clash_api_key')

# player_endpoint = (f"https://api.clashroyale.com/v1/players/%23{new_opponent_tag}")

# r=requests.get(f"{player_endpoint}", headers={"Accept":"application/json", "authorization":f"Bearer {clash_api_key}"})
# print(json.dumps(r.json()))
    
    
    