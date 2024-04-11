# import requests

# def process_audio_file(file_path, language, auth_token):
#     url = f"http://speech.snuchennai.edu.in/speech_api"
#     files = {'file': open(file_path, 'rb')}
#     data = {'languages': language}
#     headers = {'Authorization': auth_token}  # Authorization header
    
#     response = requests.post(url, files=files, data=data, headers=headers)
    
#     if response.status_code == 200:
#         print(response.text)
#     elif response.status_code == 500:
#         print("Connection Host Error: Try Again") 
#     else:
#         # If there was an error, print the status code
#         print("Error:", response.status_code)

# # Example usage:
# file_path = '/home/speechlab/sooriya/speech_new/Lab_Files/sa1.wav' # Path to your audio file
# language = "english"  # Language parameter: 'tamil', 'english', or 'hindi'
# auth_token = 'W1VfgQ9GeVxfpCj79mFiCX0tsKFWSpqM'  # Your authorization token
# process_audio_file(file_path, language, auth_token)


import requests

def process_audio_file(wave_file_path, text_file_path, language, auth_token):
    url = "http://speech.snuchennai.edu.in/speech_api"
    wave_file = {'wave_file': open(wave_file_path, 'rb')}
    text_file = {'text_file': open(text_file_path, 'rb')}
    data = {'languages': language}
    headers = {'Authorization': auth_token}  # Authorization header
    
    response = requests.post(url, files={**wave_file, **text_file}, data=data, headers=headers)
    
    if response.status_code == 200:
        print(response.text)
    elif response.status_code == 500:
        print("Connection Host Error: Try Again") 
    else:
        # If there was an error, print the status code
        print("Error:", response.status_code)

# Example usage:
wave_file_path = '/home/speechlab/sooriya/speech_new/Lab_Files/sa1.wav' # Path to your audio file
text_file_path = '/home/speechlab/sooriya/speech_new/test.txt'  # Path to your text file
language = "english"  # Language parameter: 'tamil', 'english', or 'hindi'
auth_token = 'W1VfgQ9GeVxfpCj79mFiCX0tsKFWSpqM'  # Your authorization token
process_audio_file(wave_file_path, text_file_path, language, auth_token)
