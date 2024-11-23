import requests
import time

from bs4 import BeautifulSoup

def parse_html(html_content):
    """Parse HTML content and extract raw text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

combined_response = ""

urls = [
    "https://www.scfbins.com/insurance/other-products/financial-services",
    "https://www.scfbins.com/insurance/other-products/life-insurance",
    "https://www.sfbli.com/blogs/Giving-Thanks",
    "https://www.sfbli.com/blogs/LIAM2024",
    "https://www.sfbli.com/blogs/Celebrating-Fathers-Day",
    "https://www.sfbli.com/blogs/My-Reason-For-Life-Insurance",
    "https://www.sfbli.com/blogs/Insure-Your-Love-2024",
    "https://www.sfbli.com/blogs/Planning-For-The-Future",
    "https://www.sfbli.com/blogs/LIAM-2023",
    "https://www.sfbli.com/blogs/Values",
    "https://www.sfbli.com/blogs/Why-Life-Insurance",
    "https://www.sfbli.com/blogs/Women-And-Insurance",
    "https://www.sfbli.com/blogs/LIAM-2023",
    "https://www.sfbli.com/blogs/Planning-For-The-Future",
    "https://www.insure.com/companies/southern-farm-bureau-life-insurance.html",
    "https://msfbins.com/products/life/",
    "https://sfbli.com/aboutus"
]

for url in urls:
    time.sleep(1)
    response = requests.get(url)
    parsed_html = parse_html(response.content)
    combined_response += parsed_html

with open ("./data/content.txt", 'w') as f:
    f.write(combined_response)