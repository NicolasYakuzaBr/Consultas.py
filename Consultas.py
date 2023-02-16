from brasilapy import BrasilAPI

#https://brasilapi.com.br/docs

client = BrasilAPI()


while True: 
    print('Consulta de Banco, Cep, Cnpj, DDD, Feriado e Cidades do estado')

    print('[1] Banco')
    print('[2] Cep')
    print('[3] Cnpj')
    print('[4] DDD')
    print('[5] Feriado')
    print('[6] Cidades')

    opção = int(input('Número: '))
    
    if opção == 1:
        banco = client.get_bank(input('Conta Bancária: '))
        print(f'Resultado da pesquisa sobre a conta bancária: {banco}')

    if opção == 2:    
        cep = client.get_cep(cep=(input('Cep: ')))
        print(f'Resultado do Cep: {cep}')

    if opção == 3:
        cnpj = client.get_cnpj(cnpj=(input('Cnpj: ')))
        print(f'Resultado do Cnpj: {cnpj}')

    if opção == 4:
        ddd = client.get_ddd(ddd=(input('DDD: ')))
        print(f'Resultado do DDD: {ddd}')

    if opção == 5:
        feriado = client.get_feriados(year=(input('Digite o ano para ficar por dentro dos feriados: ')))
        print(f'Feriados irão ocorrer em...: {feriado}')

    if opção == 6:
        cidade = client.get_ibge_municipios(state_uf=(input('Digite a sigla do estado para listar as cidades: ')))
        print(f'Cidades do estado: {cidade}')

    if opção == 7:
        break








