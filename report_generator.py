import pandas as pd
from datetime import datetime

class ReportGenerator:
    def __init__(self, news_data):
        self.news_data = news_data
        self.df = self._prepare_dataframe()

    def _prepare_dataframe(self):
        if not self.news_data:
            return pd.DataFrame()

        df = pd.DataFrame(self.news_data)
        
        # Convert published_at to datetime, handling potential errors
        df["published_at"] = pd.to_datetime(df["published_at"], errors='coerce')
        
        # Drop rows where published_at could not be parsed
        df.dropna(subset=["published_at"], inplace=True)
        
        # Sort by date
        df.sort_values(by="published_at", inplace=True)
        
        return df

    def generate_markdown_report(self, title="Relatório de Análise de Sentimentos de Notícias Financeiras", output_file="sentiment_report.md"):
        if self.df.empty:
            report_content = f"# {title}\n\nNenhum dado de notícia disponível para gerar o relatório.\n"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(report_content)
            print(f"Relatório vazio gerado em {output_file}")
            return

        report_content = f"# {title}\n\n"
        report_content += f"**Data de Geração:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        report_content += "## Resumo Geral\n\n"
        
        total_articles = len(self.df)
        positive_articles = len(self.df[self.df["sentiment"].apply(lambda x: x.get('sentiment') == 'pos')])
        negative_articles = len(self.df[self.df["sentiment"].apply(lambda x: x.get('sentiment') == 'neg')])
        neutral_articles = len(self.df[self.df["sentiment"].apply(lambda x: x.get('sentiment') == 'neu')])

        report_content += f"- Total de Artigos Analisados: {total_articles}\n"
        report_content += f"- Artigos Positivos: {positive_articles} ({(positive_articles/total_articles)*100:.2f}%)\n"
        report_content += f"- Artigos Negativos: {negative_articles} ({(negative_articles/total_articles)*100:.2f}%)\n"
        report_content += f"- Artigos Neutros: {neutral_articles} ({(neutral_articles/total_articles)*100:.2f}%)\n\n"

        report_content += "## Notícias Detalhadas\n\n"
        for index, row in self.df.iterrows():
            sentiment_label = row["sentiment"].get('sentiment', 'N/A')
            sentiment_pos = row["sentiment"].get('pos', 0.0)
            sentiment_neg = row["sentiment"].get('neg', 0.0)
            sentiment_neu = row["sentiment"].get('neu', 0.0)

            report_content += f"### [{row['title']}]({row['link']})\n"
            report_content += f"- **Publicado em:** {row['published_at'].strftime('%Y-%m-%d %H:%M')}\n"
            report_content += f"- **Resumo:** {row['summary']}\n"
            report_content += f"- **Sentimento:** {sentiment_label.capitalize()} (Pos: {sentiment_pos:.2f}, Neg: {sentiment_neg:.2f}, Neu: {sentiment_neu:.2f})\n\n"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"Relatório gerado com sucesso em {output_file}")

# Exemplo de uso (para teste)
if __name__ == "__main__":
    # Dados de exemplo (simulando a saída do scraper e do analisador de sentimentos)
    sample_news_data = [
        {
            'title': 'Ações da TechCorp disparam após resultados positivos',
            'summary': 'Empresa superou as expectativas de lucro no último trimestre.',
            'link': 'http://example.com/techcorp-positive',
            'published_at': '2025-09-30T10:00:00+00:00',
            'content': 'Conteúdo completo da notícia positiva.',
            'sentiment': {'neg': 0.05, 'neu': 0.15, 'pos': 0.80, 'sentiment': 'pos'}
        },
        {
            'title': 'Mercado reage mal a novas políticas econômicas',
            'summary': 'Analistas preveem queda nos investimentos.',
            'link': 'http://example.com/market-negative',
            'published_at': '2025-09-29T14:30:00+00:00',
            'content': 'Conteúdo completo da notícia negativa.',
            'sentiment': {'neg': 0.70, 'neu': 0.20, 'pos': 0.10, 'sentiment': 'neg'}
        },
        {
            'title': 'Fusão de empresas X e Y anunciada sem grandes impactos',
            'summary': 'Acordo deve ter efeito neutro no curto prazo.',
            'link': 'http://example.com/merger-neutral',
            'published_at': '2025-10-01T09:00:00+00:00',
            'content': 'Conteúdo completo da notícia neutra.',
            'sentiment': {'neg': 0.10, 'neu': 0.80, 'pos': 0.10, 'sentiment': 'neu'}
        },
        {
            'title': 'Inflação sob controle, diz Banco Central',
            'summary': 'Expectativas de mercado melhoram após comunicado oficial.',
            'link': 'http://example.com/inflation-positive',
            'published_at': '2025-09-28T11:00:00+00:00',
            'content': 'Conteúdo completo da notícia sobre inflação.',
            'sentiment': {'neg': 0.10, 'neu': 0.30, 'pos': 0.60, 'sentiment': 'pos'}
        }
    ]

    report_gen = ReportGenerator(sample_news_data)
    report_gen.generate_markdown_report()

