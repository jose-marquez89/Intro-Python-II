class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def add_items(self, *args):
        for item in args:
            self.items.append(item)

    def remove_items(self, *args):
        for item in args:
            idx = self.items.index(item)
            del self.items[idx]

    def __str__(self):
        return "roomName: %s\nroomDescription: %s" % (self.name,
                                                      self.description)

    def __repr__(self):
        return "Room(%s, %s)" % (self.name, self.description)
