print("Welcome to the physics formular generator")

print("Formular A: v = d / t")

print('Formular B: v = u + at')

print("Formular C: f = ma")

print("Formular D: v = u + gt")

print("Formular E: r = u * T")

choice = input("Choose a formular by selecting A, B, C, D or E\n")
if choice == "A":
    print("Formular Selected: v = d / t")#
    d = float(input("What is the value of d? "))
    t = float(input("What is the value of t? "))
    v = d / t
    print(f"Your Velocity is {v} m/s ")

elif choice == "B":
    print("Formular Selected: v = u + at")
    u = float(input("What is the value of u? "))
    a = float(input("What is the value of a? "))
    t = float(input("What is the value of t? "))
    v = u + a * t
    print(f"Your Velocity is {v} m/s ")

elif choice == "C":
    print("Formular Selected: f = ma")
    m = float(input("What is the value of m? "))
    a = float(input("What is the value of a? "))
    f = m * a
    print(f"Your Force is {f} kg/m^2 ")

elif choice == "D":
    print("Formular Selected: v = u + gt")
    u = float(input("What is the value of u? "))
    g = float(input("What is the value of g? "))
    t = float(input("What is the value of t? "))
    v = u + g * t
    print(f"Your Velocity is {v} m/s ")

elif choice == "E":
    print("Formular Selected: r = U * T")
    T = float(input("What is the value of T? "))
    U = float(input("What is the value of U? "))
    r = U * T
    print(f"Your Range is {r} m ")

else:
    print("Invalid Choice")


