# === Inicio do Programa ===
print("\n" + "=" * 50)
print("🌐 SISTEMA DE ATENDIMENTO AO USUÁRIO".center(50))
print("=" * 50)
print("1️⃣  Já tenho cadastro")
print("2️⃣  Fazer cadastro")
opcao = input("Escolha uma oção: ")
if opcao == "1":
    usuario = input("\nUsuario: ")
    senha = input("\nSenha: ")
    validar_usuario(usuario, senha)
else:



def validar_usuario(usuario, senha):
    print("Confirmado")


# === Menu Principal ===
def mostrar_menu_principal(usuario):
    print("\n" + "=" * 50)
    print(f"🌐 BEM-VINDO(A) {usuario}".center(50))
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
            case "1":
                menu_tutorial()
            case "2":
                menu_faq()
            case "3":
                chatbot()
            case "4":
                break
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
                acessar_consultas()
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
        print("2️⃣  Meu microfone não está funcionando")
        print("3️⃣  Minha câmera não está funcionando")
        print("4️⃣  Problemas ao fazer login")
        print("5️⃣  Esqueci minha senha")
        print("6️⃣  🔙 Voltar ao menu de Ajuda")
        print("-" * 50)

        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1":
                ver_consultas()
            case "2":
                mic_problema()
            case "3":
                camera_problema()
            case "4":
                login_problema()
            case "5":
                esqueci_senha()
            case "6":
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")


# === Funções de FAQ ===
def ver_consultas():
    print("\n📅 Como ver minhas consultas:")
    print("Após fazer login no Portal do Paciente, clique em “Teleconsulta” no menu e veja sua agenda.")
    print("No dia e horário marcados, clique na consulta para entrar.")
    print("📘 Para aprender como fazer isso, acesse:")
    print("👉 www.hcportal.com/consultas")
    input("\nPressione Enter para continuar...")


def mic_problema():
    print("\n🎤 Meu microfone não está funcionando:")
    print("Se você não está sendo ouvido na teleconsulta, o microfone pode estar bloqueado. ")
    print("Também é importante selecionar a opção “Microfone” ao iniciar a consulta e aceitar o teste de som.")
    print("📘 Para aprender como permitir acesso a seu microfone, acesse:")
    print("👉 www.hcportal.com/microfone")


def camera_problema():
    print("\n📷 Minha câmera não está funcionando:")
    print("A câmera pode precisar de permissão para funcionar corretamente durante a teleconsulta.")
    print("A câmera ajuda na avaliação médica, por isso é importante que esteja funcionando")
    print("📘 Para aprender como permitir acesso a sua câmera, acesse:")
    print("👉 www.hcportal.com/camera")

    input("\nPressione Enter para continuar...")


def login_problema():
    print("\n❌ Problemas ao fazer login:")
    print("Se este for o seu primeiro acesso ao Portal do Paciente HC, você precisa criar sua conta")
    print("e cadastrar uma senha antes de conseguir fazer login.")
    print("📘 Para aprender como fazer o primeiro acesso passo a passo, acesse:")
    print("👉 www.hcportal.com/primeiroacesso")
    print("-------------")
    print("Verifique se está usando o CPF e a senha correta.")
    print("Se não conseguir acessar, tente redefinir a senha ou verifique se sua conta já está cadastrada.")
    print("📘 Para aprender como redefinir sua senha, acesse:")
    print("👉 www.hcportal.com/redefinirsenha")
    input("\nPressione Enter para continuar...")


def esqueci_senha():
    print("\n🔐 Esqueci minha senha:")
    print(
        "Se você já possui uma conta e esqueceu a senha, clique em “Esqueci minha senha” na tela de login do Portal do Paciente. ")
    print("Depois, informe seu CPF e siga as instruções para redefinir sua senha por e-mail ou SMS.")
    print("🔗 Para saber mais como fazer isso, acesse: www.hcportal.com/senha")
    input("\nPressione Enter para continuar...")


# === Funções de Tutorial ===

def acessar_consultas():
    print("\n📅 Como ver minhas consultas:")
    print("1. Acesse o Portal do Paciente com seu CPF e senha.")
    print("2. No menu principal, clique em 'Teleconsulta'.")
    print("3. Lá você verá a lista com suas consultas agendadas.")
    print("4. No dia da consulta, clique nela para entrar na sala virtual.")
    print("🔗 Saiba mais em: www.hcportal.com/consultas")
    input("\nPressione Enter para continuar...")


