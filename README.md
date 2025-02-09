# minimal-flask-app
Minimal code for Flask app making calls to the OpenAI API


```
# Create virtual environment
python3 -m venv ./venv

# Activate your virtual environment
source venv/bin/activate

# Install the required packages. For example
pip3 install flask openai python-dotenv

# Rename the file .env-bup to .env. 
# Add your OPENAI_API_KEY to the .env file.

# Run the app
python3 app.py
```

# Dream Doctor Project Report

For this app, I implemented a Jungian dream interpreter based on the user's input from the form with a Submit button. I also implemented a Jungian dream image generator. For the first part
of the web app, I used OpenAI completions. I used the GPT-4 model. I input the following:
content for system role: "You are a Jungian analyst. Interpret dreams based on Jungian psychology, using archetypes, the collective unconscious, and symbolic meaning.". As for the
User content I input: f"Dream: {dream_description}". I set the temperature to 0.8 and the max tokens value. For the second part of the web app, I used the DALL-E-3 model and used the prompt.
: f"A surreal and symbolic visual representation of this dream: {dream_description}. Focus on archetypal symbols, like figures, actions, and settings.".

While building this web app, I encountered several issues; for example, I was not aware of how to build a Flask app with custom styles and images. So I had to learn how to build a Flask app.
with the appropriate folder structure where I need to create a static folder where I store my
CSS files and images. While working on my dream interpreter, I also had issues with retrieving
the image URL that is being generated. In fact, I tried to follow OpenAI's documentation on image
generation where you need to create an image from the client object. However, this did not work formy implementation of retrieving the OPEN_AI_API Key, so I had to do some research and instead
of generating an image from the client object, I did it by calling the generate method on OpenAI.
object.

Since it takes some time to get the response back from OpenAI, I decided to implement a
loading an object in my web app for a cleaner UI. I feel like this decision improved the overall
look and usability of my app.

