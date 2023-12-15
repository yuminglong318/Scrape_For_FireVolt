# Scrape ICCV

## Get the list of download
$ python3 get_list.py -u {URL} -o {OUTPUT_JSON_NAME}
e.g. $ python3 get_list.py -u "https://openaccess.thecvf.com/ICCV2021?day=all" -o "download_list_2021"

## Download the list
$ python3 download_pdf.py -i {input_json} -o {output_directory}
e.g. $ python3 download_pdf.py -i "download_list_2021.json" -o "./2021"
