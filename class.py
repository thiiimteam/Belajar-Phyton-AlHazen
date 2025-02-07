class Animal:
    name = ""
    color = ""
    voice = ""

    def __init__(self, animal_name, animal_color):
        self.name = animal_name
        self.color = animal_color
        print("Animal created")

    def makeSound(self, sound):
        print(f"{self.name} with color {self.color} making sound {sound}")


    def eat(self, food):
        print("It is eating", food)

cat = Animal("Lany", "Full Grey")
capybara = Animal("Capyy", "Brown")

print("-----")

print(type(cat))
print(type(capybara))

#cat.name = "Lyna"
#cat.color = "Full Grey"
#print(cat.color)
cat.makeSound("Meow")

#capybara.name = "Capyy"
#capybara.color = "Brown"
#print(capybara.name)
capybara.eat("Fish")

