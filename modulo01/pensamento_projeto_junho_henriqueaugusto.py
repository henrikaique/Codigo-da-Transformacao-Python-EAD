'''
Um Bloco de Comentarios. 
Para explicar o que o código faz, ou para deixar anotações para o programador.
>>projeto industria de automóveis:

>PO( Um sistema de venda de carros facilitando o processo de venda e escolha dos carros)

>QA( um sistema de vendas de carros para facilitar a minha compra e agilizar o processo
>Tech (Como programador: Quero um sistema de vendas para minha açaiteria,
para que eu possa desenvolver um software eficiente e funcional para o negócio.)

>Dev (Como programador: Quero um sistema de vendas para minha industria,
para que eu possa implementar as funcionalidades necessárias para 
atender as necessidades do negócio e dos clientes.)

>UX (Como designer de experiência do usuário: Quero um sistema de vendas para minha Industría de automoveis, para que eu possa criar uma interface interativa
  e agradável para que os usuários possasm ter uma sensação de segurança e profissionalidade, garantindo uma experiência de compra Gratificante.)

>IA (Como analista de dados: Quero um sistema de vendas para minha industría de automoveis, 
para que eu possa analisar os dados de vendas, ajudando a identificar
 alguns padrões de compras e otimizar as estratégias de venda.)


Ciclo de vida do projeto:
1. Planejamento: Definir os requisitos do sistema, identificar as necessidades do negócio e dos clientes, 
e criar um plano de desenvolvimento.
2. Análise: Analisar os requisitos e criar um modelo de dados e um design de sistema.
3. Desenvolvimento: Escrever o código para implementar as funcionalidades do sistema.
4. Testes: Testar o sistema para garantir que ele funcione corretamente e atenda aos requisitos.
5. Implantação: Implantar o sistema em um ambiente de produção e garantir que ele esteja funcionando 
corretamente.
6. Manutenção: Realizar manutenção contínua para corrigir bugs, adicionar novas funcionalidades e garantir 
que o sistema continue atendendo às necessidades do negócio e dos clientes.

>>Criar um aplicativo, sistema em CLI - Command Line Interface, ou seja, um sistema que funcione no terminal, sem interface gráfica.
>>Complementar e implementar o app / sistema em GUI - Graphical User Interface, ou seja, um sistema com interface gráfica, 
para que os usuários possam interagir de forma mais intuitiva e agradável.

'''
# Inicializando as variáveis para o Produto 1 (vazio)
produtos = {
    "p1": {
        "nome": "Porshe 911 Turbo S ",
        "estoque": 5,
        "preco": 8125000.0,
        "ano": "10/12/2026",
        "descricao": "Carro Esportivo que pode te entergar mais de 700 cavalos de potência."
    },
    "p2": {
        "nome": "Chevrolet Corvette C7",
        "estoque": 2,
        "preco": 700000.0,
        "ano": "10/02/2002",
        "descricao": "Carro SuperEsportivo de tração traseira que pode te entregar um motor v8 chegando de 0 a 100 em 3 segundos"
    },
    "p3": {
        "nome": "Nissan Skyline GT-R R34",
        "estoque": 1,
        "preco": 2000000.0,
        "ano": "10/12/2019",
        "descricao": "Carro Esportivo marcado por sua fama e praticidade"
    }
}

# Isso é um comentário de linha única.

