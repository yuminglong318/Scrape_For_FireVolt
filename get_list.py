import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin


domain = "https://openaccess.thecvf.com/"

def get_list(url, filename):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all('dt', {'class': 'ptitle'})

    download_list = []

    for book in books:
        title = book.text.strip()
        pdf_tag = book.find_next(lambda tag: tag.name == 'a' and tag.text == 'pdf')
        if pdf_tag:
            pdf_url = urljoin(domain, pdf_tag.get('href'))
        
        download_list.append({
            'title': title,
            'url': pdf_url
        })

    with open(f"{filename}.json", "w", encoding= "utf-8") as f:
        json.dump(download_list, f, indent= 4)
    
if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(
        description="Script to receive command line parameters"
    )

    parser.add_argument("-u", "--url", type=str, help="Url link")
    parser.add_argument("-o", "--output", type=str, help="Output File Name")

    args = parser.parse_args()

    url = args.url
    filename = args.output

    get_list(url, filename)