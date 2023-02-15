import csv
import Team as tm
import Driver as dr


class RearTyres:
    def __init__(self, RearTyresPerformance, RearTyresTemp):
        self.RearTyresPerformance = float(RearTyresPerformance)
        self.RearTyresTemp = float(RearTyresTemp)

    def __call__(self):
        return self


class FrontTyres:
    def __init__(self, FrontTyresPerformance, FrontTyresTemp):
        self.FrontTyresPerformance = float(FrontTyresPerformance)
        self.FrontTyresTemp = float(FrontTyresTemp)

    def __call__(self):
        return self


class TyresPackage:
    def __init__(self, FrontTyres, RearTyres):
        self.FrontTyres = FrontTyres()
        self.RearTyres = RearTyres()

    def __call__(self):
        return self


class RearBreaks:
    def __init__(self, RearBrakePerformance, RearBrakeTemp):
        self.RearBrakePerformance = float(RearBrakePerformance)
        self.RearBrakeTemp = float(RearBrakeTemp)

    def __call__(self):
        return self


class FrontBreaks:
    def __init__(self, FrontBrakePerformance, FrontBrakeTemp):
        self.FrontBrakePerformance = float(FrontBrakePerformance)
        self.FrontBrakeTemp = float(FrontBrakeTemp)

    def __call__(self):
        return self


class BreakPackage:
    def __init__(self, FrontBrakes, RearBrakes):
        self.FrontBrakes = FrontBrakes()
        self.RearBrakes = RearBrakes()

    def __call__(self):
        return self


class Chassis:
    def __init__(self, Performance):
        self.Performance = float(Performance)

    def __call__(self):
        return self


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

    def __call__(self):
        return self


class Car:
    def __init__(self, Driver, Chassis, BrakesPackage, AeroPackage, TyresPackage, OverallPerformance, OverallDamage,
                 FuelLevel, Team):
        self.Driver = str(Driver)
        self.Chassis = Chassis()
        self.BrakesPackage = BrakesPackage()
        self.AeroPackage = AeroPackage()
        self.TyresPackage = TyresPackage()
        self.OverallPerformance = float(OverallPerformance)
        self.OverallDamage = float(OverallDamage)
        self.FuelLevel = float(FuelLevel)
        self.Team = str(Team)


def create_chassis():
    obj = Chassis(0.0)
    return obj


def create_front_wing():
    obj = FrontWing(0.0)
    return obj


def create_rear_wing():
    obj = RearWing(0.0)
    return obj


def create_body_aero():
    obj = BodyAero(0.0)
    return obj


def create_aero_package():
    obj = AeroPackage(create_front_wing(), create_rear_wing(), create_body_aero())
    return obj


def create_front_breaks():
    obj = FrontBreaks(0.0, 0.0)
    return obj


def create_rear_breaks():
    obj = RearBreaks(0.0, 0.0)
    return obj


def create_break_package():
    obj = BreakPackage(create_front_breaks(), create_rear_breaks())
    return obj


def create_rear_tyres():
    obj = RearTyres(0.0, 0.0)
    return obj


def create_front_tyres():
    obj = FrontTyres(0.0, 0.0)
    return obj


def create_tyres_package():
    obj = TyresPackage(create_front_tyres(), create_rear_tyres())
    return obj


def create_car():
    obj = Car("",
              create_chassis(),
              create_break_package(),
              create_aero_package(),
              create_tyres_package(),
              0.0,
              0.0,
              0.0,
              "")
    return obj


def create_car_list():
    car_list = []
    x = 20
    y = 0
    while x > y:
        car_list.append(create_car())
        x -= 1

    return car_list



