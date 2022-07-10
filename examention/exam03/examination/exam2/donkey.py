#from animalsubclass import horse, mule, donke
from winreg import DisableReflectionKey
from  import *

horseobj = horse("khan khan",4)
muleobj = mule("mumu",3)
mule2ojb = mule2("meme",1)
donkeobj = donke("phil",5)

"""dogobj.info()
horseobj.make_sound
muleobj.info()
muleo2bj.make_sound
donkeyobj.info()
muleobj.make_sound"""

for animal in (horse,mule,muleobj):
    print('***********')
    animal.info()
    animal.make_sound()