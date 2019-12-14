import math 
P=float(input("Inside pressure psig:"))
SE=float(input("Allowable limit psi:"))
D=float(input("Inside Diameter in:"))
Ca=float(input("Corrosion Allowance in:"))


#corrosion allowance
Di=D+2*Ca
R=Di/2

#AS per DIV-1

#Circumferential stress thickness
tc=(P*R)/(SE-0.6*P)

#Longitudinal stress
tt=(P*R)/(2*SE+0.4*P)

#MAXIMUM OF TC AND TT
t=max(tc,tt)
t1=t+Ca

#As per DIV-2

t0=R*((math.exp(P/SE))-1)
t2=t0+Ca


#print function

print("As per ASME div-1 thk is :", t1*25.4,"mm")
print("As per ASME div-2 thk is :", t2*25.4,"mm")
print("Min thickness required :", (min(t1,t2))*25.4,"mm")
print("difference between ASME div-1 and div-2",t1*25.4-t2*25.4,"mm")


