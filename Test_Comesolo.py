def mostrar_cuadro(cuadrado):
    
    '''Esta funcion permite imprimir la matriz'''
    
    for Renglon in range(5): # Fila son cinco elementos
        for Columna in range(5): # Columna, son cinco elementos
    
            if Columna != 4 : # es para imprimir el ultimo '$' y cambiar de linea
                print(cuadrado[Renglon][Columna], end = '  ')
            else :
                print(cuadrado[Renglon][Columna])
                print('')


def juego (cuadrado):
    
    '''En esta funcion se llevan a cabo
        todas las operaciones del juego'''
    
    preg = input('Quieres jugar? ')
    if preg != 'n' and preg != 's' :
        while preg != 'n' and preg != 's' :
            print('Escribe "s" o "n"')
            preg = input('Quieres jugar? ')
            
    while preg == 's' : # mientras que el jugador quiera jugar
        reng = int(input('Renglon?: '))
        col = int(input('Columna?: '))
        
        if reng < 0 or col < 0: # no se aceptan numeros negativos
            print('Movimiento invalido')
            print('')
        
        else :
            print('Direccion a mover? \n a - izq, s - aba, d - der, w - arr : ')
            mov = input(' ')
            print('')
            
            if mov == 'a' and not(col + 1 <= 2) : # Si esta en la columna 0 o 1, no se mueve
                                                  # Verifica valor de variable mov
                                                  # Se usa 2 porque a partir de columna 1 (2) no se puede mover a izq
                    # Este if (inferior) analiza tres cosas.
                    # 1. el 'objeto' que queremos mover no esta vacio '$'
                    # 2. el lugar hacia donde se mueve esta vacio
                    # 3. debe de estar lleno el espacio entre medio del '$' y '_'
                if  cuadrado[reng + 1][col + 1] == '$' and cuadrado[reng + 1][col - 1] == '_' and  \
                    cuadrado[reng + 1][col] != '_':
                                                
                    cuadrado[reng + 1][col + 1] = '_' # Lugar que queremos mover
                    cuadrado[reng + 1][col] = '_'     # Espacio entre medio
                    cuadrado[reng + 1][col - 1] = '$' # Lugar hacia donde nos movemos
                    
                else :
                    print('movimiento invalido. Intenta de nuevo')
                    print('')
                    
            elif mov == 'd' and not(col + 1 >= 3): # Si esta en la columna 2 o 3, no se mueve
                                                   # Verifica valor de variable mov
                                                   # Se usa 3 porque a partir de columna 2 (3) no se puede mover a der
                        # Explicacion de 'if' superior tambien aplica en este caso
                if cuadrado[reng + 1][col + 1] == '$' and cuadrado[reng + 1][col + 2] != '_' and \
                   cuadrado[reng + 1][col + 3] == '_' :
                                                                                                 
                    cuadrado[reng + 1][col + 1] = '_' # Lugar que queremos mover 
                    cuadrado[reng + 1][col + 2] = '_' # Espacio entre medio
                    cuadrado[reng + 1][col + 3] = '$' # Lugar hacia donde nos movemos
                else :
                    print('movimiento invalido. Intenta de nuevo')
                    
            elif mov == 'w' and not(reng + 1 <= 2):  # Si esta en el renglon 0 o 1, no se mueve
                                                     # Verifica valor de variable mov
                                                     # Se usa 2 porque a partir del renglon 1 (2) no se puede subir
                       # Explicacion de 'if' superior tambien aplica en este caso
                if cuadrado[reng + 1][col + 1] == '$' and cuadrado[reng][col + 1] != '_' and \
                   cuadrado[reng - 1][col + 1] == '_':
                        
                    cuadrado[reng + 1][col + 1] = '_' # Lugar que queremos mover
                    cuadrado[reng][col + 1] = '_'     # Espacio entre medio 
                    cuadrado[reng - 1][col + 1] = '$' # Lugar hacia donde nos movemos
                    
                else :
                    print('movimiento invalido. Intenta de nuevo')
                    print('')
                    
            elif mov == 's' and  not (reng + 1 >= 3): # Si esta en el renglon 2 o 3, no se mueve
                                                      # Verifica valor de variable mov
                                                      # Se usa 3 porque a partir de linea 2 (3) no se puede bajar
                   # Explicacion de 'if' superior tambien aplica en este caso
                if cuadrado[reng + 1][col + 1] == '$' and cuadrado[reng + 2][col + 1] != '_'  and \
                   cuadrado[reng + 3][col + 1] == '_':
                        
                    cuadrado[reng + 1][col + 1] = '_' # Lugar que queremos mover
                    cuadrado[reng + 2][col + 1] = '_' # Espacio entre medio
                    cuadrado[reng + 3][col + 1] = '$' # Lugar hacia donde nos movemos
                else :
                    print('Movimiento invalido. Intenta de nuevo')
                    print('')
                    
            else :
                print('Movimiento invalido. Intenta de nuevo')
                print('')
                
            mostrar_cuadro(cuadrado)
            preg = input('Seguir jugando? ')
            
            if preg == 'n' :
                break
            
            elif preg != 'n' and preg != 's' :
                while preg != 'n' and preg != 's':
                    print('Escribe "s" o "n"')
                    preg = input('Seguir jugando? ')
            

    
def main():
    
    matriz = [[' ', 0, 1,2,3],[0,'_','$','$','$'],[1,'$','$','$','$'],[2,'$','$','$','$'],[3,'_','$','$','$']]
    mostrar_cuadro(matriz)
    juego(matriz)
   
main()   