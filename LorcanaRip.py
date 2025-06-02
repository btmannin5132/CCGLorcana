"""
Ben Manning
Collects card data for Lorcana and sets up formatting needed for LackeyCCG
lorcana database from https://lorcanajson.org/files/current/en/allCards.json

"""
import urllib.request
import json
import csv

# URL of the Lorcana JSON file
input_file = "allCards.json" 

output_file = "sets/carddata.txt"

# base load with local file just in case
# with open(input_file, "r", encoding="utf-8") as f:
#     data = json.load(f)

#link directly with json file instead of downloading the file every time
#Will take a little longer to run, but probably still less time that resaving the file...
with urllib.request.urlopen("https://lorcanajson.org/files/current/en/allCards.json") as url:
    data = json.load(url)
# print(data)

setNames = [0]
sets = data.get("sets", {})

setKeys = sets.keys()

for key in setKeys:
    thisSet = sets[key]["name"]
    newS = ""
    #print(thisSet)
    for c in thisSet:
        if c.isupper():
            newS += c
    setNames.append(newS)
#print(setNames)

#can add more if want in later sets
#perhaps one for hybrid colors?
headers = ["Name","Set","ImageFile","type","Rarity","Color","Cost","Inkwell","Classifications","Strength","Willpower","Lore","Text"] 

with open(output_file, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter='\t')  # Use tab as delimiter for Lackey CCG
    writer.writerow(headers)
    
    cards = data.get("cards", [])
    cardList = {}
    for card in cards:
        cardList[card["fullName"]] = {}
        Name = card["fullName"]
        #print(Name)

        #the quests have different formatting for some reason...
        if card["setCode"] == "Q1":
            Set = setNames[11]
        elif card["setCode"] == "Q2":
            Set = setNames[12]
        else:
            Set = setNames[int(card["setCode"])]
        type = card["type"]

        #not all of the cards have thumbnails listed, hopefully this catches most of them
        try:
            ImageFile = card["images"]["thumbnail"][47:-4]
        except KeyError:
            print(f"Could not find find thumbnail for {Name}, using full image instead")
            ImageFile = card["images"]["full"][47:-4]

        Rarity = card["rarity"][0:2]
        Cost= card["cost"]
        Color = card["color"]
        Inkwell = card["inkwell"]
        Strength  = ""
        Willpower  = ""
        Lore = ""
        Classifications  = ""
        Text = ""
        Script = ""

        if "flavorText" in card.keys():
            Script = card["flavorText"]
            Script = ''.join(Script.split('\n'))

        
        if "subtypes" in card.keys():
            first = 0
            for type in card["subtypes"]:
                if first != 0:
                    Classifications += ", "
                else:
                    first = 1
                Classifications  += type

        Text = card["fullText"]
        Text = ''.join(Text.split('\n'))

        if card["type"] == "Character":
            Strength  = card["strength"]
            Willpower  = card["willpower"]
            Lore = card["lore"]

        elif card["type"] == "Location":
            Willpower  = card["willpower"]
            Strength = card["moveCost"]
            Lore = card["lore"]

        # print(cardList[card["fullName"]]["name"])
    # Write the row
        writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
        
        


    