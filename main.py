print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island, Great Warrior!\n Your mission is to find the treasure...let's go")

path1 = input("The great zumba skull has been hidden away somewhere in the Malala cave and you either find it or die. What would be your first step?'left' or 'right'? ").lower()

#if the user chooses right
if path1 == 'right':
  print("Your first step was a wrong step perhaps it is the destiny of another to discover the hidden treasure, better luck next time!")
  
#if user chooses left
elif path1 == "left":
  path2 = input("Great choice, you are one step closer to the skull. You have reached the ice chamber of the Malala cave, where do you turn to next? 'left' or 'right'? ").lower()

#if the user chooses right
if path2 == "right":
  print("Time to say goodbye, Great Warrior, we have come to the end of your journey as you have stepped into a trap! We hope to see you again")

#if the user chooses left
if path2 == "left":
  door = input("Great choice again! You have now come face to face with the toughest choice in this challenge. There are three doors coloured red, blue and yellow in front of you. Only one door leads you directly to the skull. Now make your choice: 'red', 'blue' or 'yellow'? ")

#Allow user make final choice
if door == "red":
  print("To the family of a lost soul, a great warrior met death burned by fire in a fiery red room. Take heart!!!")
elif door =="blue":
  print("To the family of a lost soul, a great warrior met death drowned in the wet blue room. Take heart!!!")
elif door == "yellow":
  print("You have found the great zumba skull. In your hand lies the power to make and break nations. Congratulations!!!")
else:
  print("Game Over")
