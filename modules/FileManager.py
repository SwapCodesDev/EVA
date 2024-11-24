import base64
import mimetypes
import os
import json


def get_mime_type(path: str) -> str:
    """Get the MIME type of a file."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")
    mime_type, _ = mimetypes.guess_type(path)
    return mime_type or "application/octet-stream"


def encode_file(path: str) -> str:
    """Encode a file in base64 format."""
    try:
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Error encoding file: {e}")
    


def write_in_file(path, content):
    with open(path, 'w') as f:
        f.write(content)


def read_from_file(path):
    with open(path, 'r') as f:
        lines = f.read()
    return lines


def read_json(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{path}' is not a valid JSON.")
        return None
    

def write_json(path, data):
    try:
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully written to '{path}'.")
    except Exception as e:
        print(f"Error writing to file '{path}': {e}")


def update_json_key(path, key, value):
    try:
        # Read the current data
        with open(path, "r") as file:
            data = json.load(file)
        
        # Update the specific key
        if key in data:
            data[key] = value
        else:
            print(f"Key '{key}' not found in JSON file. Adding the key.")
            data[key] = value
        
        # Write the updated data back
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{path}' is not a valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_json_key(file_path, key):
    try:
        # Read the JSON data
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Return the value for the specified key
        return data.get(key, None)  # Returns None if the key does not exist
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
