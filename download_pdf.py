import requests
import json
import os

def download_pdf(title, url, dir):
    filename = os.path.join(dir, title)

    response = requests.get(url, stream=True)

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description="Script to receive command line parameters"
    )

    parser.add_argument("-i", "--input", type=str, help="Input Json File")
    parser.add_argument("-o", "--output", type=str, help="Output Directory")

    args = parser.parse_args()

    json_file = args.input
    dir = args.output

    with open(json_file, "r", encoding= "utf-8") as f:
        
        books = json.load(f)
        count = 1
        for book in books:
            if count % 100 == 0:
                print(count)
            title = book.get("title")
            url = book.get("url")
            
            download_pdf(title, url, dir)
            count += 1