#1 - import the random module
import random

#2 - create a list of subjects
subjects = [
    "Donald Trump",
    "Ketyy Perry",
    "Elon Musk",
    "Satyam Nendela",
    "Sundar Pichai",
    "Rojer Federer",
    "Cristiano Ronaldo",
    "Virat Kohli"
]

actions = [
    "launches",    
    "cancels",    
    "dance with",    
    "eats",    
    "declares war on",    
    "orders",    
    "celebrates with",
    "invests in"    
]

places_or_things = [
    "at the White House",
    "in Las Vegas",
    "a mysterious island",
    "silicon valley",
    "inside a google HQ",
    "at a secret location",
    "during a football match",
    "Inside the cricket stadium"
]


#3 start the headline generation function
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_things = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_things} "
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

    #print goodbye message

print("\nThanks for using the Fake News Headline Generator. Have a great day!")
