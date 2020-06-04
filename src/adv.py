import sys
import time
import textwrap

from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     items=[
                        Item(
                            "Rock",
                            "Throw the rock to cause some damage"
                        ),
                        Item(
                            "Sword",
                            "A sharpened weapon for hand-to-hand combat"
                        ),
                        Item(
                            "Magical Amulet",
                            "The amulet makes you very lucky, adds protection"
                        )
                     ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     items=[
                         Item("Map", "This map will lead you to the treasure")
                     ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     items=[
                        Item(
                          "Holy Chalice",
                          "This chalice grants you easy access to more coins")
                     ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     items=[
                         Item("Torch",
                              "The torch will help you see in dark places")
                     ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def main():
    greetings = ["Welcome to Generic Adventure 1.0!",
                 "It's time to begin a quest..."]

    def scary_print(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(1)

    def no_room_error(r):
        """Keeps current room from becoming None"""
        if r is None:
            raise TypeError("Current room cannot be NoneType")

    for g in greetings:
        scary_print(g)
        sys.stdout.write('\r')
        sys.stdout.flush()
        sys.stdout.write('\n')

    time.sleep(0.5)
    player_name: str = input("Please enter your name: ")
    player = Player(player_name, room['outside'])

    next_move = ['']
    print()

    while next_move[0] != "q":
        loc = f"{player.name} is currently in {player.location.name}:"
        print("=" * len(loc))
        print(loc)
        print("=" * len(loc))

        # print the long description with wrapping
        for line in textwrap.wrap(f"{player.location.description}"):
            print('    |', line)

        if len(player.location.items) >= 1:
            # show items in location:
            items_in_loc = "Items in this location:"
            print()
            print(items_in_loc)
            print("*" * len(items_in_loc))

            for num, item in enumerate(player.location.items):
                print(f'    |Item no. {num}: ', item.name)
                print("    |~~~~~~~~~~")
                print('    |--->', item.description)
                print('    `~~~~~~~~~~')

        next_move = input("What's next?\nEnter (h) for the command menu "
                          "or (q) to quit: ").lower().split()

        while next_move == []:
            next_move = input("Whoops, wrong command!\nEnter (h) for the "
                              "command menu or (q) to quit: ").lower().split()
        print('\n')
        no_go_message = "Oops, can't go there!"

        # single element command parsing
        if len(next_move) == 1:
            if next_move[0] == "h":
                print("Command Menu: ")
                print("\th".rjust(10),
                      "---> open this menu")
                print("\tn|e|s|w".rjust(10),
                      "---> move in a cardinal direction")
                print("\tgrab [item number]".rjust(10),
                      "---> pick up an item in current room")
                print("\tdrop".rjust(10),
                      "---> abandon an item, opens drop menu")
                input("Press Enter when finished to carry on. ")
                continue
            elif next_move[0] == "n":
                try:
                    new_room = player.location.n_to
                    no_room_error(new_room)
                except TypeError:
                    print(no_go_message)
                    continue
            elif next_move[0] == "e":
                try:
                    new_room = player.location.e_to
                    no_room_error(new_room)
                except TypeError:
                    print(no_go_message)
                    continue
            elif next_move[0] == "s":
                try:
                    new_room = player.location.s_to
                    no_room_error(new_room)
                except TypeError:
                    print(no_go_message)
                    continue
            elif next_move[0] == "w":
                try:
                    new_room = player.location.w_to
                    no_room_error(new_room)
                except TypeError:
                    print(no_go_message)
                    continue
            # drop items is bunched with single element commands
            elif next_move[0] == "drop":
                if len(player.inventory) < 1:
                    print("You don't have any items!", end='\r')
                    time.sleep(0.8)
                    continue
                player.show_inventory()
                to_drop = input("Select an item no to drop: ")
                try:
                    player.drop(player.inventory[int(to_drop)])
                    continue
                except IndexError:
                    print("That item isn't here...", end='\r')
                    time.sleep(0.8)
                    continue
                except ValueError:
                    print("That wasn't an item number!", end='\r')
                    time.sleep(0.8)
                    continue

            elif next_move[0] == "q":
                print("Looks like your quest is over...")
                continue
            else:
                print("I don't think that's a valid command...", end='\r')
                time.sleep(0.8)
                continue
            print(f"Moving To {new_room.name}...", end='\r')
            time.sleep(0.8)
            player.update_location(new_room)
        else:
            if next_move[0] == "grab":
                if len(player.location.items) < 1:
                    print("No items here...", end='\r')
                    time.sleep(0.8)
                    continue
                try:
                    item_to_grab = player.location.items[int(next_move[1])]
                    player.grab(item_to_grab)
                    continue
                except IndexError:
                    print("That item isn't here...",
                          end='\r')
                    time.sleep(1)
                    continue

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
