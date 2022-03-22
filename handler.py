import sys

sys.path.append("./resuelve/backend")
from player import Player

import json

# Handler that help us to call the salary_calculation function
def salary_calculation(event, context):
    
    request = json.loads(event["body"])
    
    player_fc = Player()
    calculation = player_fc.salary_calculation(request)

    return calculation

# Handler that help us to call the multi_salary_calculation function 
def multi_salary_calculation(event, context):
    
    request = json.loads(event["body"])
    
    player_fc = Player()
    calculation = player_fc.multi_salary_calculation(request)

    return calculation

# Handler that help us to call the post_levels_json function 
def save_json_file(event, context):
    
    request = json.loads(event["body"])
    
    player_fc = Player()
    calculation = player_fc.post_levels_json(request)

    return calculation