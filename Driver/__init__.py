import csv


class Driver:
    def __init__(self, FirstName, LastName, Abbrev, Nat, Team, Rating, Experience, Racecraft, Awareness, Pace):
        self.FirstName = str(FirstName)
        self.LastName = str(LastName)
        self.Abbrev = str(Abbrev)
        self.Nat = str(Nat)
        self.Team = str(Team)
        self.Rating = float(Rating)
        self.Experience = float(Experience)
        self.Racecraft = float(Racecraft)
        self.Awareness = float(Awareness)
        self.Pace = float(Pace)

    def __call__(self):
        return self


def create_list(file):
    driverList = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            driverList.append(Driver(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        for i in driverList:
            i.Team = i.Team.strip()

        return driverList

