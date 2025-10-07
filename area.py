while True:
    try:
        n=[]
        for i in range(2):
            num = float(input(f"Enter length {i+1}: "))
            n.append(num)
        area = n[0]* n[1]
        perimeter = 2 *(n[0]+n[1])   

        print(f"Area is {area: .2f} \nPerimeter is {perimeter: .2f}") 
    except ValueError:
        print("Invalid input. Please input a number")
    x = input("Do you want to continue(y/n): ").lower()    
    if x == "n":
        break

