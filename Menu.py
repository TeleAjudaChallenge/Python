while True:
    print("\n" + "=" * 50)
    print("🌐 SISTEMA DE ATENDIMENTO AO USUÁRIO".center(50))
    print("=" * 50)
    print("Escolha uma das opções abaixo:")
    print("1️⃣  - Chatbot")
    print("2️⃣  - Tutorial de Uso")
    print("3️⃣  - Perfil do Paciente")
    print("4️⃣  - Pesquisa de Satisfação")
    print("5️⃣  - FAQ (Perguntas Frequentes)")
    print("6️⃣  - Contato")
    print("7️⃣  - Quem Somos")
    print("0️⃣  - Sair do Sistema")
    print("-" * 50)
    opcao = input("Digite o número da opção desejada: ")

    match opcao:
        case "1":
            print("\n" + "=" * 50)
            print("🤖 Chatbot:")
            print("Este assistente virtual pode ajudar a responder suas dúvidas mais comuns.")
        case "2":
            print("\n" + "=" * 50)
            print("📚 Tutorial:")
            print("Aqui você encontra um passo a passo de como utilizar o sistema.")
        case "3":
            print("\n" + "=" * 50)
            print("🩺 Perfil do Paciente:")
            print("Veja e edite as informações pessoais e médicas do paciente.")
        case "4":
            print("\n" + "=" * 50)
            print("📝 Pesquisa de Satisfação:")
            print("Responda à pesquisa para nos ajudar a melhorar nossos serviços.")
        case "5":
            print("\n" + "=" * 50)
            print("❓ FAQ - Perguntas Frequentes:")
            print("Encontre respostas rápidas para dúvidas comuns.")
        case "6":
            print("\n" + "=" * 50)
            print("📞 Contato:")
            print("Entre em contato conosco pelo telefone, e-mail ou chat.")
        case "7":
            print("\n" + "=" * 50)
            print("🏢 Quem Somos:")
            print("Conheça mais sobre nossa equipe, história e missão.")
        case "0":
            print("\n👋 Encerrando o sistema... Até logo!")
            break
        case _:
            print("\n❌ Opção inválida. Por favor, tente novamente.")
            continue

    input("\n🔁 Pressione Enter para voltar ao menu principal...")

