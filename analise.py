import pandas as pd
import matplotlib.pyplot as plt

# Criando dados de exemplo (simulando uma planilha de  testes)
dados = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'testes_realizados': [120, 135, 98, 160, 145, 170],
    'testes_aprovados': [110, 128, 85, 152, 138, 165],
    'testes_reprovados': [10, 7, 13, 8, 7, 5]
}

# Criando DataFrame (tabela de dados)
df = pd.DataFrame(dados)

# Calculando a taxa de aprovação
df['taxa_aprovacao'] = (df['testes_aprovados'] / df['testes_realizados'] * 100).round(2)

# Mostrando a tabela no terminal 
print("=== RELATÓRIO DE TESTES ===")
print(df)
print(f"\nMédia de aprovação: {df['taxa_aprovacao'].mean():.2f}%")
print(f"Melhor mês: {df.loc[df['taxa_aprovacao'].idxmax(), 'mes']}")

#Geranndo o gráfico para visualização dos dados
plt.figure(figsize=(10, 6))
plt.plot(df['mes'], df['testes_realizados'], color='#dc3545', marker='o', label='Aprovados')
plt.plot(df['mes'], df['testes_reprovados'], color='#707070', marker='o', label='Reprovados')
plt.title('Relatório de Testes por Mês', fontsize=16)
plt.xlabel('Mês')
plt.ylabel('Quantidade')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('relatorio.png')
plt.show()
print("\nGráfico salvo como relatorio.png!")