from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Define a list of URLs to scrape data from
url_list = [
    "https://www.gnome-look.org/browse?cat=135&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=2&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=3&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=4&ord=rating",
    "https://www.gnome-look.org/browse?cat=135&page=5&ord=rating",
]

# Create an empty list to store the names of the themes
theme_name_list = []

# Loop through each URL in the url_list
for url in url_list:
    # Create a new HTMLSession object
    session = HTMLSession()
    # Send a GET request to the URL and store the response
    response = session.get(url)
    # Render the HTML of the response
    response.html.render()
    # Create a BeautifulSoup object from the rendered HTML
    soup = BeautifulSoup(response.html.html, 'html.parser')
    # Find all div elements with the class "product-browse-list-item container-wide standard"
    themes = soup.find_all("div", class_="product-browse-list-item container-wide standard")

    # Loop through each theme element
    for theme in themes:
        # Find the h2 element within the theme element and append its text to the theme_name_list
        theme_name_list.append(theme.find("h2").text)

# Print the final list of theme names and its length
print(theme_name_list)
print(len(theme_name_list))
