import time


# Codigo Auxiliar:
def Ordenacao(arr):
    n = len(arr)
    posicao = 0

    while posicao < n - 1:
        if arr[posicao] > arr[posicao + 1]:
            arr[posicao], arr[posicao + 1] = arr[posicao + 1], arr[posicao]
            posicao = 0  # Reiniciar a verificação a partir do início do array
        else:
            posicao += 1

    return arr


# Exercício 1
def VerificaSoma(arr, valor):
    arrOrdenado = Ordenacao(arr)

    print(f'Organizando o vetor: {arrOrdenado}')
    print(f'Vamos verificar se na lista existem valores que se somados resultam em: {valor}')
    time.sleep(2)

    n = len(arrOrdenado)
    encontrouSoma = False

    for i in range(n):
        for j in range(i+1, n):
            if arr[j] + arr[i] == valor:
                print(f'Os elementos da lista cuja a soma é: {valor}, são: {arr[j]} e {arr[i]}')
                encontrouSoma = True
    if encontrouSoma == False:
        print('Sem valores correspondentes') 


if __name__ == '__main__':
    VerificaSoma([1,3,2,4], 9)


# Exercício 2
def MaiorElemento(arr):
    arrOrdenado = Ordenacao(arr)
    n = len(arrOrdenado)
    maior = None

    for i in range(n):
        