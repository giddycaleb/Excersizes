staff_list = []


class Staff:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        staff_list.append(self)

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and my id is {self.id}")

class Management(Staff):
    def __init__(self,name,age,id,car):
        super().__init__(name,age,id)
        self.car = car

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and my id is {self.id} and i have a {self.car}")

class Clerical(Staff):
    def __init__(self,name,age,id,type_speed):
        super().__init__(self,name,age,id)
        self.type_speed = type_speed



s1 = Staff("Jim", 20, 42)
s2 = Staff("bill",19, 43)
m1 = Management("Jeff",21,44,"Suzuki")


for staff in staff_list:
    staff.show()
