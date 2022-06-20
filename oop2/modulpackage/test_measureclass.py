from ast import Num
from xml.dom import InvalidCharacterErr
from measure import Measure

"""if _name__=='__main_':
    m1 = Measure(56)
    m2 = Measure(78)
    m3 = Measure(14)
    m4 = Measure(250)
    
    print(m1.inch_cm())
    print(m2.inch_cm())
    print(m3.cm_inch())
    print(m4.cm_inch())"""

    
    
"""inch_list = [52,18,20,40]
for item in inch_list:
    m = Measure(item)
    print(m.inch_cm())"""

num = float(input("Enter number: "))
ch = input("Choose I (inch->cm), C(cm->inch):").upper()
if ch == 'I':
    m = Measure(num)
    print(m.inch_cm())
elif ch == 'C':
    m = Measure(num)
    print(m.cm_inch())
else:
    print("Wrong Character")
