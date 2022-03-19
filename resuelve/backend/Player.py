import sys
import json

class Player():

    def salary_calculation(self, json_body):
        players = json_body["jugadores"]
        levels = json_body["niveles"]
        
        players_response = []
        players_aux = []
        full_percentage = []

        for player in players:
            player_level = player["nivel"]
            player_goals = player["goles"]
            level_goals = Player.get_level(levels, player_level, player_goals)
            player["goles_minimos"] = level_goals
            individual_percent = Player.get_individual_percentage(player_goals, level_goals)
            player["individual_percent"] = individual_percent
            full_percentage.append(individual_percent)
            players_aux.append(player)

        team_percentage_avg = Player.get_team_percentage_avg(full_percentage)
        
        for player in players_aux:
            player_complete = Player.get_complete_salary(player, team_percentage_avg)
            players_response.append(player_complete)

        print(players_response)

        response = {"statusCode": 200, "body": json.dumps(players_response)}
        return response

    def get_level(levels, player_level,player_goals):
        for level in levels:
            if player_level.lower() == level["nivel"].lower():
                level_goals = level["goles"]
                #print("player_goals " +str(player_goals))
                #print("level_goals " +str(level_goals))
                #print(percent)

                return level_goals
    
    def get_individual_percentage(player_goals, level_goals):
        quotient = player_goals / level_goals
        percent = quotient * 100

        return percent

    def get_team_percentage_avg(full_percentage):
        team_percentage = 0
        index = 0
        for percentage in full_percentage:
            team_percentage += percentage
            index += 1

        team_percentage = team_percentage/index
        
        return team_percentage    

    def get_complete_salary(player, team_percentage):
        complete_percentage = 0
        complete_salary = 0

        individual_percent = player["individual_percent"]
        salary = player["sueldo"]
        bonus = player["bono"]
        complete_percentage = (team_percentage + individual_percent)/2
        bonus_calculated = (bonus * complete_percentage) / 100
        complete_salary = salary + bonus_calculated
        player["sueldo_completo"] = complete_salary

        del player["individual_percent"]
        del player["nivel"]
        
        return player
    
    