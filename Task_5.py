# Activity 1: Superhero Class
class Superhero:
    # Class attribute
    universe = "Comic Book Universe"
    
    # Constructor to initialize objects with unique values
    def __init__(self, name, secret_identity, powers, weakness, energy_level=100):
        self.name = name
        self._secret_identity = secret_identity  # Encapsulated attribute
        self.powers = powers  # List of powers
        self.weakness = weakness
        self.energy_level = energy_level
    
    # Method to display superhero information
    def display_info(self):
        print(f"Superhero: {self.name}")
        print(f"Secret Identity: {self._reveal_identity()}")
        print(f"Powers: {', '.join(self.powers)}")
        print(f"Weakness: {self.weakness}")
        print(f"Energy Level: {self.energy_level}%")
        print(f"Universe: {self.universe}")
        print("-" * 40)
    
    # Encapsulated method to reveal identity
    def _reveal_identity(self):
        return self._secret_identity
    
    # Method to use a power
    def use_power(self, power_index):
        if self.energy_level <= 0:
            print(f"{self.name} is too exhausted to use powers!")
            return False
        
        if 0 <= power_index < len(self.powers):
            power = self.powers[power_index]
            print(f"{self.name} uses {power}!")
            self.energy_level -= 10
            return True
        else:
            print(f"{self.name} doesn't have that power!")
            return False
    
    # Method to rest and recover energy
    def rest(self):
        print(f"{self.name} is resting...")
        self.energy_level = min(100, self.energy_level + 30)
        print(f"Energy level is now {self.energy_level}%")
    
    # Method to handle weakness encounter
    def encounter_weakness(self):
        print(f"{self.name} encounters {self.weakness}! Power reduced!")
        self.energy_level = max(0, self.energy_level - 25)


# Activity 2: Polymorphism with Vehicles
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
        pass  # To be implemented by subclasses


class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving 🚗 at {self.speed} mph"


class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying ✈️ at {self.speed} mph"


class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing ⛵ at {self.speed} knots"


# Demonstration
if __name__ == "__main__":
    print("=" * 50)
    print("SUPERHERO DEMONSTRATION")
    print("=" * 50)
    
    # Create superhero instances
    superman = Superhero(
        "Superman", 
        "Clark Kent", 
        ["Flight", "Super Strength", "Heat Vision", "X-Ray Vision"], 
        "Kryptonite"
    )
    
    batman = Superhero(
        "Batman",
        "Bruce Wayne",
        ["Martial Arts", "Detective Skills", "Technology"],
        "No Superpowers",
        85
    )
    
    # Display superhero information
    superman.display_info()
    batman.display_info()
    
    # Demonstrate power usage
    superman.use_power(0)  # Flight
    superman.use_power(2)  # Heat Vision
    print(f"Superman's energy level: {superman.energy_level}%")
    
    # Demonstrate weakness encounter
    superman.encounter_weakness()
    print(f"Superman's energy level after weakness: {superman.energy_level}%")
    
    # Demonstrate resting
    superman.rest()
    
    print("\n" + "=" * 50)
    print("POLYMORPHISM DEMONSTRATION")
    print("=" * 50)
    
    # Create different vehicle objects
    vehicles = [
        Car("Sports Car", 120),
        Plane("Jumbo Jet", 550),
        Boat("Speedboat", 45)
    ]
    
    # Demonstrate polymorphism - each vehicle moves differently
    for vehicle in vehicles:
        print(vehicle.move())
