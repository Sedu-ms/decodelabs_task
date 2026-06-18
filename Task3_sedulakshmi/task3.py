movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["Mr Bean", "Friends", "The Mask"],
    "romance": ["Titanic", "Notebook", "Me Before You"]
}

choice = input("Enter your favorite genre (action/comedy/romance): ")

if choice in movies:
    print("Recommended movies:")
    for movie in movies[choice]:
        print(movie)
else:
    print("Sorry, genre not found")
