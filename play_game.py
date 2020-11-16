import json, time, random

def main():
    # TODO: allow them to choose from multiple JSON files?
    with open('spooky_mansion.json') as fp:
        game = json.load(fp)
    print_instructions()
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)


def play(rooms):
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...']
    start_time = time.time()
    cat_fed = False
    cat_loc = random.choice(list(rooms))

    while True:
        print("")
        print("")
        
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        print(here["description"])
        if len(here["items"]) > 0:
            print("For the taking:")
            for i in range(len(here["items"])):
                print(" - ", here["items"][i])

        # TODO: print any available items in the room...
        # e.g., There is a Mansion Key.

        # Is this a game-over?
        if here.get("ends_game", False):
            end_time = time.time()
            break
        
        if cat_fed == False:
            if cat_loc == current_place:
                if "Canned Tuna" in here["items"]:
                    print("You open the canned tuna and place it on the floor. The cat is overjoyed!")
                    here["items"].remove("Canned Tuna")
                    print("...")
                    print("The cat raises its head, revealing a large key around its collar. You got a mansion key!")
                    stuff.append("Mansion Key")
                    cat_fed = True
                    continue
                if "Canned Tuna" in stuff:
                    print("A small black cat wanders into the room and starts puring at your feet. It must smell the fish!")
                else:
                    print("A small black cat wanders around the room. It looks hungry.")

        # Allow the user to choose an exit:
        usable_exits,missing_key = find_usable_exits(here, stuff)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))

        # See what they typed:
        action = input("> ").lower().strip()

        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break
        
        if action == "help":
            print_instructions()
            continue
        
        if action == "cat":
            cat_loc = "basement"
            continue
        
        if action == "stuff":
            print("You have:")
            if len(stuff) == 0:
                print(" - Nothing...")
            else:
                for i in range(len(stuff)):
                    print(" - ", stuff[i])
            continue
        
        if action == "take":
            print("You took: ")
            for i in range(len(here["items"])):
                print(" - ", here["items"][i])
                stuff.append(here["items"][i])
            here["items"].clear()
            continue
        
        if action == "drop":
            print("What will you drop?")
            for i in range(len(stuff)):
                print(" {}. {}".format(i+1, stuff[i]))
            dropselect = input("> ").lower().strip()
            itemdrop = int(dropselect) - 1
            here["items"].append(stuff[itemdrop])
            stuff.remove(stuff[itemdrop])
            continue
        
        if action == "search":
            found_hidden = False
            for exit in here["exits"]:
                hidden = exit.get("hidden")
                if hidden == True:
                    exit['hidden'] = False
                    print("Your search is fruitful!")
                    found_hidden = True
            if found_hidden == False:
                print("You search high and low to no avail...")
            continue

        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        # TODO: if they type "take", grab any items in the room.
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            if selected in missing_key:
                print("This exit is locked. You must find the key.")
            else:
                current_place = selected['destination']
                cat_loc = random.choice(list(rooms))
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("You finished in", int(end_time - start_time), "seconds.")
    print("")
    print("=== GAME OVER ===")

def find_usable_exits(room, stuff):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) and don't require a key!
    """
    usable = []
    missing_key = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue
        if "required_key" in exit:
            if exit["required_key"] in stuff:
                usable.append(exit)
                continue
            else:
                missing_key.append(exit)
                usable.append(exit)
                continue
            continue
        usable.append(exit)
    return usable, missing_key

def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print(" - Type 'help' to view instructions again.")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()