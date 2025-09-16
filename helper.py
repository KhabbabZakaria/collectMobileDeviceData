import csv
import os
import re

def sanitize_filename(name):
    """
    Removes invalid characters from a string to make it a safe filename.
    """
    # Remove any character that is not a letter, number, underscore, or hyphen
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '', name)
    # Ensure the filename is not empty
    return sanitized if sanitized else "default_user"

def save_data_to_csv(username, data):
    """
    Saves a list of sensor data dictionaries to a CSV file named after the user.
    The file will be overwritten if it already exists.
    
    Args:
        username (str): The name of the user, used for the filename.
        data (list): A list of dictionaries containing sensor data.
        
    Returns:
        str: The path to the saved file.
    """
    if not data:
        raise ValueError("Data list cannot be empty.")

    sanitized_user = sanitize_filename(username)
    filename = f"{sanitized_user}.csv"
    
    # Ensure the 'collections' directory exists
    os.makedirs('collections', exist_ok=True)
    filepath = os.path.join('collections', filename)

    with open(filepath, 'w', newline='') as f:
        # The fieldnames are taken from the first data point
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    return filepath

