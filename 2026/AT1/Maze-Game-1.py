# 🧩 MAZE GAME
# Year 11SE AT1 Programming Fundamentals

# You will build and improve this program across the unit.
# By the end, your game should include:
# ✔ at least 8 rooms
# ✔ items you can collect 🎒
# ✔ scoring ⭐
# ✔ save/load 💾
# ✔ clear instructions for the user

# 💡 You CAN use emojis in descriptions and messages!

# Samuel Marriott
# Started: 5/04/2026
# Due finish: 24/04/2026
# Finished: Date/Month/2026

# ----------------------------------
# 🗺️ ROOMS (ADD MORE APPROPRIATE TO YOUR THEME)
# ----------------------------------
rooms = {
    "Room 1": {
        "desc": "A hint of light is visible ahead.",
        "forward": "Room 2",
        "pos": {"r": 21, "c": 24}
    },
    "Room 2": {
        "desc": "A long wooden bridge stretches ahead, but there is a pile of rocks in the way.",
        "backward": "Room 1",
        "left": "Room 3",
        "right": "Room 4",
        "forward": "Room 5",
        "pos": {"r": 14, "c": 24}
    },
    "Room 3": {
        "desc": "An item lies on your left.",
        "item": "🔑 key",
        "right": "Room 2",
        "forward": "Room 6",
        "pos": {"r": 14, "c": 6}
    },
    "Room 4":{
        "desc": "An item lies in front of you, and there is a locked door behind."
        "You must find the ancient key that opens it."
        "There is a locked door here. You must find the key that opens it.",
        "requires": "🔑 key",
        "item": "⛏️ pickaxe",
        "left": "Room 2",
        "forward": "Room 7",
        "pos": {"r": 14, "c": 46}
    },
    "Room 5": {
        "desc": "A massive cave surrounds."
        "Decide where to go carefully, as one of the bridges will collapse beneath you.",
        "item": "shield",
        "requires": "⛏️ pickaxe",
        "left": "Room 6",
        "right": "Room 7",
        "forward": "Room 10",
        "backward": "Room 2",
        "pos": {"r": 8, "c": 25}
    },
    "Room 6": {
        "desc": "An item lies and a locked door is in front. You must find the key that opens it. "
        "Note: The key is not the item that lies in front.",
        "item": "🗡️ sword",
        "forward": "Room 9",
        "backward": "Room 3",
        "right": "Room 5",
        "pos": {"r": 8, "c": 5}
    },
    "Room 7": {
        "desc": "There is a wave of mobs preventing you from getting further."
        "Use your sword to defeat the mobs. Use your shield to deflect their attacks.",
        "requires": "🗡️ sword",
        "forward": "Room 8",
        "backward": "Room 4",
        "left": "Room 5",
        "pos": {"r": 8, "c": 48}
    },
    "Room 8":{
        "desc": "",
        "item": "🧪 potion bottle of regeneration",
        "backward": "Room 7",
        "left": "Room 10",
        "pos": {"r": 2, "c": 44}
    },
    "Room 9": {
        "desc": "A set of something and a bottle lies beneath you.",
        "item": "armour set",
        "right": "Room 10",
        "backward": "Room 6",
        "pos": {"r": 2, "c": 4}
    },
    "Room 10": {
        "desc": "There is a monster preventing you from getting the key for the Room 8 door."
        "You must defeat the monster.",
        "item": "🔑 key",
        "left": "Room 9",
        "right": "Room 8",
        "backward": "Room 5",
        "pos": {"r": 2, "c": 21}
    }

    # 👉 ADD MORE ROOMS
    # You need at least 8 rooms for the task
}

# Items collected will go here
inventory = []

# ⭐ You will create a scoring system later
score = 0

# ----------------------------------
# 🎮 INTRO + HELP
# ----------------------------------
def show_intro():
    print("\n🏁 Welcome to the Maze Game!")
    print("Explore the maze, collect items and earn points.")
    print("You must go to each room in numerical order.")
    print("There will be entities preventing you from skipping numbers.")
    print("Type 'help' to see commands.\n")


