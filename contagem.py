import matplotlib.pyplot as plt
ls = [["0"]] # lista de ritmos começando com 0
p = [] # lista de quantidade de ritmos por tamanho
t = 0 # total de ritmos
b = 3 # base do ritmo
x = 12 # tamanho máximo do ritmo a ser explorado

def plot(arr):
    y_values = arr  # Replace this with your array
    x_values = range(len(y_values))  # This creates a sequence of indices for the x-axis

    # Create the plot
    plt.plot(x_values, y_values, marker='o')  # 'o' creates dots at each data point

    # Optionally, you can add labels and a title
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('1D Array Plot')

    # Show the plot
    plt.show()
def C(i, n, f): # Checa se pode-se adicionar f a sequencia
    if str(i[-1]+str(f)) not in i[:-1]:
        n.append(i+str(f))
def R(ls, b): # retorna as sequencias que podem ser criadas adicionando mais um ao comprimento
    n = []
    for i in ls[-1]:
        for j in range(b):
            C(i, n, j)
    ls.append(n)
    return n

for i in range(x): # calcula todas as sequencias ate o comprimento x+1
    R(ls,b)
for i in range(x): # concatena as informações
    p.append(len(ls[i+1])*(b-1))
    t+=p[-1]
    print(p[-1])

print(ls)
plot(p)
import json
with open('minha_lista.json', 'w') as file:
    json.dump(ls, file)