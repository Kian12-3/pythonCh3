"""
Decision Tree Program: [Game recommender]
Team Members: [Kian] and [Elijah]
Date: [11-17-25]
Description: [Gives you game recommendations based of the answers you give]
"""

print("=" * 60)
print("[Game Recommender]")
print("=" * 60)
print()

genre = input("Do you prefer action or strategy games?: ").lower()
device = input("What platform do you use (PC, Console): ").lower()
player = input("Do you enjoy single-player or multiplayer experiences?: ").lower()


print() 
print("-" * 60)
print("RECOMMENDATION:")
print("-" * 60)

if genre == "action":
    if player == "single-player" or "singleplayer":
        # Outcome 1
        if device == "pc":
            print("Recommendation: DOOM Eternal")
            print("Reason: Fast paced action shooter perfect for PC players.")
        else:
            print("Recommendation: God of War")
            print("Reason: Epic action-adventure tailored for console single-player experiences.")
    else:  # multiplayer
        if device == "pc":
            # Outcome 2
            print("Recommendation: Apex Legends")
            print("Reason: A popular multiplayer battle royale with strong PC community.")
        else:
            # Outcome 3
            print("Recommendation: Call of Duty: Black OPs 7")
            print("Reason: Console friendly multiplayer shooter with massive player base.")
else:  # strategy
    if player == "single-player" or "singleplayer":
        # Outcome 4
        if device == "pc":
            print("Clover Pit")
            print("Reason: single-player strategy game ideal for PC.")
        else:
            print("Recommendation: Fire Emblem: Three Houses")
            print("Reason: Console exclusive tactical RPG with single-player story.")
    else:  # multiplayer strategy
        if device == "pc":
            print("League of Legends")
            print("Reason: Real time strategy PVP with strong multiplayer support on PC.")
        else:
            print("Recommendation: Mario Party")
            print("Reason: Fun multiplayer strategy strategy game for console players.")

print()
print("=" * 60)
print("Thank you for using our Game Recommeder")
print("=" * 60)
