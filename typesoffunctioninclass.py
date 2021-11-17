'''
1. instance method --self
2. static method
3. class mtehod
'''

class Student:
    school="Techsrijan"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def total_marks(self):
        return (self.m1+self.m2+self.m3)

    @staticmethod  #decorator
    def msg(m,n):
        print(m+n)
        print("this will run without any object")

    @classmethod
    def school_name(cls):
        return cls.school

Student.msg(67,68)
s1=Student(10,20,30)
print(s1.total_marks())

print(Student.school_name())