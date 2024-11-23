from openai import OpenAI
from helpers.serializer import Serializer


class ImproverModel:
    """
    Uses an LLM (e.g., OpenAI GPT) to improve refined text
    using additional expanded information.
    """

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        """
        Initializes the ImproverModel with an OpenAI client and model.
        
        Args:
            api_key (str): API key for OpenAI.
            model (str): Model to use for the improvement process. Defaults to 'gpt-4o-mini'.
        """
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def improve_text(
        self,
        query: str,
        refined_text_from_website: str,
        refined_text_from_corpus: str
    ) -> str:
        """
        Improves basic information using expanded information.
        
        Args:
            query (str): The query guiding the improvement process.
            refined_text_from_website (str): The basic refined text to improve.
            refined_text_from_corpus (str): The expanded refined text to use for improvement.
        
        Returns:
            str: Improved version of the refined text.
        """
        system_content = f"""
You will be asked a query.

You will also have access to some basic information to answer the query.
You will also have access to some expanded information to answer the query.

Write an improved version of the basic information using the expanded information.

---

Here is the basic information: {refined_text_from_website}

---

Here is the expanded information: {refined_text_from_corpus}
"""

        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": f"Here is the Query: {query}"},
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
