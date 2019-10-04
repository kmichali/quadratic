import math
print(" Solve quadratic equation: ax**2 + bx + c = 0")

a = float(input(" enter a: "))
b = float(input(" enter b: "))
c = float(input(" enter c: "))

if (a == 0):
    print("not a quadratic equation")
    exit()

## compute discriminant
d = b*b - 4*a*c

if d < 0:
    print("no real solutions")
    exit()

if d > 0 :
    rd = math.sqrt(d)
    x1 = (-b + rd)/(2*a)
     x2 = (-b - rd)/(2*a)
    print("two solutions :" , x1, x2) 
elif d == 0:
    x = -b/(2*a)
    print( "one solution :" , x) 
else:
    print("something is wrong, we shoudn't  be here!")
