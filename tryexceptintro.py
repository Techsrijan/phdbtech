try:
    print("freez is open ")
    a = int(input("Enter the value of a "))
    b = int(input("Enetr the value of b"))
    d=a/b
    print("div=",d)

except ValueError:
    print("you have entered character")

except ZeroDivisionError:
    print(" b cant be zero")

except Exception:
    print("something went wrong")

finally:
    print("freez is closed")