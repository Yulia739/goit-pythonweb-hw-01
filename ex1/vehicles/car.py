from typing import Any
from .vehicle import Vehicle
import logging

logger = logging.getLogger(__name__)


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")
