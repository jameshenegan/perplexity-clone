from dotenv import dotenv_values
import requests

from helpers.google_interactor import GoogleInteractor
from helpers.html_parser import HTMLParser 
from helpers.storage_manager import StorageManager

# Load environment variables
config = dotenv_values("../.env")
google_api_key = config['GOOGLE_API_KEY']
search_engine_id = config['SEARCH_ENGINE_ID']

# Declare trial number
trial_number = 1
 
google_interactor = GoogleInteractor(api_key=google_api_key, search_engine_id=search_engine_id)
storage_manager = StorageManager("../data/")    

query = "Where to buy life insurance in Mississippi?"
search_results = google_interactor.search_google(query=query, num_results=10)
    

storage_manager.save_to_folder("InitialGoogleResponses", search_results, f"{trial_number}.json")
search_results = storage_manager.load_from_folder("InitialGoogleResponses", f"{trial_number}.json")


items = search_results['items']

raw_text_from_html = []

for item in search_results['items']:
    link = item['link']
    response = requests.get(link)
    parsed_text = HTMLParser.parse_html(response.content)
    raw_text_from_html.append({"link" : link, "raw_text" : parsed_text})
    
storage_manager.save_to_folder("RawTextFromHTML", raw_text_from_html, f"{trial_number}.json")