Amostragem = 5
NumeroTratamentosPosteriores = 0
NumeroTratamentosPosteriores = int(input(f"Digite o número de vezes que você ficou doentes nos últimos {Amostragem} anos: "))
ValoresTratamentos = list()
for c in range(NumeroTratamentosPosteriores):
    ValoresTratamentos.append(float(input(f"Digite o valor do tratamento {c+1} R$")))
print(f"Você gastou em média R${round(sum(ValoresTratamentos)/60,2)} por mês com tratamentos médicos/remédios/exames.")
print(f"Isso significa que se a tendência futura for parecida com a amostragem informada, então não compensará um plano de saúde que exceda esse valor mensal.")

