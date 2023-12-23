opcion1="Continuar"
opcion2="salir"
si="si"
no="no"
contra1= "AkouYtG2023@@"
contra2="koIun&00"
contra3="85Ooppñ-q"
contra4="d@8iU7uWyt"
contra5="6cdj4NUg$jj"
contra6="ppKtBuu76@@"
caracter1= "@<"
caracter2="9689"
caracter3="#rt"
caracter4="eRt"
caracter5="pKn"
caracter6="3+Q"
caracter7="pBv"
caracter8="345"
caracter9="PyHII"
facil= "1"
dificil= "2"

print("""              
    GENERADOR DE CONTRASEÑA SEGURO
    ¡Bienvenido al Generador de Contraseñas Seguras! 
    Aquí, la seguridad es nuestra prioridad. Crea contraseñas robustas y protege tus datos con confianza. 
    ¡Comencemos a fortalecer tu seguridad en línea juntos!
    """)
print("Ingresa tu nombre: ")
nombre = input()
print("Número al azar del 1 al 10: ")
número = int(input())
print("Color favorito: ")
color = input()
print("""       
    Para continuar con el juego necesito saber si deseas CONTINUAR o SALIR     
    """)
decision = input()

while decision.lower() != opcion1.lower() and decision.lower() != opcion2.lower():
    print("Datos incorrectos, ingresa de nuevo por favor")
    decision = input()

if decision.lower() == opcion1.lower():
    print("¿Deseas generar una contraseña aleatoria? (SI o NO): ")
    siono = input().lower()

    while siono != si and siono != no:
        print("Datos ingresados incorrectamente, por favor intenta de nuevo: ")
        siono = input().lower()

    if siono == si:
        print("Ingrese la longitud deseada para la contraseña: ")
        longitud = int(input())

        while longitud <= 0:
            print("Por favor, ingrese una longitud válida mayor que cero: ")
            longitud = int(input())

        caracteres = [caracter1, caracter2, caracter3, caracter4, caracter5, caracter6, caracter7, caracter8, caracter9]

        import random
        nueva_contra = ''.join(random.choice(''.join(caracteres)) for _ in range(longitud))

        print(f"Tu nueva contraseña es: {nueva_contra}")
        print("¡Gracias por jugar! 😊")

    if siono.lower()==no.lower():
        print("Haz seleccionado 'No', deseas una contraseña fácil(1) o díficil(2): ")
        dificultad=int(input())

        while dificultad != 1 and dificultad != 2:
            print("datos incorrectos, ingrese de nuevo por favor")
            dificultad=int(input())
        if dificultad==1 and número<=3:
            def contraseñag1(c4,c1):
                 suma=c4+nombre+c1
                 return suma
            contra=contraseñag1("eRt","@<")
            print("Su contraseña es: ", contra,", gracias por jugar 😉")
        if dificultad==1 and 3<número<6:
           def contraseñag1(c5,c6):
                 suma=c5+nombre+c6
                 return suma
           contra=contraseñag1("pKn","3+Q")
           print("Su contraseña es: ", contra,", gracias por jugar 😉")
        if dificultad==1 and número>=6:
          def contraseñag1(c3,c7):
                 suma=c3+nombre+c7
                 return suma
          contra=contraseñag1("#rt","pBv")
          print("Su contraseña es: ", contra,", gracias por jugar 😉")
        if dificultad==2 and número<=3:
            def contraseñag1(c3,c8,c9):
                 suma=c3+nombre+c8+color+c9
                 return suma
            contra=contraseñag1("/%","wEr","Ase")
            print("Su contraseña es: ", contra,", gracias por jugar 😉")
        if dificultad==2 and 3<número<6:
           def contraseñag1(c5,c4,c6):
                 suma=c5+nombre+c4+color+c6
                 return suma
           contra=contraseñag1("pK/","eRt","3+Q")
           print("Su contraseña es: ", contra,", gracias por jugar 😉")
        if dificultad==2 and número>=6:
            def contraseñag1(c1,c8,c9):
                 suma=c1+nombre+c9+color+c8
                 return suma
            contra=contraseñag1("@<","wEr","Ase")
            print("Su contraseña es: ", contra, "gracias por jugar 😉")

if decision.lower()==opcion2.lower():
    print("Gracias, vuelve pronto 😎")    

