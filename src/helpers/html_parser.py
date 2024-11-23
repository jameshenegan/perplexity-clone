from bs4 import BeautifulSoup


class HTMLParser:
    """
    Provides methods to parse HTML content and extract relevant information.
    """
    
    @staticmethod
    def parse_html(html_content: str) -> str:
        """
        Parses HTML content and extracts raw text.
        
        Args:
            html_content (str): The HTML content to parse.
        
        Returns:
            str: Extracted text from the HTML.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()
