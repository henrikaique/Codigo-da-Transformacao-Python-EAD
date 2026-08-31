import os
import shutil

    #o primeiro def tem o intuito de realizar o backup do modulo 06
def realizar_backup_modulo06(): 
     
    pasta_origem = os.path.dirname(os.path.abspath(__file__))

    # Aqui diz sobre onde será o destino do backup de arquivos que o def está fazendo
    pasta_destino = os.path.join(pasta_origem, "backup_arquivos")
    
    # Os prints sinalizam a pasta origem e a pasta destino
    print(f" Pasta de Origem: {pasta_origem}")
    print(f" Pasta de Destino: {pasta_destino}\n")

    # Essa parte do codigo serve para que a pasta destino seja criada mesmo que não exista.
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Diretório de destino criado em: '{pasta_destino}'")

    # Esta parte fala sobre todos os iten dentro da pasta modulo 6
    itens = os.listdir(pasta_origem)
    
    #Está parte constroí os caminhos completos de arquivos ou pastas 
    for item in itens:
        caminho_item_origem = os.path.join(pasta_origem, item)
        caminho_item_destino = os.path.join(pasta_destino, item)

        
        if os.path.isfile(caminho_item_origem):
            # Opcional: Ignorar o próprio script de backup para não duplicá-lo na pasta backup
            if item == os.path.basename(__file__):
                continue

            shutil.copy2(caminho_item_origem, caminho_item_destino)
            print(f"✓ Copiado: {item} -> backup_arquivos/")

    print("\n Backup do Módulo 06 concluído com sucesso!")


if __name__ == "__main__":
    realizar_backup_modulo06()