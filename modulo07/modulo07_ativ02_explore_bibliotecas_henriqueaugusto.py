import random
from datetime import datetime
from colorama import Fore, Style, init
from faker import Faker

# Inicializa o colorama (necessário no Windows para as cores funcionarem)
init(autoreset=True)

# Inicializa o gerador de dados fictícios em português
fake = Faker("pt_BR")

# Lista de matérias padrão do sistema
MATERIAS = [
    "Matemática",
    "Português",
    "História",
    "Geografia",
    "Ciências",
    "Inglês",
]


def gerar_dados_aluno():
    """Gera dados pessoais fictícios para o aluno."""
    return {
        "nome": fake.name(),
        "idade": random.randint(14, 18),
        "telefone": fake.phone_number(),
        "email": fake.email(),
    }


def obter_notas_manuais():
    """Solicita ao usuário que insira manualmente as notas de cada matéria."""
    boletim = {}
    print(Fore.CYAN + "\n--- DIGITAÇÃO DAS NOTAS ---")
    for materia in MATERIAS:
        while True:
            try:
                nota = float(input(f"Digite a nota de {materia} (0 a 10): "))
                if 0 <= nota <= 10:
                    boletim[materia] = nota
                    break
                else:
                    print(
                        Fore.RED
                        + "Nota inválida! Por favor, digite um valor entre 0 e 10."
                    )
            except ValueError:
                print(
                    Fore.RED + "Entrada inválida! Digite um número válido."
                )
    return boletim


def gerar_notas_aleatorias():
    """Gera notas aleatórias entre 3.0 e 10.0 para cada matéria."""
    boletim = {}
    for materia in MATERIAS:
        nota = round(random.uniform(3.0, 10.0), 1)
        boletim[materia] = nota
    return boletim


def calcular_media(boletim):
    """Calcula a média aritmética simples de todas as matérias."""
    return sum(boletim.values()) / len(boletim)


def emitir_boletim():
    """Função principal que coordena a execução do programa."""
    aluno = gerar_dados_aluno()

    print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO E EMISSÃO DE BOLETIM ===")
    print(Fore.YELLOW + "1. Inserir notas MANUALMENTE")
    print(Fore.YELLOW + "2. Gerar notas ALEATORIAMENTE")

    # Escolha do modo de operação
    opcao = input("\nEscolha uma opção (1 ou 2): ").strip()

    if opcao == "1":
        boletim = obter_notas_manuais()
    else:
        print(Fore.GREEN + "\nGerando notas aleatórias...")
        boletim = gerar_notas_aleatorias()

    # Processamento dos resultados
    media = calcular_media(boletim)
    data_emissao = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    # Definição do status e cor correspondente
    if media >= 6.0:
        status = "APROVADO"
        cor_status = Fore.GREEN
    else:
        status = "REPROVADO"
        cor_status = Fore.RED

    # Exibição estilizada do boletim
    print("\n" + Fore.BLUE + "=" * 50)
    print(
        Fore.BLUE
        + Style.BRIGHT
        + "                BOLETIM ESCOLAR                   "
    )
    print(Fore.BLUE + "=" * 50)
    print(Fore.WHITE + f"Data de Emissão: {data_emissao}")
    print(Fore.BLUE + "-" * 50)

    print(Fore.YELLOW + Style.BRIGHT + "DADOS DO ALUNO:")
    print(Fore.WHITE + f"Nome:     {aluno['nome']}")
    print(Fore.WHITE + f"Idade:    {aluno['idade']} anos")
    print(Fore.WHITE + f"Telefone: {aluno['telefone']}")
    print(Fore.WHITE + f"E-mail:   {aluno['email']}")
    print(Fore.BLUE + "-" * 50)

    print(Fore.YELLOW + Style.BRIGHT + "DESEMPENHO POR MATÉRIA:")
    for materia, nota in boletim.items():
        # Destaque em verde para nota individual >= 6, ou vermelho caso contrário
        cor_nota = Fore.GREEN if nota >= 6.0 else Fore.RED
        print(f"• {materia:<12}: {cor_nota}{nota:.1f}{Style.RESET_ALL}")

    print(Fore.BLUE + "-" * 50)
    print(
        Fore.WHITE
        + f"Média Geral: {Style.BRIGHT}{media:.2f}{Style.RESET_ALL}"
    )
    print(f"Status:      {cor_status}{Style.BRIGHT}{status}{Style.RESET_ALL}")
    print(Fore.BLUE + "=" * 50)


# Ponto de entrada do programa
if __name__ == "__main__":
    emitir_boletim()
