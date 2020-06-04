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
                         Item("Rock", "Throw the rock to cause some damage"),
                         Item("Sword", "A sharpened weapon for hand-to-hand combat"),
                         Item("Magical Amulet", "The amulet makes you very lucky, adds protection")
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
                         Item("Holy Chalice", "This chalice grants you easy access to more coins")
                     ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     items=[
                         Item("Torch", "The torch will help you see in dark places")
                     ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     items=[
                         Item("Treasure", "This is the prize you seek!")
                     ]),
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
                 "Are you ready?"]

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

    next_move = ''
    print()

    while next_move.lower() != "q":
        print(f"{player.name} is currently in {player.location.name}:")

        # print the long description with wrapping
        for line in textwrap.wrap(f"{player.location.description}"):
            print('    |', line)
        # show items in location:
        print("Items in this location:")
        for item in player.location.items:
            print('    |', item.name)
            print("    |==========")
            print('    |', item.description)
            print('~~~~~~~~~~')
        next_move = input("Where to next?\nEnter a direction "
                          "(n|e|s|w) or (q) to quit: ")
        print('\n')
        no_go_message = "Oops, can't go there!"
        if next_move.lower() == "n":
            try:
                new_room = player.location.n_to
                no_room_error(new_room)
            except TypeError:
                print(no_go_message)
                continue
        elif next_move.lower() == "e":
            try:
                new_room = player.location.e_to
                no_room_error(new_room)
            except TypeError:
                print(no_go_message)
                continue
        elif next_move.lower() == "s":
            try:
                new_room = player.location.s_to
                no_room_error(new_room)
            except TypeError:
                print(no_go_message)
                continue
        elif next_move.lower() == "w":
            try:
                new_room = player.location.w_to
                no_room_error(new_room)
            except TypeError:
                print(no_go_message)
                continue
        elif next_move.lower() == "q":
            print("Looks like your quest is over...")
            continue
        else:
            print("I don't think that's a valid command...")
            continue
        print(f"Moving To {new_room.name}...", end='\r')
        time.sleep(.60)
        player.update_location(new_room)

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
