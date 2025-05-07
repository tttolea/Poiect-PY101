class Room:
    def __init__(self, description):
        self.description = description
        self.enemy = None
        self.item = None
        self.connections = {}
        self.visited = False  # Track whether this room has been visited

    def describe(self):
        if not self.visited:
            print(f"\nTe afli in: {self.description}")
            self.visited = True  # Mark the room as visited
        else:
            print(f"\nAi mai fost in aceasta camera: {self.description}")
        
    def connect(self, direction, room):
        self.connections[direction] = room

    def add_enemy(self, enemy):
        self.enemy = enemy

    def add_item(self, item):
        self.item = []