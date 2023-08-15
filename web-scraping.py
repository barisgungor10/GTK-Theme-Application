from requests_html import HTMLSession
from bs4 import BeautifulSoup

url_list = {
    "https://www.pling.com/browse?cat=135&ord=rating",
    "https://www.pling.com/browse?cat=135&page=2&ord=rating",
    "https://www.pling.com/browse?cat=135&page=3&ord=rating",
    "https://www.pling.com/browse?cat=135&page=4&ord=rating",
    "https://www.pling.com/browse?cat=135&page=5&ord=rating"
}
theme_name_list = []
image_link_list = []
description_link_list = []

for url in url_list:
    session = HTMLSession()
    response = session.get(url)
    response.html.render(timeout=8)

    soup = BeautifulSoup(response.html.html, 'html.parser')

    themes = soup.find_all("div", class_="product-browse-list-item container-wide standard")

    for theme in themes:
        theme_name_list.append(theme.find("h2").text)

        img_tag = theme.find("img")
        image_link_list.append(img_tag["src"])

        description_link_list.append(theme.find(class_="description").text)

print(theme_name_list)
print(image_link_list)
print((description_link_list))
