N = int(input())

for _ in range(N):
    letras = []
    frase = input()
    for letra in frase:
        if (letra.isalpha()) and (letra not in letras):
            letras.append(letra)
    if len(letras) == 26:
        print("frase completa")
    elif len(letras) >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
        
