def adicionar_pessoa(dicionario):
    while True:
        try:
            cpf = input("Digite o CPF (9 dígitos): ")
            if not (cpf.isdigit() and len(cpf) == 9):
                raise ValueError("CPF deve ter exatamente 9 dígitos.")

            if cpf in dicionario:
                raise TypeError("Este CPF já foi cadastrado.")

            nome = input("Digite o nome da pessoa: ")
            dicionario[cpf] = nome  
            print("Pessoa adicionada com sucesso!")

            continuar = input("Deseja adicionar outra pessoa? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError as ve:
            print(f"Erro: {ve}")
        except TypeError as te:
            print(f"Erro: {te}")

pessoas = {}
adicionar_pessoa(pessoas)
print("Listagem de pessoas cadastradas:", pessoas)
