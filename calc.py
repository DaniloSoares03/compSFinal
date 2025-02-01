# fazer as quatro operaçoes basicas atraves de soma e subtracao. Deve ser recursiva


def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    if b == 0 or a == 0:
        return 0
    return a + multiplicacao(a, b-1)
    
def divisao(a, b):
    if b == 0:
        return 0
    elif a < b:
        return (0, a)
    quociente, resto = divisao(a - b, b)  
    return quociente + 1, resto

def exponencial(a, b):
    if b == 0:
        return 1
    exp = exponencial(a, b -1)
    total = multiplicacao(a, exp)
    return total
    

print("valor de 3 + 6", adicao(3, 6))
print("valor de 5 - 8 ", subtracao(5, 8))
print("valor de 3 * 7", multiplicacao(7, 3))
print("o resultado de 10 / 2: ", divisao(10, 2))
print("o resultado de 3 ^ 4 é : ", exponencial(3, 4))
