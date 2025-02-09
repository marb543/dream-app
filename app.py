from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__, static_url_path='/static')  
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

@app.route("/", methods=["GET", "POST"])
def index():
    interpretation = None
    image_url = None
    if request.method == "POST":
        dream_description = request.form["prompt"]
        try:
            # Generate dream interpretation based on Jungian psychology
            interpretation_response = openai.ChatCompletion.create(
                model="gpt-4",  # Correct model name
                messages=[{
                    "role": "system", 
                    "content": "You are a Jungian analyst. Interpret dreams based on Jungian psychology, using archetypes, the collective unconscious, and symbolic meaning."
                }, {
                    "role": "user", 
                    "content": dream_description
                }],
                temperature=0.8,
                max_tokens=150
            )
            interpretation = interpretation_response.choices[0].message['content']
            
            # Generate image using DALL-E
            image_response = openai.Image.create(
                model="dall-e-3",  # Correct model name
                prompt=f"A surreal and symbolic visual representation of this dream: {dream_description}",
                n=1,
                size="1024x1024"
            )
            image_url = image_response.data[0].url

        except Exception as e:
            interpretation = f"Error: {str(e)}"
    
    return render_template("index.html", interpretation=interpretation, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
