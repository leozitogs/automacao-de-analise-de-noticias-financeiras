# Sistema de Automação de Análise de Sentimentos de Notícias Financeiras

Este projeto implementa um sistema de automação em Python para coletar notícias financeiras, realizar análise de sentimentos sobre elas e gerar relatórios detalhados. Utiliza Programação Orientada a Objetos (POO) para uma estrutura modular e reutilizável, sendo ideal para demonstrar habilidades em web scraping, Processamento de Linguagem Natural (PLN) e geração de relatórios.

## Funcionalidades

- **Coleta de Notícias**: Utiliza a API Marketaux para buscar notícias financeiras com base em palavras-chave ou símbolos de ações.
- **Análise de Sentimentos**: Emprega a biblioteca `pysentimiento` para determinar o sentimento (positivo, negativo, neutro) de cada notícia em português.
- **Geração de Relatórios**: Cria relatórios em formato Markdown, resumindo a análise de sentimentos e listando as notícias detalhadas.

## Estrutura do Projeto

```
. 
├── main.py
├── scraper.py
├── sentiment_analyzer.py
├── report_generator.py
├── requirements.txt
└── README.md
```

- `main.py`: Ponto de entrada do sistema, orquestra a coleta, análise e geração de relatórios.
- `scraper.py`: Módulo responsável pela interação com a API de notícias (Marketaux).
- `sentiment_analyzer.py`: Módulo que encapsula a lógica de análise de sentimentos usando `pysentimiento`.
- `report_generator.py`: Módulo para formatar e gerar os relatórios em Markdown.
- `requirements.txt`: Lista todas as dependências do projeto.
- `README.md`: Este arquivo, contendo a documentação do projeto.

## Como Usar

### 1. Pré-requisitos

- Python 3.8+
- Chave de API da Marketaux (obtenha uma em [https://www.marketaux.com/](https://www.marketaux.com/))

### 2. Configuração do Ambiente

1.  **Clone o repositório (ou crie os arquivos manualmente):**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <nome_do_repositorio>
    ```

2.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua Chave de API da Marketaux:**

    Defina a sua chave de API como uma variável de ambiente. Isso é crucial para a segurança e o funcionamento do scraper.

    ```bash
    export MARKETAUX_API_KEY="SUA_CHAVE_AQUI" # Linux/macOS
    # No Windows (CMD):
    # set MARKETAUX_API_KEY="SUA_CHAVE_AQUI"
    # No Windows (PowerShell):
    # $env:MARKETAUX_API_KEY="SUA_CHAVE_AQUI"
    ```

    Alternativamente, você pode substituir `"D82LmIRJrzKE658U87QvsYvjvMEX6a7CTX6hMX4J"` diretamente no arquivo `main.py` (linha 58), mas a abordagem com variável de ambiente é mais segura e recomendada.

### 3. Executando o Sistema

Para executar o sistema e gerar relatórios, utilize o arquivo `main.py`.

**Exemplo 1: Análise de notícias sobre "inflação" em português**

```bash
python3 main.py
```

Este comando irá:
- Coletar notícias relacionadas a "inflação" em português.
- Analisar o sentimento de cada notícia.
- Gerar um relatório chamado `relatorio_inflacao.md`.

**Exemplo 2: Análise de notícias sobre ações específicas (TSLA, AAPL) em inglês**

O `main.py` já inclui um exemplo para isso. Ao executar `python3 main.py`, ele também gerará um relatório `relatorio_acoes.md`.

Você pode modificar o bloco `if __name__ == "__main__":` em `main.py` para personalizar as buscas e os relatórios.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, correção de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor

Leonardo Gonçalves Sobral

