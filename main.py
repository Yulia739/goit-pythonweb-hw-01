import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

from factories.us_factory import USVehicleFactory
from factories.eu_factory import EUVehicleFactory

us_factory = USVehicleFactory()
car_us = us_factory.create_car("Ford", "Mustang")
motorcycle_us = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

car_us.start_engine()
motorcycle_us.start_engine()

eu_factory = EUVehicleFactory()
car_eu = eu_factory.create_car("Volkswagen", "Golf")
motorcycle_eu = eu_factory.create_motorcycle("BMW", "R1250")

car_eu.start_engine()
motorcycle_eu.start_engine()
