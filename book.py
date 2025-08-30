import requests

def search_books(query):
    url = f"https://openlibrary.org/search.json?title={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        books = data.get("docs", [])[:10]  # first 10 results
        for idx, book in enumerate(books, start=1):
            title = book.get("title", "Unknown Title")
            authors = ", ".join(book.get("author_name", ["Unknown Author"]))
            year = book.get("first_publish_year", "N/A")
            print(f"{idx}. {title} | {authors} | {year}")
    else:
        print("Error fetching data from API")

if __name__ == "__main__":
    query = input("Enter a book title: ")
    if query.strip():
        search_books(query)
    else:
        print("Please enter a valid title.")
