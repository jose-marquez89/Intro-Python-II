class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_grab(self):
        print(f"You picked up {self.name}!")

    def on_drop(self):
        print(f"You've dropped {self.name}! It's no longer in your inventory")
