import requests
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_current_weather(location: str):
    """Return main weather info for a city."""
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}"
    try:
        response = requests.get(url)
        data = response.json()
        if "error" in data:
            return f"Weather API Error: {data['error']['message']}"
        return (f"Weather in {data['location']['name']}, {data['location']['country']}:\n"
                f"Temperature: {data['current']['temp_c']}°C\n"
                f"Condition: {data['current']['condition']['text']}\n"
                f"Humidity: {data['current']['humidity']}%\n"
                f"Wind: {data['current']['wind_kph']} kph")
    except Exception as e:
        return f"Tool Crash: {str(e)}"

with open("system_prompt.txt", "r") as f:
    instructions = f.read()

client = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(
    model="gemini-2.5-flash-lite",
    config=types.GenerateContentConfig(
        tools=[get_current_weather],
        system_instruction=instructions
    )
)

def ask_chatbot(message: str) -> str:
    """Send message to Gemini chatbot and return response."""
    try:
        response = chat.send_message(message)
        text = response.text.replace("```html", "").replace("```", "").replace("</div>", "").strip()
        return text
    except Exception as e:
        return f"Error: {str(e)}"