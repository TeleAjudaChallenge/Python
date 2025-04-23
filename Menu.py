while True:
    print("=== MENU PRINCIPAL ===")
    print("1. Chatbot")
    print("2. Tutorial")
    print("3. Perfil do Paciente")
    print("4. Pesquisa de Satisfação")
    print("5. FAQ")
    print("6. Contato")
    print("7. Quem Somos")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("\nChatbot: Aqui está o Chatbot. Ele ajuda com dúvidas frequentes.")
        case "2":
            print("\nTutorial: Este é o tutorial de uso da aplicação.")
        case "3":
            print("\nPerfil do Paciente: Aqui você pode visualizar ou editar o perfil do paciente.")
        case "4":
            print("\nPesquisa de Satisfação: Por favor, responda a pesquisa de satisfação.")
        case "5":
            print("\nFAQ: Perguntas frequentes e suas respostas.")
        case "6":
            print("\nContato: Entre em contato conosco através do email ou telefone.")
        case "7":
            print("\nQuem Somos: Conheça nossa equipe e missão.")
        case "0":
            print("Saindo do programa. Até logo!")
            break
        case _:
            print("Opção inválida. Tente novamente.")
            continue

    input("\nPressione Enter para voltar ao menu...")

