#vehicle_abstract.py
#ต้อง import แบบนี้เสมอสำหรับ abstract class
from abc import ABC, abstract, abstractmethod
from io import BufferedRandom
from turtle import speed,brand

class Vehicle(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.brand = brand
        self.speed = speed
        self.gear = 0
        self.seat = 0

        @abstractmethod
        def show_detil(self):
            pass