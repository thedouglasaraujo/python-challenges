caixa = 40
receitas = {'hamburguer de siri': ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'), 'pizza de siri': (
    'siri', 'trigo', 'fermento', 'ovos', 'queijo'), 'siri frito': ('siri', 'manteiga'), 'siri a parmegiana': ('siri', 'trigo', 'ovos', 'queijo', 'tomate')}
alimentos = {'trigo': 5, 'fermento': 5, 'manteiga': 5, 'ovos': 5, 'batata': 5, 'arroz': 5,
             'siri': 5, 'pao': 5, 'tomate': 5, 'alface': 5, 'picles': 5, 'queijo': 5}  # Quantidade de alimentos
precos = {'trigo': 12, 'fermento': 8, 'manteiga': 24, 'ovos': 8, 'batata': 16, 'arroz': 12, 'siri': 32, 'pao': 8, 'tomate': 8,
          'alface': 4, 'picles': 12, 'queijo': 20, 'hamburguer de siri': 24, 'pizza de siri': 42, 'siri frito': 15, 'siri a parmegiana': 24}
vendas = {}
novopedido = {}
continuar = True

while continuar == True:
    try:
        pedido = input()
        if pedido in receitas:
            caixa += precos[pedido]
            print(f"{pedido} saindo...")
            for elemento in receitas.get(pedido):
                if alimentos[elemento] == 0:  # Caso o ingrediente tenha acabado
                    # Comprar mais 4 unidades do ingrediente
                    alimentos[elemento] = 4
                    # Diminuir o valor da compra dos ingredientes
                    caixa -= precos[elemento]
                alimentos[elemento] -= 1
            if pedido not in vendas:
                vendas[pedido] = 0
            else:
                vendas[pedido] += 1
        elif pedido not in receitas and pedido not in novopedido:
            novopedido[pedido] = 0
            print(f"{pedido} ainda não é uma opção disponível.")
        elif novopedido[pedido] == 0:
            # Para registrar quando o novo pedido for solicitado 2 vezes
            novopedido[pedido] += 1
            print(f"{pedido} ainda não é uma opção disponível.")
        else:
            ingredientes = input().split(' ')
            # Adicionando a receita do novo pedido
            receitas[pedido] = tuple(ingredientes)
            preconovo = 0
            for i in receitas[pedido]:
                # Calculando o preço do novo pedido com base nos ingredientes
                preconovo += (precos[i])/4
            preconovo += 5
            precos[pedido] = int(preconovo)
            print(
                f"Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.")
    except EOFError:
        print("##### Fim do expediente #####")
        print(f"O lucro obtido no dia de hoje foi de R${caixa-40}.")
        # Para descobrir qual receita vendeu mais
        maximo = vendas[max(vendas, key=vendas.get)]
        for j in vendas:
            if vendas.get(j) == maximo:
                mais_vendido = j
        if mais_vendido == "hamburguer de siri":
            print(
                "O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!")
        else:
            print(
                f"{mais_vendido[0].capitalize()+mais_vendido[1:]} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.")
        continuar = False
