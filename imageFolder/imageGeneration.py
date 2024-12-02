from newfile import OPENAPIKEY
import openai

# Set up the OpenAI API client with the key
openai.api_key = OPENAPIKEY

# Generate an image with DALL-E
def generate_image(prompt):
    try:
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            n=1,
        )
        # Extract the image URL
        image_url = response['data'][0]['url']
        print("Image URL:", image_url)
        return image_url
    except Exception as e:
        print("An error occurred:", e)
        return None

# Main function
if __name__ == "__main__":
    prompt = "how the world is there in 50 years after"
    image_url = generate_image(prompt)
