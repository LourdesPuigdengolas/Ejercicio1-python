import csv
from claseEmail import Email

class gestorEmail:
    __listaEmails = []
    def __init__(self, listaEmail):
        self.__listaEmails = listaEmail

  
    def abrirLista(self):
       print(f'--- Abriendo lista ---')
       archivo = open('listaEmails.csv')
       reader = csv.reader(archivo, delimiter=',')
       for email in reader:
         for n in email:
            print(f' email: {n} ')
            if "@" in n: 
               Email.crearCuenta(self, n)
               print(f'Cuenta creada exitosamente.') 
            else:
               print(f'El e-mail: {n} ,NO es válido.')   

       archivo.close()


   