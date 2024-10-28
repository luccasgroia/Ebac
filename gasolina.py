
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo 'gasolina.csv'
data = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
plt.figure(figsize=(10, 5))
plt.plot(data['dia'], data['venda'], marker='o') # Changed data['preco'] to data['venda']
plt.xlabel('Dia')
plt.ylabel('Preço da Gasolina')
plt.title('Variação do Preço da Gasolina ao Longo dos Dias')
plt.grid(True)

# Salvar o gráfico no arquivo 'gasolina.png'
plt.savefig('gasolina.png')
