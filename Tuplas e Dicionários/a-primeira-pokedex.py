pokemons = {}  # Criando dicionário
continuar = True
while continuar == True:
    try:
        comando = input()
        if comando[0:3] == "ADD":
            if comando[4:] in pokemons:  # Selecionando o nome do Pokemon
                print("Pokémon já adicionado na Pokédex")
            else:
                # Adicionando o pokemon e a sua descrição ao dicionário
                pokemons[comando[4:]] = input()
                print("Pokémon adicionado com sucesso")
        if comando[0:4] == "DESC":
            nome = comando[5:]  # Selecionando a descrição do Pokemon
            if nome in pokemons:
                print(pokemons.get(nome))  # Imprimindo a descrição do Pokemon
            else:
                print("Ainda não há registro desse Pokémon")
    except EOFError:
        continuar = False
