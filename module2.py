import nltk

from nltk.sentiment import SentimentIntensityAnalyzer
from module1 import FecthReview

nltk.download('vader_lexicon')

class Sentiment:    
    def review_sentiment(self,link):
        sia = SentimentIntensityAnalyzer()

        review = FecthReview(link)
        reviews = review.fetch()

        for rvw in reviews:
            print('---------------------')
            print(rvw)
            polar_score = sia.polarity_scores(rvw)
            computed_stars = ((polar_score['compound'] + 1)/ 2) * 4 + 1
            print(f"Rating: {round(computed_stars, 2)}")
            print('---------------------')
