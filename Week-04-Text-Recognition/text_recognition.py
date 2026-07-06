from textblob import TextBlob

print("=== Text Recognition System ===")

text = input("Enter a sentence: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity

if polarity > 0:
    print("\nSentiment: Positive 😊")
elif polarity < 0:
    print("\nSentiment: Negative 😔")
else:
    print("\nSentiment: Neutral 😐")