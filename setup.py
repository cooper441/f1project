import Team as tm
import Driver as dr
import Car as cr
import Track as tr


class ColouredText:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'


teamList = tm.create_list("Resources\Teams.csv")
driverList = dr.create_list("Resources\Drivers.csv")
carList = []
trackList = []


def driver_to_team(l1, l2):
    for i in l1:
        for x in l2:
            if i.Team == x.Name:
                i.Team = x
                print(str(i.Abbrev) + " is now assigned to " + str(i.Team.Name))
                break

    print(ColouredText.GREEN + "All default Drivers are now assigned to a Team" + ColouredText.RESET)



driver_to_team(driverList, teamList)


# Default car settings
def create_car(driver):
    obj = cr.Car(driver,
                 cr.Car.create_chassis(),
                 cr.Car.create_break_package(),
                 cr.Car.create_aero_package(),
                 cr.Car.create_tyres_package(),
                 0.0,
                 0.0,
                 0.0,
                 driver.Team)

    return obj


# Assigns each drive to a car
def driver_to_car(driverList):
    x = 0
    y = 20  # amount of cars
    while x < y:
        carList.append(create_car(driverList[x]))
        print(driverList[x].Abbrev + " is now assigned a car")
        x += 1
    print(ColouredText.GREEN + "All Cars have been created" + ColouredText.RESET)
    print(ColouredText.GREEN + "All Drivers have been assigned a car" + ColouredText.RESET)


driver_to_car(driverList)
test = tr.create_track("Resources\Silverstone.csv", "Silverstone")
trackList.append(test)


print(ColouredText.GREEN + "Track has been created" + ColouredText.RESET)
print(ColouredText.GREEN + "Setup complete" + ColouredText.RESET)

