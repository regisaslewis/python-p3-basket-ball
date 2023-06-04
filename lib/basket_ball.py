def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

def num_points_per_game(name):
    for n in game_dict()["home"]["players"]:
        if n["name"] == name:
            return n["points_per_game"]
    for n in game_dict()["away"]["players"]:
        if n["name"] == name:
            return n["points_per_game"]

def player_age(name):
    for n in game_dict()["home"]["players"]:
        if n["name"] == name:
            return n["age"]
    for n in game_dict()["away"]["players"]:
        if n["name"] == name:
            return n["age"]

def team_colors(team):
    if game_dict()["home"]["team_name"] == team:
        return game_dict()["home"]["colors"]
    else:
        return game_dict()["away"]["colors"]

def team_names():
    names = []
    names.append(game_dict()["home"]["team_name"])
    names.append(game_dict()["away"]["team_name"])
    return names

def player_numbers(team):
    if game_dict()["home"]["team_name"] == team:
        return [n["number"] for n in game_dict()["home"]["players"]]
    if game_dict()["away"]["team_name"] == team:
        return [n["number"] for n in game_dict()["away"]["players"]]

def player_stats(name):
    for n in game_dict()["home"]["players"]:
        if n["name"] == name:
            return n
    for n in game_dict()["away"]["players"]:
        if n["name"] == name:
            return n

def average_rebounds_by_shoe_brand():
    brand_dict = {
        "Nike": [],
        "Adidas": [],
        "Puma": [],
        "Jordan": [],
    }
    for n in game_dict()["home"]["players"]:
        if n["shoe_brand"] == "Nike":
            brand_dict["Nike"].append(n["rebounds_per_game"])
    for n in game_dict()["home"]["players"]:
        if n["shoe_brand"] == "Adidas":
            brand_dict["Adidas"].append(n["rebounds_per_game"])
    for n in game_dict()["home"]["players"]:
        if n["shoe_brand"] == "Puma":
            brand_dict["Puma"].append(n["rebounds_per_game"])
    for n in game_dict()["home"]["players"]:
        if n["shoe_brand"] == "Jordan":
            brand_dict["Jordan"].append(n["rebounds_per_game"])
    for n in game_dict()["away"]["players"]:
        if n["shoe_brand"] == "Nike":
            brand_dict["Nike"].append(n["rebounds_per_game"])
    for n in game_dict()["away"]["players"]:
        if n["shoe_brand"] == "Adidas":
            brand_dict["Adidas"].append(n["rebounds_per_game"])
    for n in game_dict()["away"]["players"]:
        if n["shoe_brand"] == "Puma":
            brand_dict["Puma"].append(n["rebounds_per_game"])
    for n in game_dict()["away"]["players"]:
        if n["shoe_brand"] == "Jordan":
            brand_dict["Jordan"].append(n["rebounds_per_game"])
    print("Nike:  " + "%.2f" % (sum(brand_dict["Nike"]) / len(brand_dict["Nike"])))
    print("Adidas:  " + "%.2f" % (sum(brand_dict["Adidas"]) / len(brand_dict["Adidas"])))
    print("Puma:  " + "%.2f" % (sum(brand_dict["Puma"]) / len(brand_dict["Puma"])))
    print("Jordan:  " + "%.2f" % (sum(brand_dict["Jordan"]) / len(brand_dict["Jordan"])))