def show_help():
    print("\n📜 Commands you can use:")
    print("- forward / backward / left / right \n ➡️ move between rooms")
    print("- help                   \n ❓ show commands")
    print("- quit                   \n 🚪 exit the game")
    print("- inventory              \n 🎒 check your bag")
    print("- pick up                \n 🧹 collect item")
    print("- save                   \n 🛟 save your progress")
    print("- load                   \n 💾 load your saved progress")
    print("- score                  \n ⭐  check how many points you have")
    print("- map                    \n 🗺️  show map of your current location")
    print("- use item:",   "\n use the item you wish to use in that circumstance")
    # 👉 Add more commands such as:
    # inventory
    # pick up item
    # save
    # load
    # score
    # map

# ----------------------------------
# 💾 LOAD/SAVE GAME & SCORE
# ----------------------------------
def save_game(current_room, score):
    with open("maze_game.txt", "w") as game_file:
        game_file.write(current_room + "\n") # Save the current room on the first line
        game_file.write(",".join(inventory)) # Save inventory items as a comma_separated list
    with open("maze_game_score.txt", "w") as score_file:
        score_file.write(str(score))

    print("\n 💾 Game saved successfully!")

def load_game():
    global inventory
    try:
        with open("maze_game.txt", "r") as game_file:
            lines = game_file.readlines()
            room = lines[0].strip() # Read the first line for the current room
            if len(lines) > 1: # Read inventory
                inventory = lines[1].strip().split(",")
            else:
                inventory = []

        
        with open("maze_game_score.txt", "r") as score_file:
            score = int(score_file.read().strip())

        print("\n 💾 Game loaded successfully!")
        return room, score
    except FileNotFoundError:
        print("\n ⚠️ No saved file found. Starting new game...")
        return "Room 1", 0 # Default starting room and score

# ----------------------------------
# 🗺️ MAP
# ----------------------------------
# COLUMNS  10        20        30        40        50
           #01234567890123456789012345678901234567890123456789       
def map(current_room):
    map = [                                                     # ROWS
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n", # 0
        "▒         ▒                    ▒                 ▒\n", # 1
        "▒  💎  𐂫      👹      🗝️ 🏹     👿                ▒\n", # 2
        "▒         ▒                    ▒                 ▒\n", # 3
        "▒         ▒                    ▒                 ▒\n", # 4
        "▒▒▒▒🚪▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒🪤 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 5
        "▒        ▒                     ▒                 ▒\n", # 6 
        "▒        ▒                     ▒                 ▒\n", # 7
        "▒  🗡️                   🛡️       👿           🧪   ▒\n", # 8
        "▒        ▒                     ▒                 ▒\n", # 9
        "▒        ▒                     ▒                 ▒\n", # 10
        "▒▒▒▒🪤 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒🪨 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒👿▒\n", # 11
        "▒             ▒                  ▒               ▒\n", # 12
        "▒             ▒           💡     ▒               ▒\n", # 13
        "▒    🔑                          🚪           ⛏️  ▒\n", # 14
        "▒             ▒                  ▒               ▒\n", # 15
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒🚪▒\n", # 16
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 17
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 18
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 19
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n", # 20
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒\n"  # 21
    ]
    # Legend
    print("\n Legend:" \
    "\n - 👿: Mob/monster - you must encounter these to be able to move on." \
    "\n - 👹: Apex predator - you must put on your armour first before swiping him with your sword." \
    "\n - 🚪: Locked door - use items collected to open these." \
    "\n - 💎: Gems - must be collected to repair weapons and armory." \
    "\n - 🪨 : Rocks - must be cleared to progress." \
    "\n - 🪤 : Traps - you will die if you walk into these." \
    "\n - 💡: Lights - will help you to navigate through the dark passages."
    "\n - The other symbols are items. \nYou need these to unlock doors or defeat mobs.")
    print("The numbers in each room are the room numbers. \n You must visit each room in numerical order.\n")

    current_pos = {"r": rooms[current_room]["pos"]["r"], "c": rooms[current_room]["pos"]["c"]}
    show_map(map, current_pos)

