from world import World
from command import Command
from helptext import helpText
from sys import exit

def doCommand(w,currentInput):
    commands = {
      "go": Command(w.go,True),
      "look": Command(w.look,False),
      "whereami": Command(w.whereami,False),
      "carrying": Command(w.carrying,False),
      "lookaround": Command(w.lookaround,False),
      "examine": Command(w.examine,True),
      "take": Command(w.take,True),
      "drop": Command(w.drop,True),
      "save": Command(w.save, False)
      # "use": Command(w.use,True)
    }
    # format input
    if ' ' in currentInput:
      command,params = currentInput.split(None, 1)
    else:
      command = currentInput
      params = ""
    # check for special command
    if command == 'help':
      return(helpText)
    elif command == "exit":
      # shouldSaveGame = input("Would you like to save before you leave? y or n: ")
      # if(shouldSaveGame == "y" or shouldSaveGame == "yes"):
      #   print(commands["save"].useCommand(None))
      return("Thanks for playing!")
      exit()
    else:
    # execute regular command
      try:
        return(commands[command].useCommand(params))
      except KeyError:
        return("command '"+ currentInput + "' not recognized. type 'help' for a list of commands")

def createWorld(gameName):
  # gameName = input("Please enter game folder name (ClueHouse, or custom save folder)")
  w = None
  while w == None:
    try:
      w = World(gameName)
    except Exception as e:
      print("error: " + e)
      exit()
      # print(gameName + " not found.")
      # gameName = input("Please enter game folder name (ClueHouse, or custom save folder)")
  print(gameName + " game loaded!")
  return w
