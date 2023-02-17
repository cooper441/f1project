import Team as tm
import Driver as dr
from Car import Car as cr
from Track import Track as tr

teamList = tm.create_list("Resources\Teams.csv")
driverList = dr.create_list("Resources\Drivers.csv")


def driver_to_team(l1, l2):
    for i in l1:
        for x in l2:
            if i.Team == x.Name:
                i.Team = x
                print(str(i.Abbrev) + " is now assigned to " + str(i.Team.Name))
                break


driver_to_team(driverList, teamList)


def create_car(driver):
    obj = cr(driver,
             cr.create_chassis(),
             cr.create_break_package(),
             cr.create_aero_package(),
             cr.create_tyres_package(),
             0.0,
             0.0,
             0.0,
             driver.Team)

    return obj


def driver_to_car(driverList):
    x = 0
    y = 20
    while x < y:
        create_car(driverList[x])
        print(driverList[x].Abbrev + " is now assigned a car")
        x += 1


driver_to_car(driverList)
