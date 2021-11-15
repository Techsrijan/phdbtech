''''
variable
  1. instance varable
  2. class variable(static variable)

namespace--- is an area where you can create and store object/variable
1. class namespace
2. object/instance namespace
'''
class Car:
    company_name="Maruti" #class variable
    def __init__(self):
        self.mil=10 #instance varable
        self.speed=100
        #print(self.mil)



#c1=Car()
maruti=Car()
print("mil=",maruti.mil,"speed=",maruti.speed,Car.company_name)

Car.company_name="CarBanao"
wagnor=Car()
wagnor.mil=33
wagnor.speed=125
print("mil=",wagnor.mil,"speed=",wagnor.speed,wagnor.company_name)

#alto.company_name="fgfg"
alto=Car()
alto.mil=44
alto.speed=50
print("mil=",alto.mil,"speed=",alto.speed,alto.company_name)