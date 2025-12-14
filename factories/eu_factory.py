from .vehicle_factory import VehicleFactory
from vehicles.car import Car
from vehicles.motorcycle import Motorcycle


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (EU Spec)", model)
