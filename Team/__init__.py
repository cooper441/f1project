import csv


class Team:
    def __init__(self, Name, Nat, PerformanceImpact):
        self.Name = str(Name)
        self.Nat = str(Nat)
        self.PerformanceImpact = float(PerformanceImpact)





def create_list(file):
    teamList = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            teamList.append(Team(row[0], row[1], row[2]))

        for i in teamList:
            i.Name = i.Name.strip()
            i.Nat = i.Nat.strip()


        return teamList

