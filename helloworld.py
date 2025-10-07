r= []

for i  in range(3) :
    while True:  
      resist = float(input(f"Enter the resistance R{i+1}: "))
      r.append(resist)
      if resist <= 0:
         print("Invalid input, Try again..")
      break

Ra = r[1]+r[2]+(r[1]*r[2])/r[0]
Rb = r[0]+ r[2]+(r[0]*r[2])/r[1]
Rc= r[0]+ r[1]+(r[0]*r[1])/r[2]

print(f"You new R1, R2 and R3 are {Ra:.2f},{Rb:.2f} and {Rc:.2f}")
sum = Ra + Rb + Rc
import math
square = math.sqrt(sum)
print(f"The square root is {square: .2f}")