# Text Adventure (Files)

The goal of this project is to work on a text adventure engine that is run out of a JSON file. [JSON](https://www.json.org/json-en.html) lets us encode dictionaries, lists, strings, and integers into a file in a standard way; Python can read it with the built-in module ``json``.

```
=== Instructions ===
 - Type a number to select an exit.
 - Type 'stuff' to see what you're carrying.
 - Type 'take' to pick up an item.
 - Type 'quit' to exit the game.
 - Type 'search' to take a deeper look at a room.
=== Instructions ===

You are about to play 'Adventure'! Good luck!


You're in a lecture hall, for some reason.
  1. A door leads into the hall.
> nap
I don't understand 'nap'...
You're in a lecture hall, for some reason.
  1. A door leads into the hall.
> 1
...
This is a hallway with many locked doors.
  1. Go back into the classroom.
  2. A door with the words STAIRS is stuck open.
> 2
...
The staircase leads downward.
  1. Nevermind; go back to the hallway.
  2. A door at the bottom of the stairs has a red, glowing, EXIT sign.
> 2
...
You've escaped! It's cold out.


=== GAME OVER ===
```

## On your own / getting-started:

1. Click on the green "Code" button and then on the "Download Zip".
2. Find this ``main.zip`` in your downloads folder and extract it to a place you'll want to work on the code.
3. Open ``play_game.py`` in Thonny, and play the "Adventure" game (default).
4. Read (for understanding) both ``play_game.py`` and ``adventure.py``. ``play_game.py`` loads the game from ``adventure.json`` and runs it in a generic way. ``adventure.py`` creates ``adventure.json`` because creating the data directly would be tedious and error-prone.
5. Modify ``adventure.py`` to have another classroom. Run ``adventure.py`` to regenerate ``adventure.json``, and play it again.
6. Modify ``play_game.py`` so you can explore the "Spooky Mansion" inside ``spooky_mansion.json``.
    - I suggest drawing a map.
    - Once you implement items there are three exits to the game; before there are just two.

### What can we add? Smaller tasks (~4 each ... up to 42)

- (4) When the user types ``help``; print the instructions again. Add this option to the listing of instructions. You'll need Python's ``continue`` statement.
- If it's not nailed down...
    - (4) Make a ``stuff`` command that prints out the user's items or "You have nothing."
    - (4) After printing the description of a "room", print out any items that exist "for the taking".
    - (4) Make a ``take`` command work to take all the items and put them in the player's ``stuff``.
    - (4) Make a ``drop`` command that lets the user drop a specific item, and attach it to the current location. (It should be there if they decide to come back for it).
- (4) Make a ``search`` command that makes any ``hidden`` exits visible (and selectable).
- (6) Use ``os.listdir`` to list the files in the current directory; find all the ``.json`` files, and ask the user which game they would like to play in the ``main`` of ``play_game.py``.
- (6) ***No bridges to nowhere:*** write a function that loops over every room, then over every exit in each room, to ensure that no exits point at non-existent rooms. Typos happen; this can catch them!
- (6) Investigate Python's ``time`` module so that you can keep track of how many minutes and seconds the user has been trapped in your game.

### Bigger Challenges: (~10 each ... up to 64)

- (10) (Creative) Create your own adventure. It should come with some helper-functions.
    - For example, if you want to do something in the style of the mansion, write a helper function that ``create_closet(room)`` that creates a closet for whatever room you call it on; (all or most closets can be boring) but creates a new room and two exits as needed.
- (8) (Cats) Create a black cat that wanders from room to room. Announce the existence of the cat when you happen to be in the same place as it.
    - (4) If the player has some sort of cat treat (raw fish?), have it purr and not leave the room if they're in the same place.
- (8) (Software Engineering) -- Get your code/project onto Github! 
- (10) (String Search) -- Instead of selecting exits from a numbered list; allow the user to type whatever they want; then search through the list of exits for the best match (being vague here to give you some freedom).
- (12) (AI) Implement a ``game_checker.py`` that loads up a JSON file and tells the user if the game is solvable -- if you can reach an ``ends_game`` room -- (go ahead and ignore items, for simplicity). 
    - Recursion is pretty helpful for this: if the current location ``ends_game``, then it's solvable. Otherwise, mark the current room as ``visited``, and then try all the rooms that you can get to from the current room that you haven't already ``visited``.
- (12) Giant unmarked switches: it just wouldn't be a text adventure if there weren't a switch that changes something out of sight. For simplicity, think about having exits become visible or invisible as this switch is toggled.