
# Image Generation with OpenAI's DALL-E 3

This Python project allows you to generate images using OpenAI's DALL-E 3 model by providing a text prompt. The application integrates with the OpenAI API to create images based on the provided prompt.

## Features

- **Generate Images from Text Prompts:** Use DALL-E 3 to generate high-quality images based on the prompts you provide.
- **Simple API Integration:** The project uses the OpenAI Python library to communicate with the DALL-E 3 model.
- **Error Handling:** The application includes error handling to manage API issues.

## Requirements

- Python 3.x
- OpenAI API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SathishMadhiyalagan/imageGeneration.git
   cd imageGeneration
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required libraries:**

   Ensure you have `openai` and any necessary dependencies by installing them with:

   ```bash
   pip install openai
   ```

4. **Set up your OpenAI API key:**

   - Create a new Python file `newfile.py` and add your OpenAI API key as follows:

     ```python
     OPENAPIKEY = "your-openai-api-key"
     ```

   - Replace `"your-openai-api-key"` with your actual OpenAI API key.

   **Note:** Be sure not to commit your API key to the repository. Add `newfile.py` to your `.gitignore` file.

## Usage

1. **Run the Python script to generate an image:**

   Execute the script to generate an image using the provided prompt:

   ```bash
   python imageFolder/imageGeneration.py
   ```

   This will use the prompt `"how the world is there in 50 years after"`, but you can change the prompt in the script to any text you like.

2. **Modify the Prompt:**

   To use your own prompt, change the value of the `prompt` variable in the script:

   ```python
   prompt = "a futuristic cityscape with flying cars"
   ```

3. **View the Image URL:**

   After running the script, it will output the URL of the generated image in the console:

   ```bash
   Image URL: <generated_image_url>
   ```

   You can open the URL in a browser to view or download the generated image.

## Important Notes

- **API Key Security:** Ensure that your OpenAI API key is kept secure and not exposed in public repositories. Use `.gitignore` to avoid committing sensitive files like `newfile.py` to GitHub.
  
  Example `.gitignore` entry:

  ```plaintext
  newfile.py
  ```

- **API Rate Limits:** The OpenAI API may have rate limits and costs associated with image generation. Make sure to monitor your API usage.

## Contributing

Feel free to fork the repository and submit pull requests for improvements, bug fixes, or new features.

