
print("""
──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──
      

Welcome to my island!
There are two doors in front of you. 🚪a red door and 🚪a blue door 
      """)
door = input ("Which door do you want to open? ").lower()

if door == "red":

   print (" you found three boxes : 🎁 white, 🎁 black, 🎁 green ")

   box = input ("Which box do you open?").lower()

   if box == "white" :
      print ("Oops! You opened a box filled with snakes 🐍🐍🐍")

   elif box == "black" :
        print ("Oops! You opened a box filled with spiders 🕷🕸🕷🕸🕷")

   elif box == "green" :
        print ("Congratulations! You found the treasure! 💰💰💰")
   else :
        print ("Invalid choice! 🙅🙅🙅")

elif door == "blue":
    print ("""
    Oops! You chose the crocodile door .
    Game over!🐊🐊🐊 
    """)

else :
    print(" Invalid choice! 🙅🙅🙅")
