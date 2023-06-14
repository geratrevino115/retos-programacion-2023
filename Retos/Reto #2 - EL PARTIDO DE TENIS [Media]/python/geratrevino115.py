# Reto #2: EL PARTIDO DE TENIS

## Enunciado

# ```
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
# ```

lista = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']

def marcador(lista: list):
    P1 = 0
    P2 = 0
    puntos = ("Love", 15, 30, 40)

    for elemento in lista:
        if elemento == 'P1':
            P1+=1
        elif elemento == 'P2':
            P2+=1

        if P1 >= 3 and P2 >= 3:
            ventaja = P1 - P2
            if ventaja == 0:
                print('Duece')
            elif ventaja == 1:
                print('Ventaja P1')
            elif ventaja == -1:
                print('Ventaja P2')
            elif ventaja == 2:
                print('Ha ganado P1')
                break
            elif ventaja == -2:
                print('Ha ganado P2')
                break
        else:        
            print('{} - {}'.format(puntos[P1], puntos[P2])) 
    
if __name__ == "__main__":
    marcador(lista)