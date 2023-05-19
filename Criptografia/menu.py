from proceso import Proceso
import helper 

def main():
    while True:

        helper.limpiar_pantalla()

        print('---------------------------')
        print('M E N Ú   P R I N C I P A L')
        print('---------------------------') 

        print('[1] Encriptar mensaje.')
        print('[2] Desencriptar mensaje.')
        print('[3] Salir.')
        print('---------------------------') 

        p = Proceso()

        opcion = input('>> ')
        helper.limpiar_pantalla()

        if opcion == '1':
            resultado = p.encriptar()
            print('El mensaje encriptado es\n\n', resultado)

        elif opcion == '2':
            resultado = p.desencriptar()    
            print('El mensaje desencriptado es\n\n', resultado)

        elif opcion == '3':
            print("Saliendo...\n")
            break
        
        else:
            print('Opción inválida.')

        print('\n¿Desea seguir ejecutando el código? (Y/N)')
        decision = input('>> ')
        if decision == 'N':
            break