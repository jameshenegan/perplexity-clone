from openai import OpenAI

from helpers.serializer import Serializer


class RefinerModel:
    """
    Uses an LLM (e.g., OpenAI GPT) to refine raw text 
    and extract information relevant to a query.
    """

    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        """
        Initializes the RefinerModel with an OpenAI client and model.
        
        Args:
            api_key (str): API key for OpenAI.
            model (str): Model to use for the refinement process. Defaults to 'gpt-4o-mini'.
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def refine_text(self, raw_text: str, query: str) -> str:
        """
        Refines raw text and extracts information relevant to the query.
        
        Args:
            raw_text (str): The raw text to refine.
            query (str): The query guiding the refinement process.
        
        Returns:
            str: Refined text relevant to the query.
        """

        system_content = f"""
Filter the following text to information related to the query: {query}.  

Only use what is available in the original raw text.  

If the original raw text contains nothing that is relevant, then respond with the following message:

'THERE IS NO RELEVANT INFORMATION IN THE RAW TEXT'
"""
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"Raw text: {raw_text}"},
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
