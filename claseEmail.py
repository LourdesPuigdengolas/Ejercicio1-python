
class Email:
    __idcuenta = " "
    __dominio = " "
    __tipodom = " "
    __contrasenia = " "
    def __init__(self, idcuenta, dominio, tipodom, contrasenia): #)constructor
     self.__idcuenta = idcuenta
     self.__dominio = dominio
     self.__tipodom= tipodom
     self.__contrasenia= contrasenia
    def retornaEmail(self):
        return print(f" email ingresado: {self.__idcuenta}@{self.__dominio}.{self.__tipodom}")
    def getdominio(self):
       #return print(f"dominio ingresado: {self.__dominio}")
        return ({self.__dominio})
    def crearCuenta(self, correo):
       parte1 = correo.split('@')
       parte2 = parte1[1].split('.')
       self.__idcuenta = parte1[0]
       self.__dominio = parte2[0]
       self.__tipodom = parte2[1]
    def modifContrasenia(self, contra):
       if self.__contrasenia == contra:
          self.__contrasenia = input('Ingrese nueva contrasenia: ')
          return print(f"La nueva contrasenia es: {self.__contrasenia}")
         
    def crearObjeto(self):
       e1 = Email('informatica.fcefn@' ,'gmail', 'com', 'po')
       print(f'El objeto mail creado es: {e1.__idcuenta}{e1.__dominio}.{e1.__tipodom}')

    
            

