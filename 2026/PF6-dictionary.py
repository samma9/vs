# PF6 dictionary
# Samuel Marriott 8/03/2026

# 2D list
quests1 = [
    ["Find the Key", 10],
    ["Defeat the Dragon", 50],
    ["Rescue the Villager", 30]
]

# Rewritten as nested dictionary
quests = {
    "Find the Key": {
        "points": 10,
        "completed": True
    },
    "Defeat the Dragon": {
        "points": 50,
        "completed": False
    },
    "Rescue the Villager": {
        "points": 30,
        "completed": False
    }
}

quest_name = input("Enter quest name: ")

if quest_name in quests: # Check if quest exists. Prevents runtime errors.

    if quests [quest_name]["completed"] == False: # If not completed set to completed
        pts = str(quests[quest_name]["points"])
        quests [quest_name]["completed"] = True
        print(f"Quest completed! You earned {pts} points.")

    elif quests [quest_name]["completed"] == True: # If it is already completed, display a message
        print("This quest has already been completed.")

else:
    print("Quest not found.") # Handles runtime errors (key missing from dictionary)