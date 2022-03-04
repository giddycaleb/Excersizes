
class Bus:
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        bus_list.append(self)


bus_list=[]




b1 = Bus(2010, "Y", "Bob")
b2 = Bus(2011, "B", "Greg")
b3 = Bus(2011, 100, "Mohammed")

for bus in bus_list:
    print(f"Bus number is {bus.number} Route is {bus.route} and driver is {bus.driver}")
