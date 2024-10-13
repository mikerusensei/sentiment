from module2 import Sentiment

if __name__ == '__main__':
    link = input("Enter link: ")

    sentiment = Sentiment()
    sentiment.review_sentiment(link)