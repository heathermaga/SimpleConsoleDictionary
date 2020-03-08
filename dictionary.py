import json
import os
from os import system, name
from difflib import SequenceMatcher, get_close_matches

# found at https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
  if name =='nt':
    _ = system("cls")
  else:
    _ = system("clear")

if os.path.exists("data.json"): 
  data = json.load(open("data.json","r"))
else:
  print("dictionary does not exist")

def formatdef(defi):
  defi = defi[2:]
  defi = defi[:-2]
  defi = defi.replace("', '","\n\n")
  defi = "\n" + "\033[94m" + "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+" + "\x1b[0m" + "\n" + defi + "\n" + "\033[94m" + "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+" + "\x1b[0m" + "\n"
  return defi

def getDef(word):
  if word in data:
    definition = str(data[word])
    definition = formatdef(definition)
    return definition
  elif word.title() in data:
    definition = str(data[word.title()])
    definition = formatdef(definition)
    return definition
  elif word.upper() in data:
    definition = str(data[word.upper()])
    definition = formatdef(definition)
    return definition
  else:  
    if len(get_close_matches(word, data.keys(),cutoff=0.8)) > 0:
      maybe = get_close_matches(word, data.keys(),cutoff=0.8)[0]
      yn = input("\n\n" + "\033[91m" + "Did you mean " + maybe + "? Enter Y for yes, N for no" + "\x1b[0m" + "\n\n")
      if yn.upper() == "Y":
        definition = str(data[get_close_matches(word, data.keys(),cutoff=0.8)[0]])
        definition = formatdef(definition)
        clear()
        print(f"{bcolors.BOLD}{maybe.lower()}:{bcolors.ENDC}")
        return definition
      else:
        return "\n\n" + "\033[91m" + "_,.-'~'-.,__ cannot find a definition for " + word + " __,.-'~'-.,_" + "\x1b[0m" + "\n\n"
    else:
      return "\n\n" + "\033[91m" + "_,.-'~'-.,__ cannot find a definition for " + word + " __,.-'~'-.,_" + "\x1b[0m" + "\n\n"

clear()
print(f"{bcolors.HEADER}{bcolors.BOLD}Welcome to the dictionary! Definitions are deperated by line breaks. You can exit the dictionary by entering \end at the prompt.{bcolors.ENDC}")

while True:
  theword = input(f"Enter the word: ")
  clear()
  if theword == "\end":
    break
  else:
    print(f"{bcolors.BOLD}{theword.upper()}:{bcolors.ENDC}")
    thedef = getDef(theword.lower())
    print(thedef)
    print(f"{bcolors.WARNING}(To exit enter \end){bcolors.ENDC}")
    continue



