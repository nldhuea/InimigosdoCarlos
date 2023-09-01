risada = input()
comp = ''
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(len(risada)):
    if risada[i] in vowel:
        comp += risada[i]
if(comp == comp[::-1]):
    print('S')
else:
    print('N')