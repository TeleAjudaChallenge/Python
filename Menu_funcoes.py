# Funções para cada opção
def chatbot():
    print("\n" + "=" * 50)
    print("🤖 Chatbot:")
    print("Este assistente virtual pode ajudar a responder suas dúvidas mais comuns.")

def tutorial():
    print("\n" + "=" * 50)
    print("📚 Tutorial:")
    print("Aqui você encontra um passo a passo de como utilizar o sistema.")

def perfil_paciente():
    print("\n" + "=" * 50)
    print("🩺 Perfil do Paciente:")
    print("Veja e edite as informações pessoais e médicas do paciente.")

def pesquisa_satisfacao():
    print("\n" + "=" * 50)
    print("📝 Pesquisa de Satisfação:")
    print("Responda à pesquisa para nos ajudar a melhorar nossos serviços.")

def faq():
    print("\n" + "=" * 50)
    print("❓ FAQ - Perguntas Frequentes:")
    print("Encontre respostas rápidas para dúvidas comuns.")

def contato():
    print("\n" + "=" * 50)
    print("📞 Contato:")
    print("Entre em contato conosco pelo telefone, e-mail ou chat.")

def quem_somos():
    print("\n" + "=" * 50)
    print("🏢 Quem Somos:")
    print("Conheça mais sobre nossa equipe, história e missão.")

def mostrar_menu():
    print("\n" + "="*50)
    print("🌐 SISTEMA DE ATENDIMENTO AO USUÁRIO".center(50))
    print("="*50)
    print("Escolha uma das opções abaixo:")
    print("1️⃣  - Chatbot")
    print("2️⃣  - Tutorial de Uso")
    print("3️⃣  - Perfil do Paciente")
    print("4️⃣  - Pesquisa de Satisfação")
    print("5️⃣  - FAQ (Perguntas Frequentes)")
    print("6️⃣  - Contato")
    print("7️⃣  - Quem Somos")
    print("0️⃣  - Sair do Sistema")
    print("-"*50)

def main():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ")

        match opcao:
            case "1":
                chatbot()
            case "2":
                tutorial()
            case "3":
                perfil_paciente()
            case "4":
                pesquisa_satisfacao()
            case "5":
                faq()
            case "6":
                contato()
            case "7":
                quem_somos()
            case "0":
                print("\n👋 Encerrando o sistema... Até logo!")
                break
            case _:
                print("\n❌ Opção inválida. Por favor, tente novamente.")
                continue

        input("\n🔁 Pressione Enter para voltar ao menu principal...")

# Inicia o programa
main()
