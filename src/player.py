class Player:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def update_location(self, new_location):
        self.location = new_location

    def grab(self, item: object):
        """Take an item, triggers item 'on_take' printout"""
        self.inventory.append(item)
        self.location.remove_items(item)
        item.on_grab()

    def drop(self, item: object):
        """Drop an item, triggers item 'on_drop' printout"""
        idx = self.inventory.index(item)
        self.location.add_items(item)
        del self.inventory[idx]
        item.on_drop()

    def show_inventory(self):
        print("Your Items:")
        for idx, item in enumerate(self.inventory):
            print("\t", f"Item no. {idx}: {item}")
