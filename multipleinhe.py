class Theory:
    def thoery_marks(self):
        print("this this theory marks")

class Sessional:
    def sessional_marks(self):
        print("this this sessional marks")

class Result(Theory,Sessional):
    def result_marks(self):
        print("This is result")

r=Result()
r.thoery_marks()
r.sessional_marks()
r.result_marks()