import random
from datetime import datetime

try:
    from colorama import Fore, Style, init
except ImportError:
    class _ColorDummy:
        def __getattr__(self, name):
            return ""

    Fore = _ColorDummy()
    Style = _ColorDummy()

    def init(*args, **kwargs):
        return None

try:
    from faker import Faker
except ImportError:
    class Faker:
        def __init__(self, locale=None):
            self._nomes = [
                "Ana Souza",
                "Carlos Lima",
                "Beatriz Costa",
                "Davi Pereira",
                "Laura Santos",
                "João Oliveira",
                "Maria Silva",
                "Pedro Rocha",
            ]

        def name(self):
            return random.choice(self._nomes)

        def phone_number(self):
            return f"({random.randint(11, 99)}) {random.randint(90000, 99999)}-{random.randint(1000, 9999)}"

        def email(self):
            nome = random.choice(self._nomes).lower().replace(" ", ".")
            dominio = random.choice(["gmail.com", "outlook.com", "yahoo.com.br"])
            return f"{nome}@{dominio}"


init(autoreset=True)

# Inicializa o gerador de dados fakes
fake = Faker("pt_BR")

# lista de materias para as notas do boletim
MATERIAS = [
    "Matemática",
    "Português",
    "História",
    "Geografia",
    "Ciências",
    "Inglês",
]

 #essa def cria os dados fakes de um aluno, nome, idade , telefone, e email.
def gerar_dados_aluno():
   
    return {
        "nome": fake.name(),
        "idade": random.randint(14, 18),
        "telefone": fake.phone_number(),
        "email": fake.email(),
    }

 # essa def é uma forma de preencher as notas de forma manual
def obter_notas_manuais():
    
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

 #  essa def gera notas aleatorias.
def gerar_notas_aleatorias():
    
    boletim = {}
    for materia in MATERIAS:
        nota = round(random.uniform(3.0, 10.0), 1)
        boletim[materia] = nota
    return boletim

 # essa def calcula a media.
def calcular_media(boletim):
   
    return sum(boletim.values()) / len(boletim)

 # essa def exibe o booletim ficiticio com notas e dados
def emitir_boletim():
    
    aluno = gerar_dados_aluno()

    print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO E EMISSÃO DE BOLETIM ===")
    print(Fore.YELLOW + "1. Inserir notas MANUALMENTE")
    print(Fore.YELLOW + "2. Gerar notas ALEATORIAMENTE")

    # asopções de escolha.
    opcao = input("\nEscolha uma opção (1 ou 2): ").strip()

    if opcao == "1":
        boletim = obter_notas_manuais()
    elif opcao == "2":
        print(Fore.GREEN + "\nGerando notas aleatórias...")
        boletim = gerar_notas_aleatorias()
    else:
        print(Fore.RED + "Opção inválida! Gerando notas aleatórias...")
        boletim = gerar_notas_aleatorias()

    #resultados
    media = calcular_media(boletim)
    data_emissao = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    # Pàrte para definir cor e status do boletim

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