def show_map(map, pos):
    r = 0  # row zero 
    player = "웃"
    rows = len(map)
    while r < rows:
        c = 0
        rowString = map[r]
        rowlen = len(rowString)
        while c < rowlen:  # print each column in row
            if c == pos["c"] and r == pos["r"]:
                print(player, end="") 
                c+=1 # double wide character, so move to next column.
            else:
                print(rowString[c], end="") 
                # https://www.w3schools.com/python/ref_func_print.asp
            c+=1
        r+=1
    
# ----------------------------------
# 📍 SHOW CURRENT ROOM
# ----------------------------------
def show_room(current_room):
    print(f"\n📍 You are in {current_room}.")
    print(rooms[current_room]["desc"])

    # 👉 When you add items to rooms, you can show them here like this:
    if "item" in rooms[current_room]:
        print("👀 You have found a(n):", "".join(rooms[current_room]["item"]))
    else:
        print("No item here.")

# 🎒 Items collected will go here
def collect_item(current_room):
    if "item" in rooms[current_room]:
        inventory.append(rooms[current_room]["item"])
        print(inventory)
    else:
        print("No item to collect in this room.")
        print(inventory)

def check_bag():
    if inventory == []:
        print("You have nothing in your bag.")
    else:
        print(f"You have {inventory} in your bag")

# ----------------------------------
# 🚶 MOVE BETWEEN ROOMS
# ----------------------------------
def move(direction, current_room):
    global inventory
    # Check if the direction exists in this room
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        # Check if new room has a requirement, and if passages have traps and/or monsters.
        if "requires" in rooms[new_room] and rooms[new_room]["requires"] not in inventory:
            print(f"\n 🔒 You need a {rooms[new_room]['requires']} to enter {new_room}!")
            return current_room # Stay in the current room
        elif current_room == "Room 3" and direction == "forward" or current_room == "Room 6" and direction == "backward":
            print("Bad luck. You walked into a trap and died.")
            current_room = "Room 1"
            inventory = []
            return current_room
        elif current_room == "Room 5" and direction == "forward" or current_room == "Room 10" and direction == "backward":
            print("Nice try. The bridge collapsed beneath you and you fell to your death.")
            current_room = "Room 1"
            inventory = []
            return current_room
        else:
            print(f"\n🚶 You moved {direction} to {new_room}.")
            return new_room
    # If the direction is not valid
    else:
        print("\n⛔ You can't go that way!")
        return current_room


# ----------------------------------
# 🔁 MAIN GAME LOOP
# ----------------------------------
def game_loop():
    # Starting room
    current_room = "Room 1"
    show_intro()

    while True:
        show_room(current_room)
        
        # Ask the player for a command
        command = input("\n> ").strip().lower()

        # Movement commands
        if command in ("forward", "backward", "left", "right"):
            current_room = move(command, current_room)

        # Show help
        elif command == "help":
            show_help()
        
        # Show map
        elif command == "map":
            map(current_room)
        
        # Collect item
        elif command == "pick up":
            collect_item(current_room)
        
        # Check inventory
        elif command == "inventory":
            check_bag()
        
        # Save game
        elif command == "save":
            save_game(current_room, inventory, score)

        # Load saved progress
        elif command == "load":
            load_game()

        # Quit game
        elif command == "quit":
            print("\n👋 Thanks for playing!")
            break

        # Anything else = invalid
        else:
            print("\n❌ Invalid command.")
            show_help()

# ----------------------------------
# ▶️ START GAME
# ----------------------------------
if __name__ == "__main__":
    game_loop()