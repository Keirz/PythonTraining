print("Digite o tempo gasto na viagem e a velocidade média durante a viagem em ordem:" )
dados = list(map(int, input().split()))
tempo, velocidade = dados
distancia = tempo*velocidade
litros_usados = distancia/12
print('A distancia percorrida é de: ',  distancia)
print('A quantidade de litros usada é de: ', litros_usados)
print('O tempo gasto na viagem é de: ', tempo)
