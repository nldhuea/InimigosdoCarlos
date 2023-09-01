while True:
    try:
        senha = input()

        if not senha.isalnum():
            print("Senha invalida.")
            continue

        len = senha.len()
        if len < 6 or len > 32:
            print("Senha invalida.")
            continue

        minuscula = False
        maiuscula = False
        numero = False

        minusculas = []...
        
        for simb in senha:
            if simb in minusculas:
                ...

    except EOFError:
        break