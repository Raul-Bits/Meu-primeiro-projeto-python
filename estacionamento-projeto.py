n = int(input('Vagas - '))
m = int(input('Clientes - '))
lista_vi = []
vagas_disponiveis = 0

for i in range (m):
    vi = int(input('Vaga - '))
    if vi not in lista_vi:
        vagas_disponiveis += 1
        lista_vi.append(vi)
print('Vagas disponíveis:',vagas_disponiveis,'\nvagas fixas:',lista_vi) 
