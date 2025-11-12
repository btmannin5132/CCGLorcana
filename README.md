# Disney's Lorcana TCG inside of Lackey CCG

This plugin for Lorcana is to test and play decks inside of Lackey CCG

Lackey can be downloaded for your respective operating system here: https://lackeyccg.com/index.html

After downloading, go to the `plugin` tab on the top and paste the update URL below into the text box and then select `Install or Update from URL!`.

Main Update list url is https://raw.githubusercontent.com/btmannin5132/CCGLorcana/refs/heads/main/updatelist.txt

After that, you can play Lorcana!


lorcana database from https://lorcanajson.org/files/current/en/allCards.json


## Updating the Plugin

1. Run `python LorcanaRip.py`
2. update `updatelist.txt` and `version.txt` with updated dates and comments as needed
3. Transfer `sets/carddata.txt`, `updatelist.txt` and `version.txt` to their proper locations inside of your lackey plugin directory
4. Open Lackey, it should have the updated lists and cards if you want to preview.
5. In the command window on the main board page, run `/mkupdate plugins/lorcana/updatelist.txt`.  This will update the checksums for all of the new files generated.
6. Move the new `updatelistNEW.txt` back to the git directory and rename back to `updatelist.txt` (No need for the version.txt, nothing got updated in there with the terminal command).
7. Commit with useful message.
8. Push to repo

    **Validation Steps:**

9. Close Lackey
10. Go back to the lackey plugin directory, and DELETE `sets/carddata.txt`, `updatelist.txt` and `version.txt`
11. Update the plugin with the url: `https://raw.githubusercontent.com/btmannin5132/CCGLorcana/refs/heads/main/updatelist.txt`.  All of the files should be replaced and updated.


## Setting up Drafts
As of 11/2025, this plugin has booster packs!

You can now perform drafts just like you would in any other TCG.

Follow the steps laid out here: https://www.angelfire.com/funky/magiclackey/drafting.html
This is technically labeled for Magic, so don't worry about the valitation steps or whatnot at the end, but everything else should work the same.

### The main Steps:
#### For each pack:
1. Each player in game goes to `Deck Editor` and then select `Card Pool` next to `All Cards`.
2. Each player selects `Add a pack or Random Deck`.
3. Select the desired set to do a draft from
4. Select `Add directly to` and have `hand` selected

#### For selecting cards:

After a pack is slected, and all players have cards in their hand from a pack:

1. Each player moves one card from their hand to their `sideboard`
2. Make sure everyone is in their `hand` location
3. The host then uses `/exchangeclockwise` or `/exchangecounterclockwise` to rotate the hand cards to the next player

Repeat above steps for as many packs used in the draft.

#### Making a Deck:

After all cards have been moved to the players' decks:
1. All players move to their `sideboard` location
2. Use the command `/copyzonetocardpool` to copy all cards in sideboard to their card pool in the deck editor
3. Go over to the `Deck Editor` to make your deck with the provided cards in the card pool
4. If you every over-select a card, the `verify deck` button on the bottom will turn red, meaning that your deck and the pool do not match.  Selecting the `verify deck` button will remove any cards (or count of cards) to make the deck above compatible with the pool.
5. After the deck is made, select `Load Entire Deck to You` in the middle of the deck editor.
6. The deck will be loaded to your deck in the main game area, and you are ready to play your drafted deck!



