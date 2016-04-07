# CST 205 - Lab 7
# Team: Byte Bistro
# April 4, 2016

# Global variables for player items in game
hasGoldenKey = False
hasHairPin = False
hasRope = False
doorIsOpen = False
windowIsOpen = False
gameRun = True # main condition for game loop

def playGame():

  displayHelp() # displays help prompt with available commands
  currentRoom = getNextRoom("Den") # set currentRoom to "Den" to start the game
  prompt(currentRoom) # displays the current room and description to the user
  
  while(gameRun): # gameRun is True, sets to False when game is over
    input = raw_input("What would you like to do? ")
    
    # begining of main if-else statements. Each case is a user input of type: string
    if input == "help":
      displayHelp()
      input = raw_input("Press ENTER to continue. ") # pauses the screen at the help dialouge
      prompt(currentRoom) # re-print the current room information
      continue
    # main choices for directions of movement
    elif input == "north" or input == "east" or input == "south" or input == "west": 
      currentRoom = goDirection(currentRoom, input) # set the currentRoom to the new room using the direction
      prompt(currentRoom) # display the new room information
    elif input == "exit":
      break # exit kills the main loop condition
    elif input == "look":
      prompt(currentRoom) # displays current room information
    elif input == "open":
      if doesCommandExist(currentRoom): # checks to see if there are objects in the room
        object = raw_input("What would you like to open? ") # asks user what object they would like to open
        string = ""
        
        #loops through objects in room and executes command "open" using the object
        for i in range(0, len(currentRoom[4])):
          if currentRoom[4][i] == object:
            string = executeCommand("open", object, currentRoom[5][i])
        if len(string):
          print(string)
        else:
          print("That object does not exist. ")
      else:
        print("There is nothing to open in this room. ") # if there are no objects
      currentRoom = getNextRoom(currentRoom[0])
    else:
        print("I can't do that for you. ")

# function for getting the next room after a player moves direction
def getNextRoom(string):
  if string == "Den":
    return getDen()
  elif string == "Kitchen":
    return getKitchen()
  elif string == "Study":
    return getStudy()
  elif string == "Lounge":
    return getLounge()
  elif string == "Library":
    return getLibrary();
  elif string == "Ballroom":
    return getBallroom()
  elif string == "Conservatory":
    return getConservatory()
  elif string == "Deck":
    return getDeck()

# function to pull array information from Lounge
def getLounge():
  return ["Lounge", 
         ["north", "south", "west"], 
         ["Library", "Kitchen", "Study"], 
         "You've entered the Lounge.  A portrait of a man hangs in the center.  It feels like someone is watching you.", 
         ["portrait"], 
         ["\nThere is nothing behind this portrait, your imagination is playing with your head"]]

# function to pull array information from Den
def getDen():    
  return ["Den", 
         ["north", "east"],
         ["Study", "Kitchen"], 
         "You've entered the Den. There is a large oriental rug in the center of the room and a coffee table. There is an unopened letter sitting on the table.", 
         ["letter"], 
         ["\n(picks up letter)\nGreetings, You must escape this house. There is only one way out! HAHAHA!"]]

def getKitchen():
  return ["Kitchen", 
         ["north", "west"], 
         ["Lounge", "Den"], 
         "You've entered the kitchen. There is a cabinet and a drawer.", 
         ["cabinet", "drawer"], 
         ["plate", "golden key"]]

def getStudy():
  return ["Study", 
         ["south", "east"], 
         ["Den", "Lounge"], 
         "You've entered the study.  There is a book on the table and a bottled beverage.  You take a seat and rest for a bit.", 
         ["book","beverage"], 
         ["hair pin", "You take a sip... The refreshing feeling sweeps over your body. You stand there shivering because it's so good. "]]

def getBallroom():
  return ["Ballroom", 
         ["west"], 
         ["Library"], 
         "Music is playing faintly from a jukebox, but no one is around.  You get an eerie feeling down your spine.  ", 
         [], 
         []]

