a = 4
b = 6
c = 8
discriminant = b*b - 4.0*a*c
if discriminant < 0 :
    print("no real roots")
else:
    d = math.sqrt(discriminant)
    print(((-b+d)/2.0))
    print(((-b-b)/2.0))