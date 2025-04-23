# === Menu Principal ===
def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("🌐 SISTEMA DE ATENDIMENTO AO USUÁRIO".center(50))
    print("=" * 50)
    print("1️⃣  Ajuda")
    print("2️⃣  Quem Somos")
    print("3️⃣  Contato")
    print("4️⃣  Área do Paciente")
    print("5️⃣  🚪 Sair do Sistema")
    print("--------------------------")

# === Menu Ajuda ===
def menu_ajuda():
    while True:
        print("\n" + "=" * 50)
        print("📚 MENU DE AJUDA".center(40))
        print("=" * 50)
        print("1️⃣  Tutorial")
        print("2️⃣  FAQ")
        print("3️⃣  Chatbot")
        print("4️⃣  Pesquisa de Satisfação")
        print("5️⃣  🔙 Voltar ao Menu Principal")
        print("--------------------------")

        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1": menu_tutorial()
            case "2": menu_faq()
            case "3": chatbot()
            case "4": pesquisa_satisfacao()
            case "5": break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

def menu_tutorial():
    while True:
        print("\n" + "=" * 50)
        print("📚 TUTORIAIS".center(40))
        print("=" * 50)
        print("1️⃣  Como ver minhas consultas")
        print("2️⃣  Como instalar o aplicativo")
        print("3️⃣  Como acessar o portal do paciente")
        print("4️⃣  🔙 Voltar ao menu de Ajuda")
        print("--------------------------")

        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1":
                ver_consultas()
                input("\nPressione Enter para continuar...")
            case "2":
                instalar_app()
                input("\nPressione Enter para continuar...")
            case "3":
                acessar_portal()
                input("\nPressione Enter para continuar...")
            case "4":
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

def menu_faq():
    while True:
        print("\n" + "=" * 50)
        print("📚 FAQ".center(40))
        print("=" * 50)
        print("1️⃣  Como ver minhas consultas")
        print("2️⃣  Como instalar o aplicativo")
        print("3️⃣  Como acessar o portal do paciente")
        print("4️⃣  Meu aplicativo não está funcionando")
        print("5️⃣  Horário de funcionamento do suporte")
        print("6️⃣  🔙 Voltar ao menu de Ajuda")
        print("--------------------------")

        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1":
                ver_consultas()
                input("\nPressione Enter para continuar...")
            case "2":
                instalar_app()
                input("\nPressione Enter para continuar...")
            case "3":
                acessar_portal()
                input("\nPressione Enter para continuar...")
            case "4":
                faq_app_nao_funciona()
                input("\nPressione Enter para continuar...")
            case "5":
                faq_horario_suporte()
                input("\nPressione Enter para continuar...")
            case "6":
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

# === Funções do submenu FAQ ===
def faq_app_nao_funciona():
    print("\n❌ Meu aplicativo não está funcionando:")
    print("Tente reiniciar o aparelho ou reinstalar o aplicativo.")

def faq_horario_suporte():
    print("\n🕒 Horário de funcionamento do suporte:")
    print("Segunda a sexta, das 08h às 18h.")


# === Outras funções da Ajuda ===
def chatbot():
    print("\n🤖 Chatbot:")
    print("Assistente virtual para tirar suas dúvidas comuns.")
    input("\nPressione Enter para continuar...")

def pesquisa_satisfacao():
    print("\n📝 Pesquisa de Satisfação:")
    print("Ajude-nos a melhorar respondendo a pesquisa.")
    input("\nPressione Enter para continuar...")

# === Funções do submenu TUTORIAL ===
def ver_consultas():
    print("\n📅 Como ver minhas consultas:")
    print("Acesse sua área do paciente e clique na aba 'Consultas'.")

def instalar_app():
    print("\n📲 Como instalar o aplicativo:")
    print("Acesse a loja de aplicativos, busque pelo nome e clique em instalar.")

def acessar_portal():
    print("\n🌐 Como acessar o portal do paciente:")
    print("Acesse www.portal.com.br e entre com seu login e senha.")

# === Menu Principal ===
def quem_somos():
    print("\n🏢 Quem Somos:")
    print("Instituição dedicada ao bem-estar dos pacientes.")
    input("\nPressione Enter para continuar...")

def contato():
    print("\n📞 Contato:")
    print("Telefone: (11) 1234-5678 | Email: contato@instituicao.com")
    input("\nPressione Enter para continuar...")

def area_paciente():
    print("\n👤 Área do Paciente:")
    print("Acesse e edite suas informações pessoais e histórico.")
    input("\nPressione Enter para continuar...")


def main():
    while True:
        mostrar_menu_principal()
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1": menu_ajuda()
            case "2": quem_somos()
            case "3": contato()
            case "4": area_paciente()
            case "5":
                print("\n👋 Saindo do sistema... Até mais!")
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

# Iniciar o programa
main()