class A:
    def __init__(self):
        print("this is class A Constructor")



class B(A):

    def __init__(self):
        super().__init__()
        print("this is class B Constructor")


class C(B):

    def __init__(self):
        super().__init__()
        print("this is class C Constructor")

c=C()
