
while True:
    try:
        operation= int(input("What operation do you want to perform: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division \n "))
        if operation > 4:
            print("Invalid input, try again")
        else: 
            n = []
            for i in range(2):
                num =  int(input(f"Enter num{i+1}: "))
                n.append(num)
            if operation == 1:
                add = n[0] + n[1]
                print(add)
            elif operation == 2:
                sub = n[0] - n[1]
                print(sub)
            elif operation == 3:
                mult= n[0]*n[1]
                print(mult)
            elif operation == 4:
                div = n[0]/n[1]   
                print(div) 
    except ZeroDivisionError:
        print("Invalid input, try again..\nCheck if your second input is zero") 

    y =input("Do you want to continue?(y/n) ").lower()
    if y == "n":
        break
         
        