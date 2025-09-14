import random
from datetime import datetime

def get_category_data(choice):
    match choice:
        case "sports":
            return {
                "subjects": ["MSD", "VIRAT", "MESSI", "CR7", "SERENA WILLIAMS", "ROGER FEDERER"],
                "actions": ["SCORES", "EATS", "ORDERS", "RETURNS", "CANCELS", "DANCES"],
                "places": ["IN WORLD CUP FINAL", "AT WIMBLEDON", "IN IPL MATCH", "AT FOOTBALL STADIUM", "IN TOKYO", "AT RED FORT"]
            }
        case "politics":
            return {
                "subjects": ["MODI", "BIDEN", "PUTIN", "TRUMP", "OBAMA", "SUNAK"],
                "actions": ["DECLARES", "CANCELS", "SUPPORTS", "FIGHTS WITH", "CELEBRATES", "EATS"],
                "places": ["AT PARLIAMENT", "IN WHITE HOUSE", "IN LONDON", "AT RED FORT", "IN DELHI", "IN NEW YORK"]
            }
        case "funny":
            return {
                "subjects": ["A CAT", "MY NEIGHBOR", "SRK", "A DOG", "ALIEN", "SPONGEBOB"],
                "actions": ["EATS", "DANCES WITH", "DECLARES WAR ON", "ORDERS", "CELEBRATES", "SINGS"],
                "places": ["IN MUMBAI LOCAL TRAIN", "AT A WEDDING", "IN KERALA", "ON THE MOON", "IN A STADIUM", "AT MCDONALD'S"]
            }
        case _:
            print("⚠ Invalid choice, defaulting to 'funny'")
            return {
                "subjects": ["A CAT", "MY NEIGHBOR", "SRK", "A DOG", "ALIEN", "SPONGEBOB"],
                "actions": ["EATS", "DANCES WITH", "DECLARES WAR ON", "ORDERS", "CELEBRATES", "SINGS"],
                "places": ["IN MUMBAI LOCAL TRAIN", "AT A WEDDING", "IN KERALA", "ON THE MOON", "IN A STADIUM", "AT MCDONALD'S"]
            }
# Main Programm

print("\nAvailable categories: sports, politics, funny")
user_choice = input("Enter your category choice: ").strip().lower()

category_data = get_category_data(user_choice)

# Ask if user to add their friend’s name
custom_subject = input("Do you want to add your own subject (friend’s name)? (yes/no): ").strip().lower()
if custom_subject == "yes":
    friend_name = input("Enter your friend’s name: ").strip()
    category_data["subjects"].append(friend_name)

# List to store generated headlines
headlines_list = []

# Start generating fake news headlines
while True:
    subject = random.choice(category_data["subjects"])
    action = random.choice(category_data["actions"])
    place = random.choice(category_data["places"])

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    headlines_list.append(headline)

    user_input = input("Do you want to regenerate this (yes/no)? ").strip().lower()
    if user_input == "no":
        break

# Ask if user wants to save to file
save_choice = input("Do you want to save the results to a text file? (yes/no): ").strip().lower()
if save_choice == "yes":
    filename = f"fake_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(headlines_list))
    print(f"\n Headlines saved to '{filename}'")

print("\nThanks for using Fake News Headline Generator APP! \nHAVE A FUNNY DAY!!!! ")
