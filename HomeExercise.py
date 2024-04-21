import json
import os
import sys

def verify_input(file_path):

    # check if file_path is empty
    if not file_path:
        raise ValueError("File path is empty.")

    # if path exist
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    
     # if file is empty
    if os.path.getsize(file_path) == 0:
        raise AssertionError("File is empty.")

    # load JSON data from file
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        raise ValueError(f"Error reading JSON file '{file_path}': {e}")
    
     # access keys: 'PolicyDocument' and 'Statement'
    try:
        statement_array = data['PolicyDocument']['Statement']
    except KeyError as e:
        raise KeyError(f"Required key(s) not found in JSON data: {e}")


    # Check if 'Statement' is empty
    if not statement_array:
        raise ValueError("No statements found in the JSON file.")


    # if at least one position constains single '*' return false
    for statement in statement_array:
        if statement['Resource'].count('*') == 1:
            return False


    
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python HomeExercise.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        result = verify_input(file_path)
        print(result)
    except (ValueError, FileNotFoundError, AssertionError, KeyError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

    
# file_path = "policy.json"
# print(verify_input(file_path))