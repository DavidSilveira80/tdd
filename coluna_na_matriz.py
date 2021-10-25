"""Programa que retorna a soma ou a média de determinada coluna de uma matriz - Uri-1182"""


def coluna_na_matriz(coluna, T):
    """Recebe como argumentos: um inteiro 'coluna' para o nº da coluna a ser calculada(coluna = 5
       para somar/média da col. 5.
       E um caracter T para o tipo de cálculo a ser feito( T = 'S' para soma/ T = 'M' para média). """

    matriz = (
        (0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 2.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 3.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 4.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 5.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 6.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 7.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 8.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 9.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 10.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 11.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 12.0, 0, 0, 0, 0, 0, 0)
    )

    def soma_da_coluna(coluna):  # recebe como argumento a coluna que será calculada.
        soma_coluna = 0
        for linha in range(len(matriz)):  # intera as linhas da matriz.
            soma_coluna += matriz[linha][coluna]  # soma os elementos correspondentes a coluna a ser calculada.
        return soma_coluna

    if T == 'M':
        resp = f'A média da coluna {coluna} da matriz é: {soma_da_coluna(coluna) / 12:.1f}'

    elif T == 'S':
        resp = f'A soma da coluna {coluna} da matriz é: {soma_da_coluna(coluna):.1f}'
    return resp


print(coluna_na_matriz(5, 'M'))
print(coluna_na_matriz(5, 'S'))
