class Donante():

    """
    Es la clase utilizada para definir a los donantes 



    Parameters:

        name(str): Nombre del donante

        age(num): Edad del donante

        b_type(str): Tipo de sangre del donante

        sex(str): Sexo del paciente (no en cantidad, sino su genero, Masculino o Femenino)

    """

    def __init__(self,name,apellido,age,b_type,sex):
        self.name=name
        self.apellido=apellido
        self.age=age
        self.b_type=b_type
        self.sex=sex


class Donatario(Donante):
    """
        
    Define a un donatario de sangre en la base de datos

    """

    def __init__(self,name,apellido,age,b_type,sex):
        super().__init__(name,apellido,age,b_type,sex)

    def posible(self):
        if self.b_type=="A+":
            sangre_permitida=["A+","A-","O+","O-"]
        elif self.b_type=="O+":
            sangre_permitida=["O+","O-"]
        elif self.b_type=="B+":
            sangre_permitida=["B+","B-","O+","O-"]
        elif self.b_type=="AB+":
            sangre_permitida=["A+","A-","B+","B-","O+","O-","AB+","AB-"]
        elif self.b_type=="A-":
            sangre_permitida=["A-","O-"]
        elif self.b_type=="O-":
            sangre_permitida=["O-"]
        elif self.b_type=="B-":
            sangre_permitida=["B-","O-"]
        elif self.b_type=="AB-":
            sangre_permitida=["A-","B-","O-","AB-"]
        else:
            return f"La Sangre {self.b_type} no existe."
        return sangre_permitida