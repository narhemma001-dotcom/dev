class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if name not in ["kofi","emma"]  :
            raise ValueError("Invalid name")
        self._name = name
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    
    house = input("House: ")
    return Student(name,house)    



if __name__ == "__main__":
    main()
