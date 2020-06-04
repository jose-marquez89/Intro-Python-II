import time


class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_grab(self):
        print(f"Picked up the {self.name}!", end='\r')
        time.sleep(.80)

    def on_drop(self):
        print(
          f"{self.name} was left behind!",
          end='\r')
        time.sleep(.80)

    def __str__(self):
        return self.name
