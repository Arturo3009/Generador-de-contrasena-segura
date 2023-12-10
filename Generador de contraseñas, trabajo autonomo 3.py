opcion1="Jugar"
opcion2="salir"
si="si"
no="no"
contra1= "AkouYtG2023@@"
contra2="koIun&00"
contra3="85Ooppñ-q"
caracter1= "@<"
caracter2="9689"
caracter3="/%"
caracter4="eRt"
facil= "1"
dificil= "2"
print("""             Bienvenido a mi primer proyecto 
           GENERADOR DE CONTRASEÑA SEGURO
            
            JUGAR       o        SALIR""")
decision=input("Ingrese la opción: ")
while decision.lower() != opcion2.lower(): 
    if (decision.lower() == opcion1.lower()):
        print("Hola, ingresa tu nombre:")
        datosnombre=input()
        print("Ahora tu color favorito: ")
        colorfav=input()
        print("tu año de nacimiento: ")
        añoc=input()
        siono=input("Deseas generar una contraseña aleatoria, si o no?: ")
        if (siono.lower() == si.lower()):
            aleatoria=int(input("Escoja un número al azar del 1 al 10: "))
            if(aleatoria <5 ):
                print("Su contraseña es: ", contra1)
                print("Gracias por jugar")
            if(aleatoria==5):
                print("Su contraseña es: ", contra2)
                print("Gracias por jugar")
            if(aleatoria >5):
                print("Su contraseña es: ", contra3)
                print("gracias por jugar")
                break 
        if(siono.lower() == no.lower()):
            dificultad=(input("Haz seleccionado no, entonces si deseas una contraseña fácil(1) o dificil(2)?: "))
            if(dificultad.lower() == facil.lower()):
                print("Listo he generado tu nueva contraseña: ", (añoc+datosnombre+caracter1))
                print("Gracias por jugar")
                break
            elif(dificultad.lower()==dificil.lower()):
                print("Listo he generado tu nueva contraseña: ", (caracter2+datosnombre+caracter3+colorfav+caracter4))
                print("Gracias por jugar")
                break
        break    
if (decision.lower() == opcion2.lower()):
    print("gracias, vuelva pronto")
 
    




       
