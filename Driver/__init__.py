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

# def create_driver_df(csv):
#     # Creates column names for driver DF
#     columnNames = ["FirstName", "LastName", "Abbrev", "Nat", "Team", "Rating", "Experience", "Racecraft", "Awareness",
#                    "Pace"]
#     # Imports csv data with the correct column names
#     drivers = pd.read_csv(csv, names=columnNames)
#
#     # Strips whitespace from every data entry
#     for i in drivers.columns:
#         # checking datatype of each column
#         if drivers[i].dtype == 'object':
#             # applying strip function on column
#             drivers[i] = drivers[i].map(str.strip)
#         else:
#             # if condn. is False then it will do nothing.
#             pass
#     # Sorts correct data types to columns
#     drivers = drivers.astype(
#         {"FirstName": "category", "LastName": "category", "Abbrev": "category", "Nat": "category", "Team": "object"})
#
#     return drivers
#
#
# def showAllDrivers(list):
#     for x in list:
#         print(x.FirstName + " " + x.LastName + " " + x.Abbrev + " " + x.Nat + " " + x.Team + " " + str(x.Rating)
#               + " " + str(x.Experience) + " " + str(x.Racecraft) + " " + str(x.Awareness) + " " + str(x.Pace))
