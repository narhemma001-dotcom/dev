
library ={
"Title":[],
"Author":[],
}
def add_book():
    while True: 
        try:
            title = input("Enter the title: ").strip().title()
            author = input("Name of author: ").strip().title()
            library["Author"].append(author)
            library["Title"].append(title)
            print("Successfully added..")
            x = input("Do you wanted to add another book(yes/no)? ").lower().strip()
            if x == "no":
                break 
        except ValueError:
            print("Invalid input..")       

def borrow_book():    
    while True: 
        try:       
            title = input("Enter the title: ").strip().title()
            author = input("Name of author: ").strip().title()
            if title not in library["Title"] or author not in library["Author"] :
                print("No such book available")
            else:    
                library["Author"].remove(author)
                library["Title"].remove(title)
                print("Successful..")
            x = input("Do you wanted to borrow/remove another book(yes/no)? ").lower().strip()
            if x == "no":
              break  
        except ValueError:
            print("Invalid input..")
             
while True:
    try:
        user = int(input("1.Add book\n2.Borrow book\n3.Return book\n4.Display available books\n")) 
        if user == 1:
            add_book()
        elif user == 2:
            borrow_book()      
        elif user == 3:
            add_book()
        elif user == 4:
            print(library)
        x = input("Do you wanted to continue (yes/no)? ").lower().strip()
        if x == "no":
            break
    except ValueError:
        print("Invalid Input..")    