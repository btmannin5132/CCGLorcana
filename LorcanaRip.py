import json
import csv

# URL of the Lorcana JSON file
input_file = "allCards.json" 
output_file = "carddata.txt"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# print(data)

setNames = [0]
sets = data.get("sets", {})

setKeys = sets.keys()

for key in setKeys:
    thisSet = sets[key]["name"]
    newS = ""
    # print(thisSet)
    for c in thisSet:
        if c.isupper():
            newS += c
    setNames.append(newS)
    # print(newS)


headers = ["Name",	"Set", "ImageFile",	"type",	"Rarity",	"Color",	"Cost",	"Inkwell",	"Classifications",	"Strength",	"Willpower","Lore",	"Text",	"Script"]

with open(output_file, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter='\t')  # Use tab as delimiter for Lackey CCG
    writer.writerow(headers)
    
    cards = data.get("cards", [])
    cardList = {}
    for card in cards:
        cardList[card["fullName"]] = {}
        Name = card["fullName"]
        Set = setNames[int(card["setCode"])]
        type = card["type"]
        ImageFile = card["images"]["thumbnail"][47:-4]
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

        
        if "subtypes" in card.keys():
            Classifications  = card["subtypes"]

        
        if "abilities" in card.keys():
            for ability in card["abilities"]:
                Text += ability["fullText"] + ","
        else:
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
        writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text,Script])


    