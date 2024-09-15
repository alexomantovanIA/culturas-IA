# print("Esse programa exibirá o seu nome completo")
# nome = input("Por favor, digite seu nome: ")
# sobrenome = input("Por favor, digite seu sobrenome: ")
# nome_completo = nome + " " + sobrenome
# print(f"Seu nome completo é {nome_completo}")

# numbers = [1,2,3,4,5]
# doubles = [num * 2 for num in numbers]
# triplets = [num * 3 for num in numbers]
# print(triplets)
print("FAZENDA AROEIRAS")
print("Assistente de Plantio e Manejo")
# Dados das culturas
milho_dados = {
    "sementes_por_hectare": 20,  # kg por hectare
    "agua_por_hectare": 0.6,  # m³ por hectare
    "herbicida_por_hectare": 3,  # litros por hectare
    "inseticida_por_hectare": 0.5,  # litros por hectare
    "fungicida_por_hectare": 1.5,  # litros por hectare
    "calcario_por_hectare": 3.5,  # toneladas por hectare
    "plantas_por_hectare": 60000,  # número de plantas por hectare
    "produtividade_por_hectare": 8  # toneladas por hectare
}

cafe_dados = {
    "mudas_por_hectare": 4000,  # mudas por hectare
    "agua_por_hectare": 1.5,  # m³ por hectare
    "herbicida_por_hectare": 2,  # litros por hectare
    "inseticida_por_hectare": 1.5,  # litros por hectare
    "fungicida_por_hectare": 3,  # litros por hectare
    "calcario_por_hectare": 3.5,  # toneladas por hectare
    "plantas_por_hectare": 8000,  # número de plantas por hectare
    "produtividade_por_hectare": 25  # sacas por hectare
}

feijao_dados = {
    "sementes_por_hectare": 60,  # kg por hectare
    "agua_por_hectare": 0.5,  # m³ por hectare
    "herbicida_por_hectare": 2,  # litros por hectare
    "inseticida_por_hectare": 0.7,  # litros por hectare
    "fungicida_por_hectare": 0.7,  # litros por hectare
    "calcario_por_hectare": 3,  # toneladas por hectare
    "plantas_por_hectare": 300000,  # número de plantas por hectare
    "produtividade_por_hectare": 2  # toneladas por hectare
}

mandioca_dados = {
    "manivas_por_hectare": 12000,  # manivas por hectare
    "agua_por_hectare": 0.7,  # m³ por hectare
    "herbicida_por_hectare": 3,  # litros por hectare
    "inseticida_por_hectare": 1.5,  # litros por hectare
    "fungicida_por_hectare": 1.5,  # litros por hectare
    "calcario_por_hectare": 2,  # toneladas por hectare
    "plantas_por_hectare": 12000,  # número de plantas por hectare
    "produtividade_por_hectare": 25  # toneladas por hectare
}

# Função para calcular o consumo para uma área
def calcular_para_area(area_em_hectares, dados):
    consumos = {}
    for item, valor_por_hectare in dados.items():
        consumos[item] = valor_por_hectare * area_em_hectares
    return consumos

# Função para exibir o menu e capturar a escolha do usuário
def escolher_cultura():
    print("Escolha uma cultura:")
    print("A - Milho")
    print("B - Café")
    print("C - Feijão")
    print("D - Mandioca")
    print("S - Sair")
    opcao = input("Escolha uma opção: ").upper()

    if opcao == "A":
        return "Milho", milho_dados
    elif opcao == "B":
        return "Café", cafe_dados
    elif opcao == "C":
        return "Feijão", feijao_dados
    elif opcao == "D":
        return "Mandioca", mandioca_dados
    elif opcao == "S":
        return "Sair", None
    else:
        print("Opção inválida. Tente novamente.")
        return escolher_cultura()

# Função principal
def menu_principal():
    while True:
        # Primeira escolha de cultura
        print("\n# Escolha a primeira cultura:")
        cultura1, dados1 = escolher_cultura()
        if cultura1 == "Sair":
            print("Encerrando o programa...")
            break

        # Perguntar a área para a primeira cultura
        try:
            area1 = float(input(f"Informe a área para {cultura1} (até 150 hectares): "))
            if area1 > 150 or area1 <= 0:
                print("Área inválida. Deve ser entre 1 e 150 hectares.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        # Perguntar se o usuário quer escolher uma segunda cultura
        escolha_segunda_cultura = input("\nDeseja escolher uma segunda cultura? (S/N): ").upper()

        if escolha_segunda_cultura == "S":
            # Segunda escolha de cultura
            print("\n# Escolha a segunda cultura:")
            cultura2, dados2 = escolher_cultura()
            if cultura2 == "Sair":
                print("Encerrando o programa...")
                break

            # Perguntar a área para a segunda cultura
            try:
                area2 = float(input(f"Informe a área para {cultura2} (até 150 hectares): "))
                if area2 > 150 or area2 <= 0:
                    print("Área inválida. Deve ser entre 1 e 150 hectares.")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                continue
        else:
            cultura2 = None
            area2 = None
            dados2 = None

        # Calcular e exibir resultados
        print(f"\nResultados para {area1} hectares de {cultura1}:")
        resultado1 = calcular_para_area(area1, dados1)
        for item, valor in resultado1.items():
            print(f"{item.capitalize()}: {valor}")

        if cultura2:
            print(f"\nResultados para {area2} hectares de {cultura2}:")
            resultado2 = calcular_para_area(area2, dados2)
            for item, valor in resultado2.items():
                print(f"{item.capitalize()}: {valor}")

        # Perguntar se o usuário deseja sair ou reiniciar
        reiniciar = input("\nDeseja realizar outra operação? (S para Sim, N para Não): ").upper()
        if reiniciar == "N":
            print("Encerrando o programa...")
            break

# Executando o menu principal
menu_principal()