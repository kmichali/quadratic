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

def two_soln(aa,bb,dd):
    rr = math.sqrt(dd)
    x1 = (-bb + rr)/(2*aa)
    x2 = (-bb - rr)/(2*aa)
    return (x1,x2)

def one_soln(aa,bb):
    x = -bb/(2*aa)
    return x

if d > 0 :
    print("two solutions :" , two_soln(a,b,d)) 
elif d == 0:
    print( "one solution :" , one_soln(a,b)) 
else:
    print("something is wrong, we shoudn't  be here!")
