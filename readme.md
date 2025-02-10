# Precificação de Veículos com Teoria dos Jogos

Este projeto aplica a teoria dos jogos, especificamente o **Modelo de Bertrand** e o **Equilíbrio de Nash**, para otimizar a precificação de veículos SUVs em cenários competitivos. O objetivo é fornecer uma ferramenta prática para empresas e profissionais tomarem decisões estratégicas de preços.

---

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

/veiculos-pricing-game-theory
│
├── /data # Dados brutos ou processados
│ └── custos.csv # Exemplo: dados de custos marginais
│
├── /models # Códigos de modelagem teórica
│ ├── bertrand.py # Modelo de Bertrand básico
│ └── nash.py # Modelos de equilíbrio de Nash
│
├── /src # Código-fonte principal
│ ├── app.py # Aplicação Streamlit
│ ├── utils.py # Funções auxiliares (cálculos, gráficos)
│ └── config.py # Parâmetros globais (elasticidade, demanda base)
│
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto


---

## Descrição dos Arquivos

### **1. `models/bertrand.py`**
Este arquivo contém a implementação do **Modelo de Bertrand**, que é usado para determinar o preço ótimo de um produto em um mercado competitivo. Ele inclui funções para:
- Calcular a demanda com base no preço próprio e no preço dos concorrentes.
- Calcular o lucro com base no preço, custo marginal e demanda.
- Otimizar o preço para maximizar o lucro.

**Conexões:**
- É usado no `app.py` para calcular o preço ótimo e o lucro máximo.
- Depende dos parâmetros globais definidos em `config.py`.

---

### **2. `models/nash.py`**
Este arquivo estende o modelo básico para simular o **Equilíbrio de Nash** em um cenário com múltiplos concorrentes. Ele inclui funções para:
- Calcular a demanda considerando o preço médio dos concorrentes.
- Encontrar o equilíbrio de Nash iterativamente, onde nenhuma empresa tem incentivo para mudar seu preço.

**Conexões:**
- É usado no `app.py` para simular o equilíbrio de preços entre várias empresas.
- Depende dos parâmetros globais definidos em `config.py`.

---

### **3. `src/utils.py`**
Este arquivo contém funções utilitárias para:
- Carregar dados de arquivos CSV (ex: custos marginais).
- Plotar gráficos de preço vs. lucro para análise visual.

**Conexões:**
- É usado no `app.py` para carregar dados e gerar gráficos.
- Pode ser estendido para incluir outras funcionalidades de análise.

---

### **4. `src/config.py`**
Este arquivo define **parâmetros globais** usados em todo o projeto, como:
- Elasticidade-preço da demanda.
- Demanda base (quantidade de veículos vendidos sem variação de preço).
- Custo marginal padrão.

**Conexões:**
- É importado em `app.py`, `bertrand.py` e `nash.py` para acessar os parâmetros globais.
- Facilita a manutenção e ajuste dos valores.

---

### **5. `src/app.py`**
Este é o arquivo principal que implementa a **interface gráfica** usando o Streamlit. Ele permite que o usuário:
- Defina parâmetros como custo marginal, número de concorrentes e preços concorrentes.
- Calcule o preço ótimo que maximiza o lucro.
- Simule o equilíbrio de Nash para múltiplos concorrentes.
- Visualize gráficos de sensibilidade (preço vs. lucro).

**Conexões:**
- Importa funções de `bertrand.py` e `nash.py` para realizar cálculos.
- Usa `utils.py` para carregar dados e plotar gráficos.
- Acessa parâmetros globais de `config.py`.

---

### **6. `requirements.txt`**
Este arquivo lista as **dependências** necessárias para executar o projeto. Ele inclui bibliotecas como:
- `streamlit`: Para criar a interface gráfica.
- `numpy` e `pandas`: Para manipulação numérica e de dados.
- `scipy`: Para otimização matemática.
- `matplotlib`: Para plotagem de gráficos.

**Conexões:**
- É usado para instalar as dependências necessárias para todos os arquivos do projeto.

---

### **7. `data/custos.csv`**
Este arquivo contém **dados de exemplo** sobre custos marginais das empresas. Ele pode ser substituído por dados reais coletados de fontes como:
- Relatórios de montadoras.
- Dados de mercado (ex: Sindipeças, ANFAVEA).

**Conexões:**
- Pode ser carregado em `app.py` usando a função `carregar_dados` de `utils.py`.

---

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/veiculos-pricing-game-theory.git
   cd veiculos-pricing-game-theory

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Execute o projeto:
   ```bash
   streamlit run src/app.py
   ```
Acesse a interface no navegador e comece a simular cenários de precificação.


## Como os Arquivos se Conectam

O usuário interage com a interface gráfica em app.py.

app.py usa funções de bertrand.py e nash.py para realizar cálculos de precificação e equilíbrio.

Parâmetros globais são acessados de config.py.

Dados podem ser carregados de data/custos.csv usando utils.py.

Gráficos são gerados com matplotlib através de utils.py.

Todas as dependências são gerenciadas por requirements.txt.
