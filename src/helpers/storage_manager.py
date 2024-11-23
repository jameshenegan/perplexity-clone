import os
import json


class StorageManager:
    """
    Manages saving and retrieving data as JSON files.
    """
    
    def __init__(self, base_directory: str = "data"):
        """
        Initializes the StorageManager with a base directory for file storage.
        
        Args:
            base_directory (str): The root directory for storing data. Defaults to 'data'.
        """
        self.base_directory = base_directory
        os.makedirs(self.base_directory, exist_ok=True)

    def save_to_folder(self, folder_name: str, data: dict, filename: str) -> None:
        """
        Saves a dictionary as a JSON file in the specified folder.
        
        Args:
            folder_name (str): The name of the folder within the base directory.
            data (dict): The data to save as JSON.
            filename (str): The name of the file (with .json extension).
        """
        folder_path = os.path.join(self.base_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {file_path}")

    def load_from_folder(self, folder_name: str, filename: str) -> dict:
        """
        Loads a JSON file from the specified folder.
        
        Args:
            folder_name (str): The name of the folder within the base directory.
            filename (str): The name of the file to load (with .json extension).
        
        Returns:
            dict: The data loaded from the JSON file.
        """
        file_path = os.path.join(self.base_directory, folder_name, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        print(f"Data loaded from {file_path}")
        return data


# Example usage
if __name__ == "__main__":
    # Initialize StorageManager
    storage_manager = StorageManager("../../data/")

    # Example data to save
    example_data = {
        "query": "Where to buy life insurance in Mississippi?",
        "results": [
            {"title": "Best Life Insurance in Mississippi", "url": "https://example.com"},
            {"title": "Affordable Life Insurance Options", "url": "https://anotherexample.com"}
        ]
    }

    # Save data
    storage_manager.save_to_folder("InitialGoogleResponses", example_data, "example_query.json")

    # Load data
    loaded_data = storage_manager.load_from_folder("InitialGoogleResponses", "example_query.json")
    print(loaded_data)
