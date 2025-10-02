from pysentimiento import create_analyzer

class SentimentAnalyzer:
    def __init__(self):
        # Inicializa o analisador de sentimentos para português
        self.analyzer = create_analyzer(task="sentiment", lang="pt")

    def analyze_sentiment(self, text):
        if not text or not isinstance(text, str):
            return {
                'neg': 0.0,
                'neu': 0.0,
                'pos': 0.0,
                'sentiment': 'neutral' # Adiciona um campo de sentimento padrão
            }

        # pysentimiento retorna um objeto que contém os resultados
        result = self.analyzer.predict(text)
        
        # O resultado contém a label (NEG, NEU, POS) e as probabilidades
        # Vamos mapear para o formato anterior para consistência, se possível
        # ou retornar o formato nativo do pysentimiento
        
        # Para este projeto, vamos retornar a label principal e as probabilidades
        # para negativo, neutro e positivo.
        
        sentiment_label = result.output # 'NEG', 'NEU', 'POS'
        probabilities = result.probas # Dicionário com probabilidades

        # Mapeando para um formato similar ao VADER para manter a estrutura, se desejado
        # Ou podemos simplesmente retornar o objeto 'result' diretamente
        mapped_sentiment = {
            'neg': probabilities.get('NEG', 0.0),
            'neu': probabilities.get('NEU', 0.0),
            'pos': probabilities.get('POS', 0.0),
            'sentiment': sentiment_label.lower() # Converte para minúsculas para consistência
        }
        return mapped_sentiment

# Exemplo de uso (para teste)
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()

    texts_to_analyze = [
        "As ações da empresa subiram significativamente hoje devido a um excelente relatório de lucros.",
        "O mercado está em baixa, com investidores preocupados com a inflação crescente.",
        "A empresa anunciou novos produtos, mas o impacto no mercado ainda é incerto.",
        "Este é um texto neutro sem emoções fortes.",
        "Apesar dos desafios, a empresa demonstrou resiliência e potencial de crescimento."
    ]

    for text in texts_to_analyze:
        sentiment_scores = analyzer.analyze_sentiment(text)
        print(f"Texto: {text}")
        print(f"Sentimento: {sentiment_scores['sentiment']} (Negativo={sentiment_scores['neg']:.2f}, Neutro={sentiment_scores['neu']:.2f}, Positivo={sentiment_scores['pos']:.2f})")
        print("---")

