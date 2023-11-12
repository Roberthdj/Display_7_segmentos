
def capturar_entrada():
    entrada = input("Que valor deseas mostrar: ")

    while not entrada.isdigit():
        entrada = input(
            "Ingrese solo números enteros positivos, que valor deseas mostrar: ")

    for item in entrada:
        display.append(led_status(digits[int(item)]))


def led_status(digito):
    tablero = [[' ' for i in range(3)]for j in range(5)]
    leds = []

    if digito[0] == '1':
        tablero[0][0] = tablero[0][1] = tablero[0][2] = '#'
    if digito[1] == '1':
        tablero[0][2] = tablero[1][2] = tablero[2][2] = '#'
    if digito[2] == '1':
        tablero[2][2] = tablero[3][2] = tablero[4][2] = '#'
    if digito[3] == '1':
        tablero[4][0] = tablero[4][1] = tablero[4][2] = '#'
    if digito[4] == '1':
        tablero[2][0] = tablero[3][0] = tablero[4][0] = '#'
    if digito[5] == '1':
        tablero[0][0] = tablero[1][0] = tablero[2][0] = '#'
    if digito[6] == '1':
        tablero[2][0] = tablero[2][1] = tablero[2][2] = '#'

    for i in range(5):
        leds.append(''.join(tablero[i]))

    return leds


def mostrar_display(lista):
    for i in range(5):
        concat = ''
        for j in range(len(lista)):
            concat += lista[j][i] + ' '
        print(concat)


if __name__ == '__main__':
    digits = [
        '1111110',  # 0
        '0110000',  # 1
        '1101101',  # 2
        '1111001',  # 3
        '0110011',  # 4
        '1011011',  # 5
        '1011111',  # 6
        '1110000',  # 7
        '1111111',  # 8
        '1111011'   # 9
    ]
    display = []
    capturar_entrada()
    mostrar_display(display)
