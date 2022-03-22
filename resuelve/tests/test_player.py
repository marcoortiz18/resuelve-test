import sys

sys.path.append("./resuelve/backend")

from player import Player

# Unit test to valid the get levels function
def test_get_levels():
    levels = Player.get_levels()
    print(levels)
    assert len(levels) > 0

# Unit test to valid the post levels function
def test_post_levels_json():
    json_test= {"niveles": [{"nivel": "A", "goles": 5}, {"nivel": "B", "goles": 10}, {"nivel": "C", "goles": 15}, {"nivel": "Cuauh", "goles": 20}]}
    player = Player()
    valid = player.post_levels_json(json_test)
    print(valid)
    assert valid["statusCode"] == 200

# Unit test to valid the set minimum goals
def test_set_minimum_goals():
    players = [
                {
                "nombre": "Juan Perezz",
                "nivel": "C",
                "goles": 10,
                "sueldo": 50000,
                "bono": 25000,
                "sueldo_completo": "",
                "equipo": "rojo"
                }
            ]

    levels = [
                {
                "nivel": "C",
                "goles": 15
                }
            ]

    player_with_minimum_goals = Player.set_minimum_goals(players, levels)

    assert player_with_minimum_goals[0]["goles_minimos"] == 15

# Unit test to valid the get the goal by a level    
def test_get_goals_by_level():
    levels = [
                {
                "nivel": "C",
                "goles": 15
                }
            ]
    player_level = "C"

    level_goals = Player.get_goals_by_level(levels, player_level)

    assert level_goals == 15

# Unit test to valid the get individual percentage
def test_get_individual_percentage():
    player_goals = 9
    level_goals = 10
    individual_percent = Player.get_individual_percentage(player_goals, level_goals)
    
    assert individual_percent == 90

# Unit test to valid the get full percentage
def test_full_percentage():
    individual_percentage = [
                                {
                                    "individual_percent": 100
                                },
                                {
                                    "individual_percent": 90
                                },
                                {
                                    "individual_percent": 100
                                },
                                {
                                    "individual_percent": 100
                                }
                            ]

    full_percentage_list = Player.get_full_percentage(individual_percentage)
    assert len(full_percentage_list)  > 0

def test_get_team_percentage_avg():
    full_percentage = [100, 100, 100, 100]
    full_percentage = Player.get_team_percentage_avg(full_percentage)
    assert full_percentage == 100

def test_get_complete_salary():
    player = {
                "nombre": "Juan Perezz",
                "nivel": "C",
                "goles": 10,
                "sueldo": 50000,
                "bono": 25000,
                "sueldo_completo": "",
                "equipo": "rojo",
                "individual_percent": 100
            }

    team_percentage = 100

    salary = player["sueldo"]
    bonus = player["bono"]

    player_with_complete_salary = Player.get_complete_salary(player, team_percentage)
    complete_salary = player_with_complete_salary["sueldo_completo"]

    assert complete_salary == (bonus + salary)
