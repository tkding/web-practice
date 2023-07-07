class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats:
            return False
        
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
            
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]

for pep in people:
    success = flight.add_passenger(pep)
    
    if success:
        print(f"Added {pep} successfully")
    
    else:
        print(f"No available seat for {pep}.")