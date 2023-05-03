n = int(input())  # Total de rodadas

rodadas = 0  # Contador para as rodadas
pontos_sheldon = 0
pontos_raj = 0

if (n > 0):
    while (rodadas < n):  # Enquanto o contador não atingir o número de rodadas (dado pelo input)
        sheldon = input().lower()
        raj = input().lower()
        rodadas += 1
        # Casos em que Sheldon ganha o ponto
        if (sheldon == "lagarto") and (raj == "spock"):
            pontos_sheldon += 1
        if (sheldon == "spock") and (raj == "tesoura"):
            pontos_sheldon += 1
        if (sheldon == "tesoura") and (raj == "lagarto"):
            pontos_sheldon += 1
        # Casos em que Raj ganha o ponto
        if (raj == "lagarto") and (sheldon == "spock"):
            pontos_raj += 1
        if (raj == "spock") and (sheldon == "tesoura"):
            pontos_raj += 1
        if (raj == "tesoura") and (sheldon == "lagarto"):
            pontos_raj += 1
        # Caso Sheldon e Raj joguem a mesma opção, a pontuação não é alterada:
        if (sheldon == raj):
            pontos_sheldon += 0
            pontos_raj += 0

    # Sheldon vence um maior número de rodadas:
    if (pontos_sheldon > pontos_raj):
        print("BAZINGA! EU SOU O SENHOR DA SALA!")
    # Raj vence um maior número de rodadas:
    if (pontos_raj > pontos_sheldon):
        print("ENGOLE ESSA, SHELDON!")
    # Empate entre os dois jogadores:
    if (pontos_raj == pontos_sheldon):
        print("Oh não, precisamos de outra rodada.")
