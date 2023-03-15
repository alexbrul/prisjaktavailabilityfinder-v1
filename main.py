import requests
from bs4 import BeautifulSoup

urll = 'https://www.prisjakt.no/product.php?p=5113846'

def findAvailableProduct(url):
    # Send a GET request to the page and parse the HTML content using BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <li> elements on the page
    list_items = soup.find_all('li')

    # Create an empty list to hold the results
    results = []

    # Loop through each <li> element
    for li in list_items:
        try:
            picture = li.find('picture')
            svg = li.find_all('svg')

            alt_text = picture.find('img')['alt']
            class_name = svg[-2]['class'][-1]

            if class_name == "iconstockinstock":
                results.append((alt_text, class_name))
        except:
            pass

    # Print the results list
    return results

output = findAvailableProduct(urll)

print(output)