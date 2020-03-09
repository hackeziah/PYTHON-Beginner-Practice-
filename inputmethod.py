from sys import argv

script,P,Y,R = argv
# print("Script Name: ",script) 
# print("Script Name: ",P) 
# print("Script Name: ",Y) 
# print("Script Name: ",R) 

P = float(P)
Y = float(Y)
R = float(R)
n = 12*Y
r =R/(12*100)  

Payment = P*r/(1-(1+r)**-n) 

print(Payment)

#y = int(input("ENTER A NUMBER1 :"))
#x = int(input("ENTER A NUMBER2 :"))
#c  = y+x
#int(c)
#print("The total is:"+c)