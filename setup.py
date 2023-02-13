import Team as tm
import Driver as dr
import Car as cr

teamList = tm.create_list("Resources\Teams.csv")
driverList = dr.create_list("Resources\Drivers.csv")
carList = cr.create_list("Resources\Car.csv")


# def driver_to_team(l1, l2):
#     for i in l1:
#         for x in l2:
#             if i.Team == x.Name:
#                 i.Team = x
#                 print(str(i.Abbrev) + " is now assigned to " + str(i.Team.Name))
#                 break
#
#
# driver_to_team(driverList, teamList)

