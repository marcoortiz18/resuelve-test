import sys

sys.path.append("../resuelve/backend/player")
from resuelve.backend.player import Player

import json

def salary_calculation(event, context):
    
    request = json.loads(event["body"])
    
    player_fc = Player()
    calculation = player_fc.salary_calculation(request)

    return calculation
    
def multi_salary_calculation(event, context):
    
    request = json.loads(event["body"])
    
    player_fc = Player()
    calculation = player_fc.multi_salary_calculation(request)

    return calculation

def save_json_file(event, context):
    
    request = json.loads(event["body"])
    
    player_fc = Player()
    calculation = player_fc.post_levels_json(request)

    return calculation