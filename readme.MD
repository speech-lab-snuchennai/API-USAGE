# API usage guide

### !pip install requests
It utilizes the `requests` library to send HTTP requests.

## Parameters:
* file_path: This parameter should be the path to the audio file you want to process. Ensure that the file exists at this location and is accessible by the script.
  
* language: Specify the language of the audio content. Currently supported languages are 'tamil', 'english', or 'hindi'.

* auth_token :This token is used to authenticate your requests to the API. Make sure to replace the placeholder token with your actual authorization token.

## Output:
The function will print the response received from the API endpoint. 
If the status code is 200, it means the request was successful, and the extracted data will be printed.
If the status code is 500, it indicates a connection error with the host, and the function will prompt you to try again.
For any other status code, an error message along with the status code will be printed.

### Example Usage:
Here's how you can use the function:

1. Set the `file_path` variable to the path of your audio file.
2. Specify the `language` parameter according to the language of your audio content.
4. Replace the `auth_token` variable with your actual authorization token.
5. Call the `process_audio_file` function with the specified parameters.

### Contributors

 Project Officers

- [Preethi T](mailto:preethit@snuchennai.edu.in)
- [Sooriya S](mailto:sooriyas@snuchennai.edu.in)
- [Malarvizhi M](mailto:malarvizhim@snuchennai.edu.in)

 Project Intern

- [Adithya V](mailto:adithya21110421@snuchennai.edu.in)

## Demo

🌐 [Project Demo – SpeechLab, SNU Chennai](https://speech.snuchennai.edu.in/)


## License

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
© 2024–2026 speech-lab-snuchennai.

