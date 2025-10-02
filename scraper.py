import requests
from datetime import datetime

class NewsScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.marketaux.com/v1/news/all"

    def scrape_news(self, keyword=None, symbols=None, language='en'):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")

class MarketauxScraper(NewsScraper):
    def __init__(self, api_key):
        super().__init__(api_key)

    def scrape_news(self, keyword=None, symbols=None, language='en'):
        print(f"Buscando notícias via Marketaux API...")
        params = {
            "api_token": self.api_key,
            "language": language,
            "filter_entities": "true",
            "group_similar": "true",
            "limit": 100 # Adjust limit as needed, based on your plan
        }

        if keyword:
            params["search"] = keyword
        if symbols:
            params["symbols"] = ",".join(symbols)

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            articles_data = []

            for article in data.get("data", []):
                published_at = None
                if article.get("published_at"):
                    try:
                        # Marketaux returns ISO format directly
                        published_at = datetime.fromisoformat(article["published_at"].replace('Z', '+00:00')).isoformat()
                    except ValueError:
                        pass

                articles_data.append({
                    'title': article.get('title', 'N/A'),
                    'summary': article.get('description', 'N/A'),
                    'link': article.get('url', 'N/A'),
                    'published_at': published_at,
                    'content': article.get('snippet', 'N/A') + " " + article.get('text', '') # Combine snippet and text for content
                })
            return articles_data
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar notícias da Marketaux API: {e}")
            return []

# Exemplo de uso (para teste)
if __name__ == "__main__":
    # Substitua 'SUA_API_KEY_AQUI' pela chave de API real
    API_KEY = "D82LmIRJrzKE658U87QvsYvjvMEX6a7CTX6hMX4J"
    scraper = MarketauxScraper(API_KEY)
    
    print("\n--- Teste com palavra-chave 'inflação' ---")
    news_inflation = scraper.scrape_news(keyword="inflação", language='pt')
    for article in news_inflation:
        print(f"Título: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Publicado em: {article['published_at']}")
        print(f"Resumo: {article['summary']}")
        print(f"Conteúdo: {article['content'][:200]}...") # Limita para não imprimir muito
        print("---")
    print(f"Total de notícias encontradas sobre inflação: {len(news_inflation)}")

    print("\n--- Teste com símbolos de ações (TSLA, AAPL) ---")
    news_stocks = scraper.scrape_news(symbols=["TSLA", "AAPL"], language='en')
    for article in news_stocks:
        print(f"Título: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Publicado em: {article['published_at']}")
        print(f"Resumo: {article['summary']}")
        print(f"Conteúdo: {article['content'][:200]}...") # Limita para não imprimir muito
        print("---")
    print(f"Total de notícias encontradas sobre ações: {len(news_stocks)}")

