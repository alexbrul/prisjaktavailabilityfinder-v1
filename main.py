import requests
from bs4 import BeautifulSoup

urll = 'https://www.prisjakt.no/product.php?p=5113846'

def findAvailableProduct(url):
    # Send a GET request to the page and parse the HTML content using BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <li> elements on the page
    list_items = soup.find_all('li')
    print(list_items)
    for li in list_items:
        print(li)

    # Create an empty list to hold the results
    results = []

    # Loop through each <li> element
    for li in list_items:
        try:
            # Find the <picture> and <svg> elements inside the <li>
            picture = li.find('picture')
            svg = li.find_all('svg')

            # Extract the 'alt' text from the <picture> element and the class name from the <svg> element
            alt_text = picture.find('img')['alt']
            class_name = svg[-2]['class'][-1]

            # Add the extracted information to the results list as a tuple
            results.append((alt_text, class_name))
        except:
            pass

    # Print the results list
    print(results)

findAvailableProduct(urll)