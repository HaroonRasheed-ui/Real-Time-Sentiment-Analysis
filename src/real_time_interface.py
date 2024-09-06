from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine sentiment
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, polarity

def main():
    print("Real-time Sentiment Analysis")
    print("Type 'exit' to quit")
    
    while True:
        # Take user input
        user_input = input("Enter text: ")
        
        if user_input.lower() == 'exit':
            break
        
        # Analyze sentiment
        sentiment, polarity = analyze_sentiment(user_input)
        
        # Display results
        print(f"Sentiment: {sentiment}")
        print(f"Polarity: {polarity:.2f}")

if __name__ == "__main__":
    main()