from itertools import islice

def sieve ():
    primos = [2]
    while True:
        yield primos[len(primos)-1]
        a = primos[len(primos)-1]+1 #3
        encontrado = False

        while not encontrado:
            i = 0
            primo = True
            while i < len(primos) and primo:
                if a%primos[i] == 0: primo = False
                i += 1

            if primo: encontrado = True
            else: a += 1
        primos.append(a);

if __name__ == '__main__':
    print(list (islice (sieve(), 25)))