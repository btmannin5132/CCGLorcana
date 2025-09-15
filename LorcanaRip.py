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
print(setNames)

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
            Set = setNames[12]
        elif card["setCode"] == "Q2":
            Set = setNames[13]
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

    #Add Quest Battlegrounds and special cards

    #Ursula's
    Name = "The Encounter"
    Set = "IQDT"
    ImageFile = "quest1/22_d9a270cca91307dc6726a12cd8f2acb7731"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Easy- Ursula Doesn't draw additional cards for lore each turn"
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 1- Remove 2 damage from chosen character, 2- Ready or Exert Chosen Character, 3- Chosen player draws 2 cards"
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  
    Name = "A Dark Realm"
    Set = "IQDT"
    ImageFile = "quest1/22_d9a270cca913072574f26a12cd8f2acb7731"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Normal"
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 1- Chosen Character gets +2 Pwr this turn, 2- Chosen character gets Resist+1 until the start of your next turn, 3- Each player except Ursula draws a card"
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  
    Name = "The Lair"
    Set = "IQDT"
    ImageFile = "quest1/22_d9a270cca95742cd8f2acb7731"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Hard- Ursula draws 1 more card each turn"
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 1- Deal 1 damage to chosen character, 2- Ready chosen character, 3- Each player except Ursula puts the top card of their deck into their inkwell facedown and exerted"
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  
    Name = "Infinite Wrath"
    Set = "IQDT"
    ImageFile = "quest1/22_d9a270cca91307d2cd8f2acb7731"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Extreme- Ursula draws one more card each turn, Whenever a character of Ursula's is banished, she returns that card to her hand."
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 1- Chosen Character gets +2 Pwr this turn, 2- Chosen character gets Resist+1 until the start of your next turn, 3- Each player except Ursula draws a card"
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  
    #Jafar
    Name = "The Reforged Crown"
    Set = "IQPH"
    ImageFile = "quest2/6_4171647582036dc9af5e08e9283df37"
    type = "Item"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = "No"
    Classifications = ""
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "At the start of their turn, whoever has this item gains 2 lore. If this item would leave play for any reason, Jafar steals it instead. When Jafar has this item, he cannot lose the game."
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  

    Name = "Jafar's Throne Room"
    Set = "IQPH"
    ImageFile = "quest2/6_4171647582036d88c7d8d9af5e08e9283df37"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Easy- Jafar's characters enter play exerted"
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 1- chosen character gets resist+1 until the start of your next turn, 2- Another chosen illumineer gets +2 lore, 3- Deal 5 damage to chosen character or location."
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  
    Name = "Secret Passage"
    Set = "IQPH"
    ImageFile = "quest2/6_4171647582036d88c78d9af5e08e9283df37"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Normal- Jafar stars the game with Inkmoat in play"
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 2- Ready chosen character, they can't quest for the rest of this turn. 2- Chosen illumineer draws a card. 4- Deal 5 damage to chosen location."
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  
    Name = "The Crown Chamber"
    Set = "IQPH"
    ImageFile = "quest2/6_4171647582036d9af5e08e9283df37"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Difficulty: Hard- Jafar begins the game with Ink Moat in play. Jafar's locations gain Resist +1."
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 1 - Chosen Character gets +2 Strength this turn. 2 - Each Illumineer pays 1 ink less for the next character they play this turn. 3 - Each Illumineer puts the top card of their deck into their inkwell facedown and exerted. "
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  
    Name = "Full Alert"
    Set = "IQPH"
    ImageFile = "quest2/6_4171647582036ddd9af5e08e9283df37"
    type = "Battleground"
    Rarity = ""
    Color = ""
    Cost = ""
    Inkwell = ""
    Classifications = "Extreme- Jafar begins the game with Inkmoat in play. Jafar's locations gain Evasive, and +1Lore"
    Strength = ""
    Willpower = ""
    Lore = ""
    Text = "Play abilities: Lore Cost- Effect: 4- Chosen character gains evasive this turn."
    writer.writerow([Name,Set,ImageFile,type,Rarity,Color,Cost,Inkwell,Classifications,Strength,Willpower,Lore,Text])
  


    