class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # def display(self):
    #     print(self.name)
    #     print(self.id)

    # salary=89
    # name="Rohan"
    def getSal(self):
        # return self.salary
        print(self.salary)

  
    
    
    
rohan=employee("Rohan","123")
# print(rohan.salary)
# print(rohan.name)

amulya=employee("Amulya","12355442")
# print(amulya.salary)
# print(amulya.name)
amulya.getSal()