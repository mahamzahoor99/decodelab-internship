# Simple Recommendation System

movies = {
    "Action": ["John Wick", "Mad Max", "The Dark Knight"],
    "Comedy": ["The Mask", "Home Alone", "Mr. Bean"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"]
}

print("=== Movie Recommendation System ===")
print("Available Categories:")
print("Action, Comedy, Sci-Fi, Horror")

choice = input("\nEnter your favorite category: ")

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Sorry! Category not found.")