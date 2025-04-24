# === Menu Principal ===
def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("🌐 SISTEMA DE ATENDIMENTO AO USUÁRIO".center(50))
    print("=" * 50)
    print("1️⃣  Ajuda")
    print("2️⃣  Quem Somos")
    print("3️⃣  Pesquisa de Satisfação")
    print("4️⃣  Contato")
    print("5️⃣  Área do Paciente")
    print("6️⃣  🚪 Sair do Sistema")
    print("-" * 50)

# === Menu Ajuda ===
def menu_ajuda():
    while True:
        print("\n" + "=" * 50)
        print("📚 MENU DE AJUDA".center(50))
        print("=" * 50)
        print("1️⃣  Tutorial")
        print("2️⃣  FAQ")
        print("3️⃣  Chatbot")
        print("4️⃣  🔙 Voltar ao Menu Principal")
        print("-" * 50)

        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1": menu_tutorial()
            case "2": menu_faq()
            case "3": chatbot()
            case "4": break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

# === Menu Tutorial ===
def menu_tutorial():
    while True:
        print("\n" + "=" * 50)
        print("📚 TUTORIAIS".center(50))
        print("=" * 50)
        print("1️⃣  Como ver minhas consultas")
        print("2️⃣  Como instalar o aplicativo")
        print("3️⃣  Como acessar o portal do paciente")
        print("4️⃣  🔙 Voltar ao menu de Ajuda")
        print("-" * 50)

        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1":
                ver_consultas()
            case "2":
                instalar_app()
            case "3":
                acessar_portal()
            case "4":
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

# === Menu FAQ ===
def menu_faq():
    while True:
        print("\n" + "=" * 50)
        print("📚 FAQ".center(50))
        print("=" * 50)
        print("1️⃣  Como ver minhas consultas")
        print("2️⃣  Como instalar o aplicativo")
        print("3️⃣  Como acessar o portal do paciente")
        print("4️⃣  Meu aplicativo não está funcionando")
        print("5️⃣  Horário de funcionamento do suporte")
        print("6️⃣  🔙 Voltar ao menu de Ajuda")
        print("-" * 50)

        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1":
                ver_consultas()
            case "2":
                instalar_app()
            case "3":
                acessar_portal()
            case "4":
                faq_app_nao_funciona()
            case "5":
                faq_horario_suporte()
            case "6":
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

# === Funções de conteúdo ===
def ver_consultas():
    print("\n📅 Como ver minhas consultas:")
    print("Acesse sua área do paciente e clique na aba 'Consultas'.")
    input("\nPressione Enter para continuar...")

def instalar_app():
    print("\n📲 Como instalar o aplicativo:")
    print("Acesse a loja de aplicativos, busque pelo nome e clique em instalar.")
    input("\nPressione Enter para continuar...")

def acessar_portal():
    print("\n🌐 Como acessar o portal do paciente:")
    print("Acesse www.portal.com.br e entre com seu login e senha.")
    input("\nPressione Enter para continuar...")

def faq_app_nao_funciona():
    print("\n❌ Meu aplicativo não está funcionando:")
    print("Tente reiniciar o aparelho ou reinstalar o aplicativo.")
    input("\nPressione Enter para continuar...")

def faq_horario_suporte():
    print("\n🕒 Horário de funcionamento do suporte:")
    print("Segunda a sexta, das 08h às 18h.")
    input("\nPressione Enter para continuar...")

def chatbot():
    print("\n🤖 Chatbot:")
    print("Assistente virtual para tirar suas dúvidas comuns.")
    input("\nPressione Enter para continuar...")

def pesquisa_satisfacao():
    print("\n📝 Pesquisa de Satisfação")
    iniciar = input("\nAperte 1 para começar a pesquisa: ")
    if iniciar == "1":
        notas = [
            input("De 0 a 10, qual nota você dá para nosso aplicativo? "),
            input("De 0 a 10, qual nota você dá para nosso site? "),
            input("De 0 a 10, qual nota você dá para nosso suporte? ")
        ]
        print("\n✅ Obrigado por responder à pesquisa!")
        print(f"Notas registradas: Aplicativo = {notas[0]}, Site = {notas[1]}, Suporte = {notas[2]}")
    else:
        print("Pesquisa cancelada.")
    input("\nPressione Enter para continuar...")

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

# === Main ===
def main():
    while True:
        mostrar_menu_principal()
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1": menu_ajuda()
            case "2": quem_somos()
            case "3": pesquisa_satisfacao()
            case "4": contato()
            case "5": area_paciente()
            case "6":
                print("\n👋 Saindo do sistema... Até mais!")
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")

# Iniciar o programa
main()
