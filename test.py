
import requests
import warnings
import os

# Suppress InsecureRequestWarning
warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

def process_audio_file(wave_file_path, text_file_path, language, auth_token):
    url = "https://speech.snuchennai.edu.in/speech_api"
    headers = {'Authorization': auth_token}

    # Ensure language is capitalized as in the server code
    language = language.capitalize()

    # Check if files exist before attempting to open them
    if not os.path.exists(wave_file_path):
        print(f"Error: Wave file not found at {wave_file_path}")
        return
    if not os.path.exists(text_file_path):
        print(f"Error: Text file not found at {text_file_path}")
        return

    with open(wave_file_path, 'rb') as wave_file, open(text_file_path, 'rb') as text_file:
        files = {
            'wave_file': (os.path.basename(wave_file_path), wave_file, 'audio/wav'),
            'text_file': (os.path.basename(text_file_path), text_file, 'text/plain')
        }
        data = {'languages': language}

        try:
            response = requests.post(url, files=files, data=data, headers=headers, verify=False)
            if response.status_code == 200:
                print("Success! Response:")
                print(response.text)
                return response.text
            elif response.status_code == 401:
                print("Error: Unauthorized access. Check the authorization token.")
            elif response.status_code == 500:
                print("Connection Host Error: Try Again")
            else:
                print(f"Error: {response.status_code}\n{response.text}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    wave_file_path = '/home/speechlab/Downloads/complete_demo_Wave_modified_hindi_2/data1/hindi_male_mono/wav/text_01180.wav'  # Path to your audio file
    text_file_path = 'test.txt'  # Path to your text file
    language = "Hindi"  # Case matters! Server compares with 'English'
    auth_token = 'W1VfgQ9GeVxfpCj79mFiCX0tsKFWSpqM'
    process_audio_file(wave_file_path, text_file_path, language, auth_token)
