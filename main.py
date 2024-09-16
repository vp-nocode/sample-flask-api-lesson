# Importing the Flask Framework and the Request library
from flask import Flask, render_template, request
import requests

# importing Flask class object
app = Flask(__name__)

# form path and methods GET and POST
@app.route('/', methods=['GET', 'POST'])
# create a function with a variable weather, where we will store the weather
def index():
   weather = None
   news = None
# we form conditions for testing the method.
# We haven't created the form yet, but we'll only need to take the city from it.
   if request.method == 'POST':
       # we will take this specific city for the API request
       city = request.form['city']
       # we register a variable where the result will be saved
       # weather function with the indication of the city, which we take from the form

       weather = get_weather(city)
       if weather:
           print("weather: ", weather)
       else:
           print("Failed to retrieve weather data")

       news = get_news()
       if news:
           print("news: ", news)
       else:
           print("Failed to retrieve news data")


   return render_template("index.html", weather=weather, news=news)

# in the function we write the city that we will enter in the form
def get_weather(city):
   # api_key = "your api key"
   api_key = "8f7b432a1c7f30d425154161758ed997"
   # the address to which we will send the request.
   # Don't forget to specify the f-string
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   # to get the result we will need the requests module
   response = requests.get(url)
   # we write the format of the result return
   if response.status_code == 200:
       # we write the format of the result return
       return response.json()
   else:
       print("Error while receiving data:", response.status_code)
       return None

def get_news():
   api_key = "216a06544d934b8a9286726c3e87577f"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   # return response.json().get('articles', [])
   if response.status_code == 200:
       # we write the format of the result return
       return response.json().get('articles', [])
   else:
       print("Error while receiving data:", response.status_code)
       return None


if __name__ == '__main__':
   app.run(debug=True)
