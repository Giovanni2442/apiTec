class Ussers:
    def __init__(self,name,lstnF,lstnM,age,email,city):
        self.name = name
        self.lstnF = lstnF
        self.lstnM = lstnM
        self.age = age
        self.email = email
        self.city = city

    def collectionUssers(self):
        return {
            'name': self.name,
            'lstnF': self.lstnF,
            'lastnM': self.lstnM,
            'age': self.age,
            'email': self.email,
            'city': self.city
        }
    
class Prueba:
    #Contructor de la clase
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #Retona los valores en fomato de dicciónario
    def collectionPrueba(self):
        return {
            'name' : self.name,
            'age' : self.age
        }
        