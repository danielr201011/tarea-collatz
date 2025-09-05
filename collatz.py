def collatz(n):
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        secuencia.append(n)
    return secuencia


ultimo_digito = int(input("Ingrese el último dígito de su código: "))
N = ultimo_digito + 3
print(f"\nDebe ingresar {N} números enteros.")

numeros = []
for i in range(N):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

promedio = round(sum(numeros) / N)
print(f"\nPromedio (redondeado): {promedio}")

print("\nSecuencia de Collatz:")
print(collatz(promedio))