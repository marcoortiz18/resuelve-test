import sys
import json
class Player():

    # Main function,
    # This function is responsible for perform all the necessary steps to obtain the complete salary
    def salary_calculation(self, json_body):
        players = json_body["jugadores"]
        levels = json_body["niveles"]
        
        players_response = []
        players_aux = []
        full_percentage = []

        players_aux = Player.set_minimum_goals(players, levels)

        full_percentage = Player.get_full_percentage(players_aux)

        team_percentage_avg = Player.get_team_percentage_avg(full_percentage)
        
        for player in players_aux:
            player_complete = Player.get_complete_salary(player, team_percentage_avg)
            players_response.append(player_complete)
        
        response = {"statusCode": 200, "body": json.dumps(players_response)}
        return response

    # Function that returns the levels list that we use to get the minimum goals by level
    def get_levels():
        levels = []
        url_file = "resuelve/backend/levels.json"
        json_file = open(url_file,"r")
        levels_data = json.loads(json_file.read())
        levels = levels_data["niveles"]
        json_file.close()
        return levels

    # Function that set the minimum goals by level on players list
    def set_minimum_goals(players, levels):
        players_with_minimum_goals = []
        for player in players:
            player_level = player["nivel"]
            player_goals = player["goles"]
            level_goals = Player.get_goals_by_level(levels, player_level)
            player["goles_minimos"] = level_goals
            individual_percent = Player.get_individual_percentage(player_goals, level_goals)
            player["individual_percent"] = individual_percent
            players_with_minimum_goals.append(player)
        
        return players_with_minimum_goals

    # Function that get the goals by the player levels
    def get_goals_by_level(levels, player_level):
        for level in levels:
            if player_level.lower() == level["nivel"].lower():
                level_goals = level["goles"]

                return level_goals
    
    # Function that get the individual percentage from a player based on his level
    def get_individual_percentage(player_goals, level_goals):
        quotient = player_goals / level_goals
        percent = quotient * 100

        return percent

    # Function that get the full percentage from all players
    def get_full_percentage(players):
        full_percentage = []
        for player in players:
            individual_percent = player["individual_percent"]
            full_percentage.append(individual_percent)

        return full_percentage

    # Function that get the average percentage based on the full percentage
    def get_team_percentage_avg(full_percentage):
        team_percentage = 0
        index = 0
        for percentage in full_percentage:
            team_percentage += percentage
            index += 1

        team_percentage = team_percentage/index
        
        return team_percentage    

    # Function that get the complete salary from a player using the team_percentage and the individual_percent
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
    
    # Bonus function,
    # This function is responsible to parse and provide all the json from different team and set the response
    def multi_salary_calculation(self, json_body):
        keys = json_body.keys()

        multi_players = []
        index = 0

        for key in keys:
            players = []
            
            players = json_body[key]
            player = Player.salary_calculations(self, players)
            player = {""+ str(key) + ":": player}
            
            multi_players.append(player)
            index += 1
        
        response = {"statusCode": 200, "body": json.dumps(multi_players)}
        return response

    # Bonus function,
    # This function is responsible to perform all the necessary steps to obtain the complete salary from multiple Teams players.
    def salary_calculations(self, json_body):
        players = json_body
        levels = Player.get_levels(self)
        
        players_response = []
        players_aux = []
        full_percentage = []

        players_aux = Player.set_minimum_goals(players, levels)

        full_percentage = Player.get_full_percentage(players_aux)

        team_percentage_avg = Player.get_team_percentage_avg(full_percentage)
        
        for player in players_aux:
            player_complete = Player.get_complete_salary(player, team_percentage_avg)
            players_response.append(player_complete)
        
        return players_response
    
    # Function used to fill Levels elements.
    def post_levels_json(self,json_levels):
        url_file = "resuelve/backend/levels.json"
        json_file = open(url_file,"r+")
        json_file.truncate(0)
        json.dump(json_levels, json_file)
        json_file.close()

        response = {"statusCode": 200, "body": "{\"status\": \"Saved!\"}"}

        return response