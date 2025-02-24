# Dashboard de Unidades Básicas de Saúde (UBS)

Este projeto é um **dashboard interativo** desenvolvido com **Streamlit** para visualizar a frequência das **Unidades Básicas de Saúde (UBS)** por estado no Brasil.

## 🏗️ Funcionalidades
- **Gráfico de barras** interativo mostrando a frequência de UBS por estado.
- **Filtro** para visualizar dados de estados específicos.
- **Visualização de dados** filtrados diretamente na interface.

## 📂 Estrutura do Projeto
```
├── ubs_dashboard.py  # Código do dashboard em Streamlit
├── ubs_atualizado.csv # Arquivo de dados atualizado
├── requirements.txt  # Dependências necessárias
└── README.md  # Documentação do projeto
```

## 🚀 Como Executar
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/ubs-dashboard.git
cd ubs-dashboard
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv env
source env/bin/activate  # Para Linux/Mac
env\Scripts\activate  # Para Windows
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a aplicação
```bash
streamlit run ubs_dashboard.py
```

## 📦 Dependências
As principais bibliotecas utilizadas no projeto são:
- `streamlit` → Interface do dashboard
- `pandas` → Manipulação de dados
- `plotly` → Visualização de gráficos interativos
