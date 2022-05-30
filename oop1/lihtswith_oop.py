#lightswith_oop.py
from http.client import SWITCHING_PROTOCOLS


class Lightswith():
    def __init__(self) -> None:
        self.switch_stasus = False

    def turnon(self):
        self.switch_stasus = True
   
    def turnoff(self):
        self.switch_stasus = False

    def show(self):
        print(f"status = {self.switch_stasus}")

#สร้างวัตถุ (Object) จากแม่พิมพ์ (clss)
switch_obj = Lightswith()

#เรียกใช้เมธอต/ฟังชัน
switch_obj.show()
switch_obj.turnon()
switch_obj.show() #True
switch_obj.turnoff()
switch_obj.show() #False
switch_obj.turnoff()
switch_obj.show()

