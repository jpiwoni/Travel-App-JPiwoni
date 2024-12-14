from flask import Flask, render_template, request
import requests

app = Flask(__name__)

WEATHER_API_KEY = '11171966cd4348cf83470211241412'
WEATHER_API_URL = 'https://api.weatherapi.com/v1/current.json'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    location = request.form['location']
    
    weather_data = get_weather_data(location)
    
    if not weather_data:
        return render_template('results.html', location=location, error="Could not fetch weather data.")
    
    return render_template('results.html', location=location, weather_data=weather_data)

def get_weather_data(location):
    params = {
        'key': WEATHER_API_KEY,
        'q': location  
    }
    response = requests.get(WEATHER_API_URL, params=params)
    
    if response.status_code == 200:
        return response.json() 
    else:
        return None  

if __name__ == '__main__':
    app.run(debug=True)
