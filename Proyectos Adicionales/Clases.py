'''
Este pequeño programa es una muestra de como funcionan las clases segun lo que vimos en Programacion III
'''
def instructions():
    print("By using thios program you will be able to create dogs and make them bark")

def replay(): 
    redo=input("Would you like to create a new dog?(y/n) ")
    if redo.lower()=="y":
        return "y"
    else:
        return "n"

class Dog():
    #Se define un attributo de objeto (Object Attribute), todas las instancias tienen este atributo como determinado
    species="mammal"

    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    
    def bark(self):
        print(f"You just made {self.name} bark.")


if __name__ == "__main__":
    instructions()
    dogs=[]
    deseo=input("Do you want to create a Dog (y/n): ")
    while deseo.lower()=="y":
        name=input("Please give me the dog's a name: ")
        age=input("Please give me the dog's a age: ")
        breed=input("Please give me the dog's a breed: ")
        new_dog=Dog(name,age,breed)
        dogs.append(new_dog)
        print(f"Right now you have {len(dogs)} dogs.\nYour dogs are: ")
        for dog in dogs:
            print (dog.name)
        dog_name=input("Please give the name of the dog that you would like to bark: ")
        for dog in dogs:
            if dog_name==dog.name:
                dog.bark()
            else:
                print(f"{dog.name} will not bark")
        deseo=replay()
    print("\nCreated by Roger Urrutia. Thank you for using my program!")