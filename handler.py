import sys

sys.path.append("../resuelve/backend/Player")
from resuelve.backend.Player import Player

import json

def salary_calculation(event, context):
    
    request = json.loads(event["body"])
    
    player_fc = Player()
    calculation = player_fc.salary_calculation(request)

    return calculation
    
    