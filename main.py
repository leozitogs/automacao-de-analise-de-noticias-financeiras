from scraper import MarketauxScraper
from sentiment_analyzer import SentimentAnalyzer
from report_generator import ReportGenerator
import os

class FinancialNewsSentimentSystem:
    def __init__(self, api_key):
        self.scraper = MarketauxScraper(api_key)
        self.sentiment_analyzer = SentimentAnalyzer()
        self.news_data = []

    def run_analysis(self, keyword=None, symbols=None, language='pt'):
        print("\n--- Coletando Notícias ---")
        raw_news = self.scraper.scrape_news(keyword=keyword, symbols=symbols, language=language)
        
        if not raw_news:
            print("Nenhuma notícia encontrada para análise.")
            return

        print(f"Encontradas {len(raw_news)} notícias. Iniciando análise de sentimentos...")
        processed_news = []
        for article in raw_news:
            sentiment_scores = self.sentiment_analyzer.analyze_sentiment(article.get('content', ''))
            article["sentiment"] = sentiment_scores
            processed_news.append(article)
        
        self.news_data = processed_news
        print("Análise de sentimentos concluída.")

    def generate_report(self, output_filename="sentiment_report.md", title="Relatório de Análise de Sentimentos de Notícias Financeiras"):
        if not self.news_data:
            print("Nenhum dado de notícia processado para gerar o relatório.")
            # Gerar um relatório vazio ou com mensagem de erro
            report_gen = ReportGenerator([])
            report_gen.generate_markdown_report(title=title, output_file=output_filename)
            return

        print("\n--- Gerando Relatório ---")
        report_gen = ReportGenerator(self.news_data)
        report_gen.generate_markdown_report(title=title, output_file=output_filename)
        print(f"Relatório salvo em {output_filename}")

# Exemplo de uso
if __name__ == "__main__":
    # Certifique-se de substituir pela sua chave de API real
    API_KEY = os.getenv("MARKETAUX_API_KEY", "D82LmIRJrzKE658U87QvsYvjvMEX6a7CTX6hMX4J") 
    
    if API_KEY == "D82LmIRJrzKE658U87QvsYvjvMEX6a7CTX6hMX4J":
        print("AVISO: Usando a chave de API padrão. Para uso em produção, defina a variável de ambiente MARKETAUX_API_KEY.")

    system = FinancialNewsSentimentSystem(API_KEY)

    # Exemplo 1: Buscar notícias sobre "inflação" em português e gerar relatório
    system.run_analysis(keyword="inflação", language='pt')
    system.generate_report(output_filename="relatorio_inflacao.md", title="Relatório de Sentimentos sobre Inflação")

    # Exemplo 2: Buscar notícias sobre "TSLA" e "AAPL" em inglês e gerar relatório
    system.run_analysis(symbols=["TSLA", "AAPL"], language='en')
    system.generate_report(output_filename="relatorio_acoes.md", title="Relatório de Sentimentos sobre Ações (TSLA, AAPL)")

