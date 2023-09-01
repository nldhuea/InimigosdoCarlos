Casodeteste = int(input())

for i in range(Casodeteste):
    String = input().split(" ")
    String1 = String[0]
    String2 = String[1]
    resultado = 0
    for j in range(len(String1)):
        resultado += ((ord(String2[j]) - ord(String1[j])) % 26)
    print(resultado)