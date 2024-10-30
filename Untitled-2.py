class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.happiness = 100

    def eat(self):
        self.energy += 20
        self.happiness += 10
        print(f"{self.name} is eating. Energy: {self.energy}, Happiness: {self.happiness}")

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.happiness += 15
            print(f"{self.name} is playing. Energy: {self.energy}, Happiness: {self.happiness}")
        else:
            print(f"{self.name} is too tired to play!")

    def sleep(self):
        self.energy += 30
        print(f"{self.name} is sleeping. Energy: {self.energy}")

    def get_status(self):
        print(f"{self.name} - Energy: {self.energy}, Happiness: {self.happiness}")

if __name__ == "__main__":
    my_cat = Cat("Whiskers")
    my_cat.get_status()
    my_cat.eat()
    my_cat.play()
    my_cat.sleep()
    my_cat.get_status()
