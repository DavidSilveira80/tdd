"""Programa que retorna a soma ou a média de determinada coluna de uma matriz - Uri-1182"""


def coluna_na_matriz(C, T):
    """Recebe como argumentos: um inteiro C para o nº da coluna a ser calculada(C = 5 para somar/média da col. 5.
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

    def soma_da_coluna(C):  # recebe como argumento a coluna que será calculada
        soma_coluna = 0
        for i in range(len(matriz)):  # laço que calcula o tamanho da matriz
            for linha_da_matriz in matriz[i]:  # intera as linhas da matriz
                if linha_da_matriz == matriz[i][C]:  # se elemento da linha corresponde ao n° da coluna a ser calculada
                    soma_coluna += linha_da_matriz  # soma os elementos correspondentes a coluna a ser calculada

        return soma_coluna

    if T == 'M':
        resp = f'A média da coluna {C} da matriz é: {soma_da_coluna(C) / 12:.1f}'

    elif T == 'S':
        resp = f'A soma da coluna {C} da matriz é: {soma_da_coluna(C):.1f}'
    return resp


print(coluna_na_matriz(5, 'M'))
print(coluna_na_matriz(5, 'S'))
