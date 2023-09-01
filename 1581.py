N = int(input())

for _ in range(N):
    K = int(input())

    idioma1 = input()
    mesmaLingua = True
    for i in range(1, K):
        idioma = input()

        if idioma1 != idioma:
            mesmaLingua = False
    
    if mesmaLingua == False:
        print("ingles")
    else:
        print(idioma1)
