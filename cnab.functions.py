def extrair_codigo_ocorrencia(linha):
    codigo_ocorrencia = linha[108:110]
    return codigo_ocorrencia

def processar_arquivo_cnab(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas:
            # Verifique se a linha é válida para o formato CNAB400
            print(len(linha))
            if len(linha) == 400:
                codigo_ocorrencia = extrair_codigo_ocorrencia(linha)
                print(f'Código de Ocorrência: {codigo_ocorrencia}')
            else:
                print("Registro inválido!")
        
if __name__ == '__main__':
    # Substitua 'caminho/do/arquivo.txt' pelo caminho do seu arquivo CNAB
    arquivo_cnab = 'files/CB271001.REM'
    processar_arquivo_cnab(arquivo_cnab)
