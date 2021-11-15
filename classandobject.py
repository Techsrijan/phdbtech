class Student:
    def display(self,name,age):
        self.name=name
        self.age=age
        print("name and age")
        print(name,age)


st=Student()   # object creation
#Student.display(st)  # what is self

st.display("ram",66)