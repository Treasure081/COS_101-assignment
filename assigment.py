def a():
    # impulse = "force*time"
    force=int(input("what is the force applied?"))
    time=int(input("what is the time covered?"))
    print(force*time)

def b():
    # force = "mass * acceleration"
    mass=int(input("what is the mass ?"))
    acceleration=int(input("what is the acceleration ?"))
    print(mass*acceleration)

def c():
    # pressure = "force*area"
    force=int(input("what is the force applied?"))
    area=int(input("what is the area covered?"))
    print(force*area)

def d():
    # power= "work / time"
    work=int(input("what is the work ?"))
    time=int(input("what is the time covered?"))
    print(work*time)

def e():
    # velocity = "distance/time"
    distance =int(input("what is the distance covered "))
    time=int(input("what is the time ?"))
    print(distance/time)

def main():
    answer = input("what operation do you want to perform")

    if answer == "a":
        a()
    elif answer == "b":
        b()
    elif answer == "c":
        c()
    elif answer == "d":
        d()
    elif answer == "e":
        e()
    else:
        print("invalid input")
if __name__ == '__main__':
    main()