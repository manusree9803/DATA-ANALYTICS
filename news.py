import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
import time

# Initialize translator and sentiment analyzer
translator = Translator()
analyzer = SentimentIntensityAnalyzer()

# Fetch Headlines Function
def fetch_headlines():
    print("\nFetching headlines...")
    url = "https://www.thanthitv.com/latest-news"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status
    except requests.exceptions.RequestException as e:
        print(f"Error fetching headlines: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    headline_tags = soup.select('h3.headlineListing')

    if not headline_tags:
        print("No headlines found.")
        return []

    headlines = [tag.get_text().strip() for tag in headline_tags]
    return headlines

# Function to translate headlines
def translate_headline(headline):
    retries = 3
    while retries > 0:
        try:
            translated = translator.translate(headline, src='ta', dest='en').text
            if translated.strip() == "":
                raise ValueError("Empty translation")
            return translated
        except Exception as e:
            print(f"Translation error: {e}. Retrying...")
            retries -= 1
            time.sleep(1)
    return headline  # If translation fails, return original

# Function to analyze sentiment
def analyze_sentiment(headlines):
    print("Analyzing sentiment...\n")
    if not headlines:
        print("No headlines to analyze.\n")
        return

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for headline in headlines:
        try:
            translated = translate_headline(headline)
            vader_results = analyzer.polarity_scores(translated)
            compound_score = vader_results['compound']
            sentiment = "Positive" if compound_score > 0.05 else "Negative" if compound_score < -0.05 else "Neutral"

            print(f"Date & Time: {current_datetime}")
            print(f"Original Headline (Tamil): {headline}")
            print(f"Translated Headline (English): {translated}")
            print(f"Sentiment: {sentiment}\n")

        except Exception as e:
            print(f"Error analyzing headline: {headline} - {e}\n")

# Main Function
def main():
    while True:
        headlines = fetch_headlines()
        analyze_sentiment(headlines)

        print("Waiting for 15 minutes before next update...\n")
        try:
            time.sleep(900)  # 15 minutes = 900 seconds
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break

if __name__ == "__main__":
    main()
