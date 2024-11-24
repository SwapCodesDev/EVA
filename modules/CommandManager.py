import subprocess
from GenResponse import generate_response
import os
import re


def contains_batch_code(text):
    """
    Check if the given text contains a batch script.
    """
    return re.search(r'(@echo off.*?exit)', text, re.DOTALL) is not None


def execute_batch_command(batch_command):
    """
    Write the given batch command to a file and execute it safely.
    """
    if not batch_command:
        print("Error: No valid command to execute.")
        return

    # Path to store the batch file in the 'files' directory
    batch_file_path = os.path.join('files', 'script.bat')

    # Write the command to a batch file
    with open(batch_file_path, "w") as bat_file:
        bat_file.write(batch_command)

    # Ensure the command is safe before execution
    if not is_command_safe(batch_command, validation_method=0):
        print("Aborted: The command was deemed unsafe.")
        return

    # Execute the batch file
    try:
        subprocess.run(["cmd.exe", "/c", "start", batch_file_path], check=True)
        print("Batch file executed successfully.")
    except subprocess.CalledProcessError as error:
        print(f"Execution failed: {error}")


def is_command_safe(command, validation_method=1):
    """
    Check if the given command is safe to execute.
    Validation methods:
    - Method 0: Automated response from an external safety service.
    - Method 1: User confirmation for safety.
    """
    if validation_method == 0:
        # Use an automated response for safety validation
        safety_response = generate_response(command, 4)
        return safety_response.lower().strip() == 'true'

    elif validation_method == 1:
        # Provide safety analysis and prompt user confirmation
        print("Safety analysis: ", generate_response(command, 4))
        user_input = input("Would you like to execute the command? (y/n): ").strip().lower()
        return user_input == 'y'

    print("Error: Unknown validation method.")
    return False
