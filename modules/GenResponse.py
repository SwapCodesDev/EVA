import google.generativeai as genai
from GenInstruction import instruction
from StaticVariables import API
from FileManager import get_mime_type
import time
import os


def upload_to_gemini(path: str, mime_type: str = None):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"The file at path '{path}' does not exist.")
    
    try:
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file
    except Exception as e:
        raise RuntimeError(f"File upload failed: {e}")


def wait_for_files_active(files: list):
    print("Waiting for file processing...")
    for name in (file.name for file in files):
        try:
            file = genai.get_file(name)
            while file.state.name == "PROCESSING":
                print(".", end="", flush=True)
                time.sleep(10)
                file = genai.get_file(name)
            if file.state.name != "ACTIVE":
                raise Exception(f"File {file.name} failed to process.")
        except Exception as e:
            raise RuntimeError(f"Error while waiting for files: {e}")
    print("...all files ready\n")


def configure_genai(api_key: str = API[0], model: str = "gemini-1.5-flash", index: int = 0):
    try:
        genai.configure(api_key=api_key)
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        return genai.GenerativeModel(
            model_name=model,
            generation_config=generation_config,
            system_instruction=instruction(index),
        )
    except Exception as e:
        raise RuntimeError(f"Error during model configuration: {e}")


def generate_response(input_text: str, instruction: int = 0, chat_history: list = []):
    try:
        model = configure_genai(index=instruction)
        chat_session = model.start_chat(history=chat_history)
        response = chat_session.send_message(input_text)
        return response.text
    except Exception as e:
        return f"Error during response generation {e}"


def generate_response_with_file(
    path: str, input_text: str, instruction: int = 0, chat_history: list = None
):
    try:
        mime_type = get_mime_type(path)

        file_id = upload_to_gemini(path, mime_type)

        if chat_history is None:
            chat_history = [{"role": "user", "parts": [file_id]}]

        wait_for_files_active([file_id])  # Wait until the file is active
        model = configure_genai(index=instruction)
        chat_session = model.start_chat(history=chat_history)
        response = chat_session.send_message(input_text)
        return response.text
    except Exception as e:
        return f"Error during response generation {e}"
