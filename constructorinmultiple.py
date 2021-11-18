class Theory:
    def __init__(self):
        print("this this theory marks")

class Sessional:
    def __init__(self):
        print("this this sessional marks")

class Result(Sessional,Theory):
    def __init__(self):
        super().__init__()
        print("This is result")

r=Result()