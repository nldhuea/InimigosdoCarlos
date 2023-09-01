n = int(input())

for _ in range(n):
    pessoas = int(input())
    idiomas = list()

    for _ in range(pessoas):
        idiomas.append(input())
        for idioma in idiomas:
            if idioma in idiomas:  continue
            else: idiomas.append(idioma)
    if len(idiomas) > 1:
        print("ingles")
    else:
        print(idiomas[0])