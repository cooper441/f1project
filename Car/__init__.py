import csv
import Team as tm
import Driver as dr


class Car:
    def __init__(self, Driver, Chassis, BrakesPackage, AeroPackage, TyresPackage, OverallPerformance, OverallDamage,
                 FuelLevel, Team):
        self.Driver = Driver()
        self.Chassis = Chassis()
        self.BrakesPackage = BrakesPackage()
        self.AeroPackage = AeroPackage()
        self.TyresPackage = TyresPackage()
        self.OverallPerformance = float(OverallPerformance)
        self.OverallDamage = float(OverallDamage)
        self.FuelLevel = float(FuelLevel)
        self.Team = Team()

    def __call__(self):
        return self
    @classmethod
    def create_chassis(self):
        obj = Chassis(0.0)
        return obj
    @classmethod
    def create_front_wing(self):
        obj = FrontWing(0.0)
        return obj
    @classmethod
    def create_rear_wing(self):
        obj = RearWing(0.0)
        return obj

    @classmethod
    def create_body_aero(self):
        obj = BodyAero(0.0)
        return obj

    @classmethod
    def create_aero_package(self):
        obj = AeroPackage(self.create_front_wing(), self.create_rear_wing(), self.create_body_aero())
        return obj

    @classmethod
    def create_front_breaks(self):
        obj = FrontBreaks(0.0, 0.0)
        return obj

    @classmethod
    def create_rear_breaks(self):
        obj = RearBreaks(0.0, 0.0)
        return obj

    @classmethod
    def create_break_package(self):
        obj = BreakPackage(self.create_front_breaks(), self.create_rear_breaks())
        return obj

    @classmethod
    def create_rear_tyres(self):
        obj = RearTyres(0.0, 0.0)
        return obj

    @classmethod
    def create_front_tyres(self):
        obj = FrontTyres(0.0, 0.0)
        return obj

    @classmethod
    def create_tyres_package(self):
        obj = TyresPackage(self.create_front_tyres(), self.create_rear_tyres())
        return obj


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
