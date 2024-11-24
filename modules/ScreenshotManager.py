import pyautogui
import pygetwindow as gw
import os


def take_screenshot():
    # Define the relative path to the files directory
    base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Move one level up
    screenshot_directory = os.path.join(base_directory, 'files')
    screenshot_filename = 'screenshot.png'
    screenshot_path = os.path.join(screenshot_directory, screenshot_filename)

    try:
        # Ensure the files directory exists
        if not os.path.exists(screenshot_directory):
            os.makedirs(screenshot_directory, exist_ok=True)

        # Take a full screenshot
        screenshot = pyautogui.screenshot()

        # Validate screenshot object
        if screenshot is None:
            raise ValueError("Screenshot capture failed.")

        # Check if the file already exists and remove it
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

        # Save the screenshot
        screenshot.save(screenshot_path)

    except Exception as e:
        print(f"Error taking screenshot: {e}")


def take_active_window_screenshot():
    # Define the relative path to the files directory
    base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Move one level up
    screenshot_directory = os.path.join(base_directory, 'files')
    screenshot_filename = 'screenshot.png'
    screenshot_path = os.path.join(screenshot_directory, screenshot_filename)

    try:
        # Ensure the files directory exists
        if not os.path.exists(screenshot_directory):
            os.makedirs(screenshot_directory, exist_ok=True)

        # Get the active window
        active_window = gw.getActiveWindow()
        if not active_window:
            raise RuntimeError("No active window found.")

        # Get window bounds
        x, y, width, height = active_window.left, active_window.top, active_window.width, active_window.height

        # Take a screenshot of the specific region
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

        # Check if the file already exists and remove it
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

        # Save the screenshot
        screenshot.save(screenshot_path)
        print(f"Active window screenshot saved at: {screenshot_path}")

    except Exception as e:
        print(f"Error taking active window screenshot: {e}")


def get_screenshot_path():
    # Define the relative path to the files directory
    base_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Move one level up
    screenshot_directory = os.path.join(base_directory, 'files')
    screenshot_filename = 'screenshot.png'
    screenshot_path = os.path.join(screenshot_directory, screenshot_filename)

    try:
        # Check if the file exists
        if not os.path.exists(screenshot_path):
            raise FileNotFoundError(f"Screenshot not found at {screenshot_path}")

        # Return the absolute path
        return os.path.abspath(screenshot_path)

    except Exception as e:
        print(f"Error retrieving screenshot path: {e}")
        return None

