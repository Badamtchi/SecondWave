import string
import random

class VehicleRegistry:
    def generate_vehicle_id(self, length):
        return ''.join(random.choice(string.ascii_uppercase, k=length))
    
    def generate_vehicle_licence(self, id):
        return f"{id[:2]}-{''.join(random.choice(string.digits, k=2))}-{''.join(random.choice(string.ascii_uppercase, k=2))}"


