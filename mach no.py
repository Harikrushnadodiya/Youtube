k=float(input("Spcific heat ratio:"))
#Real gas constant
R=0.287 #KJ/Kg*K
T=float(input("Temperature K:"))
V= float(input("velocity m/s2:"))

#find mach no


C=(k*R*1000*T)**(1/2)

Ma=V/C

print("the mach no is:", Ma)
