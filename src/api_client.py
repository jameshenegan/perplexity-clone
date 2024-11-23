import requests
from openai import OpenAI
from googleapiclient.discovery import build

def create_openai_client(api_key):
    """Create an OpenAI client."""
    return OpenAI(api_key=api_key)


def create_google_service(api_key, search_engine_id):
    """Create a Google Custom Search API service."""
    return build("customsearch", "v1", developerKey=api_key), search_engine_id

def get_openai_response_and_total_tokens(client, messages, model):
    """Make an API request to OpenAI."""
    chat_completion = client.chat.completions.create(
        messages=messages, model=model
    )
    return chat_completion.choices[0].message.content, chat_completion.usage.total_tokens, chat_completion.usage.completion_tokens, chat_completion.usage.prompt_tokens 

def search_google(service, search_engine_id, query, num_results=5):
    """Search Google Custom Search API."""
    result = service.cse().list(q=query, cx=search_engine_id, num=num_results).execute()
    return result.get('items', [])
