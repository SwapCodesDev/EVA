from GenResponse import generate_response, generate_response_with_file
from StaticVariables import intent as intent_list
from ScreenshotManager import take_active_window_screenshot, get_screenshot_path, take_screenshot
from CommandManager import execute_batch_command, contains_batch_code
from TextFormating import separate_batch_script
from RealtimeData import get_time_by_city, get_timezones
from FileManager import update_json_key


def intent_resolve(input_text):
    intent = generate_response(f"keywords: {str(intent_list)}\n{input_text}", 1).strip()
    update_json_key('files/eva.json', 'intent', intent)

    if intent == "BASIC_STATEMENT":
        response = generate_response(input_text)

    if intent == "BASIC_QUESTION":
        response = generate_response(input_text, 2)
    
    if intent == "COMMAND":
        response = generate_response(input_text, 3)
        if contains_batch_code(response):
            script = separate_batch_script(response)
            execute_batch_command(script)
            response = "Task is being Processed"
        else:
            print("Task failed: Command script not found")

    if intent == "SCREEN_BASED_QUERY_WHICH_REQUIRES_CONTENT_PRESENT_ON_SCREEN":
        take_active_window_screenshot()
        path = get_screenshot_path()
        response = generate_response_with_file(path, input_text, 6)

    if intent == "TAKE_SCREENSHOT":
        take_screenshot()
        response = "screenshot has been taken"

    if intent == "DATE_AND_TIME_DETAILS":
        all_timezones = get_timezones()
        time_zone = generate_response(f"only from: {all_timezones}\n{input_text} (if city not given consider asia/kolkata)", 7).strip()
        print(f"Time Zone: {time_zone}")
        time_data = get_time_by_city(time_zone)
        print(f"Time Data: {time_data}")
        response = generate_response(f"'time: {time_data}\ninput query: {input_text}", 7)
    
    return response
