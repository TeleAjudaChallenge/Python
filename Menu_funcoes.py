# Funções para cada opção
def chatbot():
    print("\nChatbot: Aqui está o Chatbot. Ele ajuda com dúvidas frequentes.")

def tutorial():
    print("\nTutorial: Este é o tutorial de uso da aplicação.")

def perfil_paciente():
    print("\nPerfil do Paciente: Aqui você pode visualizar ou editar o perfil do paciente.")

def pesquisa_satisfacao():
    print("\nPesquisa de Satisfação: Por favor, responda a pesquisa de satisfação.")

def faq():
    print("\nFAQ: Perguntas frequentes e suas respostas.")

def contato():
    print("\nContato: Entre em contato conosco através do email ou telefone.")

def quem_somos():
    print("\nQuem Somos: Conheça nossa equipe e missão.")

def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Chatbot")
    print("2. Tutorial")
    print("3. Perfil do Paciente")
    print("4. Pesquisa de Satisfação")
    print("5. FAQ")
    print("6. Contato")
    print("7. Quem Somos")
    print("0. Sair")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

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
                print("Saindo do programa. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue

        input("\nPressione Enter para voltar ao menu...")

# Inicia o programa
main()
