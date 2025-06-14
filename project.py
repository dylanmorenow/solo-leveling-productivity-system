import json
import sys

def main():
    data = load_data()
    name = input("What is your ID? ")
    player = check_player(data, name)

    while True:
        try:
            print("\n==Solo Leveling Productivity System==")
            print(f"Player: {name} | Rank: {player['rank']}")
            print("1. My Stats")
            print("2. Show Quest")
            print("3. Add Quest")
            print("4. Complete Quest")
            print("5. Quit")

            choice = int(input("\nChoose a number: "))
            if choice == 1:
                print(check_stats(player, name))
            elif choice == 2:
                show_quest(player)
            elif choice == 3:
                add_quest(player, data, name)
            elif choice == 4:
                complete_quest(player, data, name)
            elif choice == 5:
                sys.exit()
            else:
                raise ValueError("Number is not in option")

        except ValueError:
            print("Please enter an invalid number!")

def load_data(filename="player_data.json"):
    with open(filename, "r") as file:
        return json.load(file)

def check_player(data, name):
    if name in data["id"]:
        print(f"Welcome back {name}!")
        return data["id"][name]
    else:
        print(f"New player created: {name}!")
        data["id"][name] = {
            "level": 1,
            "exp": 0,
            "rank": "E",
            "active_quests": {},
            "completed_quests": 0
        }

        save_data(data)
        return data["id"][name]


def check_stats(player_data, name):
    id = name
    level = player_data["level"]
    exp = player_data["exp"]
    exp_to_next_level = 100 * int(level)
    rank = player_data["rank"]
    active_quests = len(player_data["active_quests"])
    completed_quests = player_data["completed_quests"]

    return f"Player: {id} | Rank: {rank} | Level: {level} | EXP: {exp}/{exp_to_next_level}\nActive Quests: {active_quests} Completed Quests: {completed_quests}"


def show_quest(player_data):
    if len(player_data["active_quests"]) == 0:
        print("There is no active quests!")
        return
    else:
        num = 1
        for quest in player_data["active_quests"]:
            print(f"{num}. {quest}")
            num += 1


def add_quest(player_data, data, name):
    new_quest = input("What is your new quest? ")
    if not new_quest:
        print("Quest name cannot be empty!")
        return

    try:
        new_exp = int(input("How many EXP would you rate this quest? "))
        if new_exp <= 0:
            print("EXP must be positive!")
            return
    except ValueError:
        print("Please enter a valid number for EXP!")
        return

    player_data["active_quests"][new_quest] = new_exp
    print(f"Quest '{new_quest}' added with {new_exp} EXP reward!")

    data["id"][name] = player_data
    save_data(data)
    return

def complete_quest(player_data, data, name):
    if len(player_data["active_quests"]) == 0:
        print("There is no active quests!")
        return
    else:
        num = 1
        for quest in player_data["active_quests"]:
            print(f"{num}. {quest}")
            num += 1


    quest_list = list(player_data["active_quests"].keys())
    choice = int(input("Which quest do you want to complete? ")) - 1

    try:
        if choice >= len(quest_list):
            raise ValueError("Your option is not in the list!")
        else:
            quest_name = quest_list[choice]
            add_exp = player_data["active_quests"][quest_name]
            player_data["exp"] += add_exp
            player_data["completed_quests"] += 1
            del player_data["active_quests"][quest_name]

            print(f"Quest '{quest_name}' completed! Earned: {add_exp} EXP")

            data["id"][name] = player_data
            save_data(data)
            check_level_up(player_data, data, name)

    except ValueError:
        print("Please enter a valid number!")


def check_level_up(player_data, data, name):
    exp_needed = 100 * player_data["level"]
    while player_data["exp"] >= exp_needed:
        player_data["level"] += 1
        player_data["exp"] -= exp_needed
        print(f"Level up! Current Level: {player_data['level']}!")

    if player_data["level"] >= 25:
        player_data["rank"] = "S"
    elif player_data["level"] >= 20:
        player_data["rank"] = "A"
    elif player_data["level"] >= 15:
        player_data["rank"] = "B"
    elif player_data["level"] >= 10:
        player_data["rank"] = "C"
    elif player_data["level"] >= 5:
        player_data["rank"] = "D"

        data["id"][name] = player_data
        save_data(data)


def save_data(data, filename="player_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
