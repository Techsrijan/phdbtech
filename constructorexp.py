class Computer:
    def company(self):
        print("Lenevo")

    #constructor is a special member fuction
    # which will be invoked automatically
    #when the object is created
    def __init__(self):
        print("This will run when the object is created")

c=Computer()
c.company()

d=Computer()