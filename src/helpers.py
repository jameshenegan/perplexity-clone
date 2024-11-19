from bs4 import BeautifulSoup

def parse_html(html_content):
    """Parse HTML content and extract raw text."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()
