

# === Menu principal com controle de navegação ===
while True:
    print("\n" + "=" * 50)
    print("🌐 SISTEMA DE ATENDIMENTO AO USUÁRIO".center(50))
    print("=" * 50)
    print("1️⃣  - Ajuda")
    print("2️⃣  - Quem Somos")
    print("3️⃣  - Contato")
    print("4️⃣  - Área do Paciente")
    print("5️⃣  - Sair do sistema")
    opcao = input("Digite o número da opção desejada: ")

    match opcao:
        case "1":
            while True:
                print("\n" + "-" * 40)
                print("📚 MENU DE AJUDA".center(40))
                print("-" * 40)
                print("1 - Chatbot")
                print("2 - Tutorial")
                print("3 - FAQ")
                print("4 - Pesquisa de Satisfação")
                print("5 - Retornar ao Menu Inicial")
                print("-" * 40)
                sub_opcao = input("Escolha uma opção de ajuda: ")

                match sub_opcao:
                    case "1":
                        print("\n🤖 Chatbot:")
                        print("Este assistente virtual pode ajudar a responder suas dúvidas mais comuns.")
                    case "2":
                        print("\n📚 Tutorial:")
                        print("Aqui você encontra um passo a passo de como utilizar o sistema.")
                    case "3":
                        print("\n❓ FAQ - Perguntas Frequentes:")
                        print("Encontre respostas rápidas para dúvidas comuns.")
                    case "4":
                        print("\n📝 Pesquisa de Satisfação:")
                        print("Responda à pesquisa para nos ajudar a melhorar nossos serviços.")
                    case "5":
                        print("\n🔙 Retornando ao menu principal...")
                        break
                    case _:
                        print("❌ Opção inválida no menu de ajuda.")

                input("\n🔁 Pressione Enter para voltar ao Menu de Ajuda...")

        case "2":
            print("\n🏢 Quem Somos:")
            print("Conheça mais sobre nossa equipe, história e missão.")
            input("\n🔁 Pressione Enter para voltar ao menu principal...")

        case "3":
            print("\n📞 Contato:")
            print("Entre em contato conosco pelo telefone, e-mail ou chat.")
            input("\n🔁 Pressione Enter para voltar ao menu principal...")

        case "4":
            print("\n🩺 Área do Paciente:")
            print("Veja e edite as informações pessoais e médicas do paciente.")
            input("\n🔁 Pressione Enter para voltar ao menu principal1...")

        case "5":
            print("\n👋 Encerrando o sistema... Até logo!")
            break

        case _:
            print("❌ Opção inválida. Tente novamente.")

