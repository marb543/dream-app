from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_url_path='/static')  

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    interpretation = None
    image_url = None
    if request.method == "POST":
        dream_description = request.form["prompt"]
        try:
            # Generate Jungian dream interpretation using OpenAI
            interpretation_response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a Jungian analyst. Interpret dreams based on Jungian psychology, using archetypes, the collective unconscious, and symbolic meaning."},
                    {"role": "user", "content": f"Dream: {dream_description}"}
                ],
                temperature=0.8,
                max_tokens=250
            )
            interpretation = interpretation_response.choices[0].message.content

            # Generate image using DALL-E 3
            image_response = openai.images.generate(
                model="dall-e-3",
                prompt=f"A surreal and symbolic visual representation of this dream: {dream_description}. Focus on archetypal symbols, like figures, actions, and settings.",
                n=1,
                size="1024x1024"
            )
            image_url = image_response.data[0].url

        except Exception as e:
            interpretation = f"Error: {str(e)}"
    
    return render_template("index.html", interpretation=interpretation, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
