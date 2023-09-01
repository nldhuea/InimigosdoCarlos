while True:
    try:
        senha = input()

        if not senha.isalnum():
            print("Senha invalida.")
            continue

        teste =   len(senha)
        if teste < 6 or teste > 32:
            print("Senha invalida.")
            continue

        minuscula = False
        maiuscula = False
        numero = False

        
        
        for simb in senha:
            if simb.islower() and simb.isalpha():
                minuscula = True;
            if simb.isupper() and simb.isalpha():
                maiuscula = True;
            if simb.isnumeric():
                numero = True;

        if(numero and maiuscula and minuscula): print("Senha valida.")
        else: print("Senha invalida.")




    except EOFError:
        break
