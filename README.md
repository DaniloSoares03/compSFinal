# Calculadora Recursiva - Valor 80

## Implementação
Este projeto implementa uma calculadora utilizando apenas soma e subtração, aplicando recursividade para as operações.

### Funcionalidades Implementadas
- Adição
- Subtração
- Multiplicação
- Divisão
- Exponenciação

### Explicação das Funções

#### Multiplicação
A multiplicação é realizada através de somas sucessivas. Caso o multiplicador seja zero, o resultado é zero. Caso contrário, a função soma o multiplicando recursivamente até atingir o valor do multiplicador.

```python
def multiplicacao(a, b):
    if b == 0 or a == 0:
        return 0
    return a + multiplicacao(a, b - 1)
```

A função chama a si mesma diminuindo o multiplicador `b` em 1 a cada chamada, somando `a` repetidamente até que `b` atinja zero, momento em que a recursão para.

#### Divisão
A divisão é implementada utilizando subtrações sucessivas. O quociente é o número de vezes que o divisor pode ser subtraído do dividendo antes de se tornar menor que ele. A função retorna uma tupla com o quociente e o resto.

```python
def divisao(a, b):
    if b == 0:
        return 0  # Evita divisão por zero
    elif a < b:
        return (0, a)
    quociente, resto = divisao(a - b, b)
    return quociente + 1, resto
```

A cada chamada recursiva, o valor de `b` é subtraído de `a`, reduzindo progressivamente o dividendo. Quando `a` for menor que `b`, a função retorna `(0, a)`, indicando que a divisão terminou e o resto da operação. O `+1` na linha final é necessário para contar quantas vezes `b` foi subtraído até esse ponto, formando assim o quociente.

#### Exponenciação
A exponenciação é realizada multiplicando a base por si mesma recursivamente até atingir o expoente. O caso base é quando o expoente é zero, retornando 1.

```python
def exponencial(a, b):
    if b == 0:
        return 1
    exp = exponencial(a, b - 1)
    total = multiplicacao(a, exp)
    return total
```

Aqui, a função reduz `b` recursivamente, chamando a si mesma até que `b` chegue a zero. Para logo após chamar a função multiplicação com o valor atualizado do expoente

