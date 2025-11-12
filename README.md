lorcana database from https://lorcanajson.org/files/current/en/allCards.json

Main Update list url is https://raw.githubusercontent.com/btmannin5132/CCGLorcana/refs/heads/main/updatelist.txt

## Updating the Plugin

1. Run `python LorcanaRip.py`
2. update `updatelist.txt` and `version.txt` with updated dates and comments as needed
3. Transfer `sets/carddata.txt`, `updatelist.txt` and `version.txt` to their proper locations inside of your lackey plugin directory
4. Open Lackey, it should have the updated lists and cards if you want to preview.
5. In the command window on the main board page, run `/mkupdate plugins/lorcana/updatelist.txt`.  This will update the checksums for all of the new files generated.
6. Move the new `updatelistNEW.txt` back to the git directory and rename back to `updatelist.txt` (No need for the version.txt, nothing got updated in there with the terminal command).
7. Commit with useful message.
8. Push to repo