from claseEmail import Email   
from gestorEmails import gestorEmail
  

if __name__=='__main__':
   print('Ingresar los sigueintes datos:')
   id=input(" ingrese id cuenta: ")
   dominio = input(" ingrese dominio: ")
   tipodom= input(" ingrese el tipo de dominio: ")
   contrasenia= input(" ingrese la contrasenia: ")
   unemail = Email(id,dominio,tipodom,contrasenia)
   unemail.getdominio()
   unemail.retornaEmail()

   correo = input('--Ingrese el email con el que desea crear una cuenta: ')
   mail = Email(0,0,0,0)
   mail.crearCuenta(correo)
   mail.retornaEmail()
   
   nombre =  input ('Ingrese nombre: ')
   #maili =  input ('Ingrese e-mail: ') no hace falta
   print(f'Estimado/a {nombre} te enviamos tus mensajes a la direccion {correo}')
   contra = input("Para modificar su contarseña ingrese la contrasenia actual: ")
   unemail.modifContrasenia(contra)
   unemail.crearObjeto()
   ungestor = gestorEmail('listaEmail')
   ungestor.abrirLista()



   
