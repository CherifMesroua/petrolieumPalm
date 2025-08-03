import requests
import os

def test_file_upload():
    url = 'http://127.0.0.1:8000/api/uploads/'
    
    # Update this path to your actual test file location
    file_path = 'C:\\Users\\user\\Downloads\\base de donner WL 2025.xlsx'
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return
        
    try:
        with open(file_path, 'rb') as file:
            files = {
                'original_file': file
            }
            response = requests.post(url, files=files)
            print(response.json())
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_file_upload()