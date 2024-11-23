from openai import OpenAI
from helpers.serializer import Serializer


class WriterCiterModel:
    """
    Uses an LLM (e.g., OpenAI GPT) to generate a response to a query,
    citing provided reference material.
    """

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        """
        Initializes the WriterCiterModel with an OpenAI client and model.
        
        Args:
            api_key (str): API key for OpenAI.
            model (str): Model to use for generating the response. Defaults to 'gpt-4o-mini'.
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_cited_response(self, rephrased_query: str, set_of_reference_query: str) -> str:
        """
        Generates an accurate and cited response to a query using reference material.
        
        Args:
            rephrased_query (str): The rephrased query for clarity.
            set_of_reference_query (str): Reference material in summarized format.
        
        Returns:
            str: Generated response with in-line citations.
        """
        system_content = """
Write an accurate and concise answer for the given query, 
using _only_ the provided summarized web search results. 
The answer should be correct, high-quality, and written by an expert using an unbiased and journalistic tone. 
The answer should be informative, interesting, and engaging. 
The answer's logic and reasoning should be rigorous and defensible. 
Every sentence in the answer should be _immediately followed_ by an in-line citation to the search result(s). 
The cited search result(s) should fully support _all_ the information in the sentence. 
Search results need to be cited using [index]. 
When citing several search results, use [1][2][3] format rather than [1, 2, 3]. 
You can use multiple search results to respond comprehensively while avoiding irrelevant search results.
"""

        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"Query: {rephrased_query}\nSet of Reference Material: {set_of_reference_query}"},
        ]

        # Make API request
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model
            )

            serializer = Serializer()
            return serializer.serialize_to_json(response)
            
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            return None