def getConservatory():
  if windowIsOpen == True:
    return ["Conservatory", 
           ["south", "west"], 
           ["Library", "Deck"], 
           "You've entered the conservatory.  On the west side of the room you see the open window that leads to a deck.  A chest sits next to it.", 
           ["window","chest"], 
           ["The window is already open! A slight breeze enters the room.", "rope"]]  
  elif hasHairPin == True:
    return ["Conservatory", 
           ["south"], ["Library"], 
           "You've entered the conservatory.  On the west side of the room you see a window that leads to a deck.  A chest sits next to it.", 
           ["window","chest"], 
           ["You try to pick the lock with the hair pin. 'click' You've opened the window! Run 'west' to get away! ", "rope"]]
  else:
    return ["Conservatory", 
           ["south"], 
           ["Library"], 
           "You've entered the conservatory.  On the west side of the room you see a window that leads to a deck.  A chest sits next to it.", 
           ["window","chest"], 
           ["The window is locked. Only if you had something to pick the lock. Maybe you should get some rest.","rope"]]

def getDeck():
  if hasRope == True:
    print("You use the rope to climb down from the deck.  You reached the ground safely.  You've escaped the mansion.")
    global gameRun
    gameRun = False   
    return ["clear!", 
           ["endless"], 
           [""], 
           "You won!", 
           [], 
           []]
  else: 
    return ["Deck", 
           ["east"], 
           ["Conservatory"], 
           "You stand out on the deck. You would not survive the fall. If only you had some rope.", 
           [], 
           []]

def getLibrary():
  if doorIsOpen == True:
    return ["Library", 
           ["north", "south", "east"], 
           ["Conservatory", "Lounge", "Ballroom"], 
           "You are in the library and you stand before the open gold door", 
           ["door"], 
           ["... wait the door is already open!"]]
  elif hasGoldenKey == True:
    return ["Library", 
           ["south", "east"], 
           ["Lounge", "Ballroom"], 
           "You step into the library. A large door is north of you. It appears to be solid gold", 
           ["door"], 
           ["You try your golden key on the door and it opens easily. You have opened the golden door!"]]
  else:
    return ["Library", 
           ["south", "east"], 
           ["Lounge", "Ballroom"], 
           "You step into the library. A large door is north of you.  It appears to be solid gold", 
           ["door"], 
           ["It wont budge. You need a key to open this door."]]

# sets global object variables for the player    
def executeCommand(command, container, object):
  if command == "open":
    if object == "golden key":
      global hasGoldenKey
      hasGoldenKey = True
    if object == "hair pin":
      global hasHairPin
      hasHairPin = True
    if object == "rope":
      global hasRope
      hasRope = True
    if container == "door":
      if hasGoldenKey == True:
        global doorIsOpen
        doorIsOpen = True
      return object
    if container == "window":
      if hasHairPin == True:
        global windowIsOpen
        windowIsOpen = True
      return object
    if container == "letter":
       return object
    else:
      return "You have opened the " + container + " and found a(n) " + object

# checks to see if there are objects in a room, returns True if there are
def doesCommandExist(room):
  return len(room[5])

# displays current room information  
def prompt(currentRoom):
  print("\nYou are currently in the " + currentRoom[0])
  print(currentRoom[3])
  printPossibleDirections(currentRoom)

# sets the player into the next room based on the direction they choose
def goDirection(cur, dir):
  for i in range(0, len(cur[1])):
    if cur[1][i] == dir:
      return getNextRoom(cur[2][i])
  return cur

# prints the directions possible for player to move
def printPossibleDirections(room):
  output = "Your possible directions are: "
  rooms = ""
  for i in range(0, len(room[1])):
    if i == 0:
      rooms = rooms + room[1][i]
    else:
      rooms = rooms + ", " + room[1][i]
  print(output + rooms)
  print("Enter 'help' for more options")

# prints out all commands and their practical function
def displayHelp():
  print("You open your eyes and find yourself in an unfamilliar mansion.  You can't remember what happened to you.  You take a look around and wonder 'Where am I'.") 
  print("\nAvailable commands: ")
  print("north     -    move the player north")
  print("south    -    move the player south")
  print("east      -    move the player east")
  print("west     -    move the player west")
  print("look      -    prints the current room information")
  print("open     -    prompts the user to open a container in the room")
  print("help      -    prints the help dialouge")
  print("exit       -    ends the current game")
