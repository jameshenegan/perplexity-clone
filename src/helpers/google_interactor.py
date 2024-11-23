from googleapiclient.discovery import build
from dotenv import dotenv_values


class GoogleInteractor:
    """
    Handles interactions with the Google Custom Search API and HTML parsing.
    """
    
    def __init__(self, api_key: str, search_engine_id: str):
        """
        Initializes the GoogleInteractor with API key and search engine ID.
        """
        self.google_service = self._create_google_service(api_key)
        self.search_engine_id = search_engine_id

    def _create_google_service(self, api_key: str):
        """
        Creates a Google Custom Search API service.
        """
        return build("customsearch", "v1", developerKey=api_key)

    def search_google(self, query: str, num_results: int = 10) -> dict:
        """
        Submits a query to Google Custom Search API and retrieves the results.
        
        Args:
            query (str): The search query.
            num_results (int): Number of results to fetch (default is 10).
        
        Returns:
            dict: A dictionary containing the search results.
        """
        response = self.google_service.cse().list(
            q=query, cx=self.search_engine_id, num=num_results
        ).execute()
        return response


# Example usage
if __name__ == "__main__":
    # Load environment variables
    config = dotenv_values("../../.env")
    google_api_key = config['GOOGLE_API_KEY']
    search_engine_id = config['SEARCH_ENGINE_ID']
    
    # Initialize GoogleInteractor
    google_interactor = GoogleInteractor(api_key=google_api_key, search_engine_id=search_engine_id)
    
    # Perform a search
    query = "Where to buy life insurance in Mississippi?"
    search_results = google_interactor.search_google(query=query, num_results=10)
    
    
    # Print the search results
    print(search_results)
