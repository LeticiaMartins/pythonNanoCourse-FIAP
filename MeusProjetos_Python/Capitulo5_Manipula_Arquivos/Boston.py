#YEAR > Ano do dado
#MONTH > Mês do dado
#LOGAN_PASSENGERS > Quantidade de passageiros, internacionais e domésticos, que passaram pelo aeroporto de Logan.
#LOGAN_INTL_FLIGHTS > Total de voos internacionais que partiram do aeroporto de Logan.
#HOTEL_OCCUP_RATE > Porcentagem de vagas ocupadas nos hotéis de Boston.
#HOTEL_AVG_DAILY_RATE > Média da diária, em dólar, de um hotel em Boston.
#TOTAL_JOBS,UNEMP_RATE > Porcentagem de desempregados em Boston.

###############################################
#Perguntas:
# - Qual o total de voos internacionais que partiram do aeroporto de Logan no
# ano de 2014?
# - Quando (mês/ano) ocorreu o maior trânsito de passageiros no aeroporto de
# Logan?
# - Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano
# que for especificado pelo usuário?
# - Qual o mês que possui a maior média da diária de um hotel, com base no
# ano especificado pelo usuário?
##############################################

with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    ano_usuario = input("Qual ano deseja pesquisar? ")
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        total_voos = total_voos + float(lista[3])
        if float(lista[2])>float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario==lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            if float(lista[5])>float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
    print("O total de voos é:", total_voos)
    print("O mês/ano de maior movimento no aeroporto foi:", str(mes),"/",str(ano))
    print("O total de passageiros do ano", ano_usuario, "foi de", total_passageiros)
    print("O mês do ano", ano_usuario, "com maior média para diária de hotel foi", mes_maior_diaria)