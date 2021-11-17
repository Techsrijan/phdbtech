class Room:    #parent
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)

class GusetRoom(Room):  #child
    def msg(self):
        print("GuestRoom")

class Test(GusetRoom):
    def msg3(self):
        print("multi level inheritance")

#r=Room()
#r.area(4,5)
'''
g=GusetRoom()
g.msg()
g.area(55,66)

'''

t=Test()
t.msg()
t.area(5,4)
t.msg3()