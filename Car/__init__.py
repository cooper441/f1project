import csv
import Team as tm
import Driver as dr


class RearTyres:
    def __init__(self, RearTyresPerformance, RearTyresTemp):
        self.RearTyresPerformance = float(RearTyresPerformance)
        self.RearTyresTemp = float(RearTyresTemp)


class FrontTyres:
    def __init__(self, FrontTyresPerformance, FrontTyresTemp):
        self.FrontTyresPerformance = float(FrontTyresPerformance)
        self.FrontTyresTemp = float(FrontTyresTemp)


class TyresPackage:
    def __init__(self, FrontTyres, RearTyres):
        self.FrontTyres = FrontTyres(FrontTyres)
        self.RearTyres = RearTyres(RearTyres)


class RearBreaks:
    def __init__(self, RearBrakePerformance, RearBrakeTemp):
        self.RearBrakePerformance = float(RearBrakePerformance)
        self.RearBrakeTemp = float(RearBrakeTemp)


class FrontBreaks:
    def __init__(self, FrontBrakePerformance, FrontBrakeTemp):
        self.FrontBrakePerformance = float(FrontBrakePerformance)
        self.FrontBrakeTemp = float(FrontBrakeTemp)


class BreakPackage:
    def __init__(self, FrontBrakes, RearBrakes):
        self.FrontBrakes = FrontBrakes(FrontBrakes)
        self.RearBrakes = RearBrakes(RearBrakes)


class Chassis:
    def __init__(self, Performance):
        self.Performance = float(Performance)


class BodyAero:
    def __init__(self, Performance):
        self.Performance = float(Performance)

    def __call__(self):
        return self


class RearWing:
    def __init__(self, Performance):
        self.Performance = float(Performance)

    def __call__(self):
        return self


class FrontWing:
    def __init__(self, Performance):
        self.Performance = float(Performance)

    def __call__(self):
        return self


class AeroPackage:
    def __init__(self, FrontWing, RearWing, BodyAero):
        self.FrontWing = FrontWing()
        self.RearWing = RearWing()
        self.BodyAero = BodyAero()


class Car:
    def __init__(self, Driver, Chassis, BrakesPackage, AeroPackage, TyresPackage, OverallPerformance, OverallDamage,
                 FuelLevel, Team):
        self.Driver = str(Driver)
        self.Chassis = str(Chassis)
        self.BrakesPackage = str(BrakesPackage)
        self.AeroPackage = str(AeroPackage)
        self.TyresPackage = str(TyresPackage)
        self.OverallPerformance = float(OverallPerformance)
        self.OverallDamage = float(OverallDamage)
        self.FuelLevel = float(FuelLevel)
        self.Team = str(Team)


# def create_list(file):
#     carList = []
#     with open(file, 'r') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             carList.append(Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
#
#         return carList

def create_chassis():
    chassisList = []
    x = 10
    y = 0
    while y < x:
        chassisList.append(Chassis(0))
        x -= 1
    return chassisList


def create_front_wing():
    frontWingList = []
    x = 10
    y = 0
    while y < x:
        frontWingList.append(FrontWing(0))
        x -= 1
    return frontWingList


def create_rear_wing():
    rearWingList = []
    x = 10
    y = 0
    while y < x:
        rearWingList.append(RearWing(0))
        x -= 1
    return rearWingList


def create_body_aero():
    bodyAeroList = []
    x = 10
    y = 0
    while y < x:
        bodyAeroList.append(BodyAero(0))
        x -= 1
    return bodyAeroList


def create_aero_package():
    aeroPackageList = []
    x = 10
    y = 0
    while y < x:
        aeroPackageList.append(AeroPackage(create_front_wing()[0], create_rear_wing()[0], create_body_aero()[0]))
        x -= 1

    return aeroPackageList


# print(callable(create_front_wing()[0]))
# print(create_front_wing()[0])
print(len(create_aero_package()))
