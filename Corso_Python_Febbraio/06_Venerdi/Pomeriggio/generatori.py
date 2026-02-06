def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

numero = 22
print(list(fibonacci(numero)))

for x in list(fibonacci(10)):
    print(x)

for i in list(fibonacci(15)):
    print(i*2)
    lista = []
    lista.append(i*2)

def contatore_fino_a(n):
    # Generatore che produce i numeri da 1 a n
    i = 1
    while i <= n:
        yield i
        i += 1

print(list(contatore_fino_a(10)))

def catena_generatori():
    # Prima produce 1..3, poi 10..12
    yield from range(1,4)
    yield from range(10,13)

print(list(catena_generatori()))