def instalar_app():
    print("\n📲 Como instalar o aplicativo:")
    print("1. Acesse a loja de aplicativos do seu celular (Play Store ou App Store).")
    print("2. Busque por 'HC Portal do Paciente'.")
    print("3. Clique em 'Instalar' e aguarde o download.")
    print("4. Após instalado, abra o aplicativo e faça login com seus dados.")
    print("🔗 Saiba mais em: www.hcportal.com/instalacao")
    input("\nPressione Enter para continuar...")


def acessar_portal():
    print("\n🌐 Como acessar o Portal do Paciente:")
    print("1. No navegador, digite: www.hcportal.com e pressione Enter.")
    print("2. Clique em 'Entrar no Portal do Paciente'.")
    print("3. Informe seu CPF e senha para fazer login.")
    print("4. Caso seja seu primeiro acesso, clique em 'Primeiro acesso' e siga os passos.")
    print("🔗 Acesse agora: www.hcportal.com")
    input("\nPressione Enter para continuar...")


# === Outras paginas ===
def chatbot():
    print("\n🤖 Chatbot:")
    print("Assistente virtual para tirar suas dúvidas comuns.")
    input("\nPressione Enter para continuar...")


def calcular_media(notas):
    n1 = float(notas['App'])
    n2 = float(notas['Site'])
    n3 = float(notas['Suporte'])
    media = (n1 + n2 + n3) / 3
    return media


def pesquisa_satisfacao(nome):
    print("\n" + "=" * 50)
    print("📝 Pesquisa de Satisfação".center(50))
    print("=" * 50)
    print(f"\n Nome: {nome}")
    iniciar = input("\nAperte 1 para começar a pesquisa: ")
    if iniciar == "1":
        while True:
            site = float(input("\nDe 0 a 10, qual nota você dá para nosso site? "))
            if (site >= 0 and site <= 10):
                break
            else:
                print("❌Digite uma nota valida!")

        while True:
            app = float(input("\nDe 0 a 10, qual nota você dá para nosso aplicativo? "))
            if (app >= 0 and app <= 10):
                break
            else:
                print("❌Digite uma nota valida!")

        while True:
            suporte = input("\nDe 0 a 10, qual nota você dá para nosso suporte? ")
            if (suporte >= 0 and suporte <= 10):
                break
            else:
                print("❌Digite uma nota valida!")
        notas = {
            'App': app,
            'Site': site,
            'Suporte': suporte,
        }
        print("\n✅ Obrigado por responder à pesquisa!")
        print("----------------------------------------------")
        print("Essas foram suas notas para pesquisa:")
        for k, v in notas.items():
            print(f"{k}: {v}")
        print(f"A sua nota média foi {calcular_media(notas)}")
    else:
        print("Pesquisa cancelada.")
    input("\nPressione Enter para continuar...")


def quem_somos():
    print("\n" + "=" * 50)
    print("👤 Quem Somos".center(50))
    print("=" * 50)
    print("Julia Corrêa e Souza de Altino")
    print("RM 564870")
    print("--------------------------------------")
    print("Matheus Borges Sansão Silva")
    print("RM 562896")
    print("--------------------------------------")
    input("\nPressione Enter para continuar...")


def contato(email):
    print("\n" + "=" * 50)
    print("📞 Contato:".center(50))
    print("=" * 50)
    print("✉️  Suporte: suporte.appportal@hc.fm.usp.br")
    print("📘 Facebook: facebook.com/redelucymontoro")
    print("📸 Instagram: @redelucymontoro")
    print("--------------")
    print("Se preferir podemos enviar um email para:")
    print(email)
    input("\nPressione Enter para continuar...")


def area_paciente():
    print("\n👤 Área do Paciente:")
    print("Para acessar a area do paciene baixe o aplicativo.")
    input("\nPressione Enter para continuar...")


# === Main ===
def main():
    while True:
        mostrar_menu_principal(usuario)
        opcao = input("\nEscolha uma opção: ")
        match opcao:
            case "1":
                menu_ajuda()
            case "2":
                quem_somos()
            case "3":
                pesquisa_satisfacao(usuario)
            case "4":
                contato(usuario)
            case "5":
                area_paciente()
            case "6":
                print("\n👋 Saindo do sistema... Até mais!")
                break
            case _:
                print("❗ Opção inválida. Tente novamente.")
                input("\nPressione Enter para continuar...")


# Iniciar o programa
main()