while True: 
    print('-' * 48 + '\n')
    print('Bem-vindo ao Sistema de vendas - Industria de Automóveis!\n')
    print('1 - Cadastrar produto')
    print('3 - Realizar venda')
    print('4 - Buscar por ano de fabricação')
    print('5 - Sobre nós')
    print('6 - Agendamento de visitas')
    print('7 - Documentação dos carros')
    print('8 - Formas de pagamento')
    print('9 - Financiamento')
    print('0 - Sair')
    print('\n--------------------------------------\n')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Cadastrando produtos...\n')
    # faça a lógica para cadastrar o produto aqui, 
    ## e somente a inseção dos dados usando input e os tipos de dados.
        if p1_nome == "":
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_ano = input('Digite o ano do produto: ')    
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p1_nome}" cadastrado na vaga 1!')           
        elif p2_nome == "":
                p2_nome = input('Digite o nome do produto: ')
                p2_estoque = int(input('Digite a quantidade em estoque: '))
                p2_preco = float(input('Digite o preço do produto: '))
                p2_ano = input('Digite o ano do produto: ')    
                p2_descricao = input('Digite a descrição do produto: ')
                print(f'\n🎉 Produto "{p2_nome}" cadastrado na vaga 2!')      
        elif p3_nome == "":
            p3_nome = input('Digite o nome do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            p3_ano = input('Digite o ano do produto: ')    
            p3_descricao = input('Digite a descrição do produto: ')
            print(f'\n🎉 Produto "{p3_nome}" cadastrado na vaga 3!')
            
        else:
            print('❌ Sistema cheio! Limite de 3 produtos atingido.')

    elif opcao == '2':
        print('Listando produtos...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":

            print('Nenhum produto cadastrado no sistema ainda.')

        else:
            # Mostra o Produto 1 se ele existir
            if p1_nome != "":
                print(f"Nome: {p1_nome} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.")

                print(f"Ano: {p1_ano} | Descrição: {p1_descricao}")

                print('🔥' * 30)
                
            # Mostra o Produto 2 se ele existir
            if p2_nome != "":

                print(f"Nome: {p2_nome} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.")

                print(f"Ano: {p2_ano} | Descrição: {p2_descricao}")

                print('🔥' * 30)
                
            # Mostra o Produto 3 se ele existir
            if p3_nome != "":

                print(f"Nome: {p3_nome} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.")

                print(f"Ano: {p3_ano} | Descrição: {p3_descricao}")

                print('🔥' * 30)

    elif opcao == '3':
        print('Realizando venda...')

        if p1_nome == "" and p2_nome == "" and p3_nome == "":
            print(f'Não há produtos cadastrados para realizar vendas.')
        else:
            nome_venda = input('Digite o nome do produto que deseja vender: ')
            
            # Testamos o nome digitado contra o Produto 1
            if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p1_nome}' deseja vender? "))
                if qtd_venda <= p1_estoque:
                    p1_estoque -= qtd_venda
                    total = qtd_venda * p1_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p1_nome}: {p1_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p1_estoque}.')
            
            # Testamos contra o Produto 2
            elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p2_nome}' deseja vender? "))
                if qtd_venda <= p2_estoque:
                    p2_estoque -= qtd_venda
                    total = qtd_venda * p2_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p2_nome}: {p2_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p2_estoque}.')
                    
            # Testamos contra o Produto 3
            elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
                qtd_venda = int(input(f"Quantas unidades de '{p3_nome}' deseja vender? "))
                if qtd_venda <= p3_estoque:
                    p3_estoque -= qtd_venda
                    total = qtd_venda * p3_preco
                    print(f'\n✅ Venda realizada! Total: R$ {total:.2f}')
                    print(f'Estoque atual de {p3_nome}: {p3_estoque} unidades.')
                else:
                    print(f'❌ Estoque insuficiente! Temos apenas {p3_estoque}.')
            
            else:
                print('🔥 Erro: Produto não encontrado!')
                
    elif opcao == '4':
        print('sbuscando por ano de produtos...')
        if p1_ano == "" and p2_ano == "" and p3_ano == "":
            print(f'Não há produtos com esses anos para realizar vendas.')
            
        else:
            ano_busca = input('Digite o ano de fabricação dos produtos que deseja buscar: ')
            print(f'Buscando produtos do ano {ano_busca}...')
            
    elif opcao == '5':
        print('Somos a Industria XYZ uma renomada industria que vem trabalhando com a fabricação de automóveis de alta performance e qualidade dês de 1990 com o objetivo de poder dar destaque a modelos incriveis de carros pouco vistos nas ruas atualmente')
        print('Nossos contatos...')
        print('Telefone: (11) 1234-5678')
        print('Email:Xyzcarros@gmail.com')
        
    elif opcao == '6':
        print('Dias disponíveis para agendamento de visitas: Segunda a Quinta-feira, das 9h às 18h.')
        print('Para agendar uma visita, entre em contato conosco pelo telefone (11) 1234-5678 ou pelo email:Xyzcarros@gmail.com')
        

    elif opcao == '7':
        nome_usuario = input('Digite seu nome para começar: ')
        print(f'Olá {nome_usuario}, seja bem-vindo à documentação dos carros!')
        print('Aqui você encontrará informações detalhadas sobre cada modelo de carro disponível em nosso sistema.')
        print('1. Porshe 911 Turbo S: IPVA Médio varia de R$ 58.000,00 a mais de R$ 80.000,00, dependendo do ano do veículo e do estado de registro.')
        print('2. Chevrolet Corvette C7: IPVA médio anual fica entre R$ 20.000 e R$ 35.000, dependendo do ano/modelo e da versão do veículo.')
        print('3. Nissan Skyline GT-R R34: IPVA Médio cerca de R$ 800.000 a mais de R$ 1 milhão.')
        
        
    elif opcao == '8':
        print('Formas de pagamento disponíveis:')
        print('1. Cartão de crédito (Visa, MasterCard)')
        print('2. Boleto bancário')
        print('3. Transferência bancária')
        print('4. Pix')
        print('5. Financiamento (consulte condições na opção 9)')
        
    elif opcao == '9':
        print('Opção de financiamento:')
        print('Oferecemos financiamento para a compra de veículos, com condições especiais e taxas que cabem no seu bolso financiando em até 60 Vezes.')
        print('Para mais informações sobre o financiamento, entre em contato conosco pelo telefone (11) 1234-5678 ou pelo email: Xyzcarros@gmail.com')
        
            
            
            

    elif opcao == '0':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
