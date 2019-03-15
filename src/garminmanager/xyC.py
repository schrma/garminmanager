class xyC:

    def __init__(self):
        self.x = []
        self.y = []

    def encode_to_json(self):
        return "{" + str(self.x) + " , " + str(self.y) + "}"