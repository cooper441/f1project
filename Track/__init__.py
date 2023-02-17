class Track:
    cornersList = []

    def __init__(self, name, location, length, corners, straight):
        self.name = str(name)
        self.location = str(location)
        self.length = float(length)
        self.corners = corners
        Track.cornersList.append(corners)
        self.straight = straight()

    def __call__(self):
        return self

    @classmethod
    def create_corner(self):
        obj = Corner(0, 0, 0, "")
        return obj

    @classmethod
    def create_straight(self):
        obj = Straight(0, 0, 0)
        return obj


class Corner:
    def __init__(self, difficulty, overtakeDifficulty, length, direction):
        self.difficulty = float(difficulty)
        self.overtakeDifficulty = float(overtakeDifficulty)
        self.length = float(length)
        self.direction = str(direction)


class Straight:
    def __init__(self, length, brakingDifficulty, overtakeBrakingDifficulty):
        self.length = float(length)
        self.brakingDifficulty = float(brakingDifficulty)
        self.overtakeBrakingDifficulty = float(overtakeBrakingDifficulty)

    def __call__(self):
        return self



test = Track("Silverston", "UK", 0, corners=Track.create_corner(), straight=Track.create_straight())

print(test)