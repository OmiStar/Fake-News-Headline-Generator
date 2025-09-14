import random

#create list for 3 object

subjects=["SRK","MSD","VIRAT","A CAT","MESSI","CR7","Narendra Modi"]

actions=["CELEBRATES","EATS","ORDERS","DECLARES WAR ON","CANCELS","DANCING"]

places=["AT RED FORT","IN MUMBAI LOCAL TRAIN","IN IPL MATCH","PLATE OF SAMOSA","KERALA","IN A STADIUM"]

#start while loop

while True:
    subject=random.choice(subjects)
    action= random.choice(actions)
    place=random.choice(places)

    headline=f"BREAKING NEWS: {subject} {action} {place}"

    print("\n" + headline)

    user_input=input("Do you want to regenerate this (yes/no)").strip().lower()
    if user_input =="no":
        break
print("\n Thanks for using fake news Headline Generator APP! \n HAVE A FUNNY DAY!!!! ")
