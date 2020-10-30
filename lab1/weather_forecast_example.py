from VirtualCopernicusNG import TkCircuit
import pyowm

# initialize the circuit inside the

configuration = {
    "name": "CopernicusNG Weather Forecast",
    "sheet": "sheet_forecast.png",
    "width": 343,
    "height": 267,

    "servos": [
        {"x": 170, "y": 150, "length": 90, "name": "Servo 1", "pin": 17}
    ],
    "buttons": [
        {"x": 295, "y": 200, "name": "Button 1", "pin": 11},
        {"x": 295, "y": 170, "name": "Button 2", "pin": 12},
    ]
}

circuit = TkCircuit(configuration)

owm_key = "1a36004cdc1d325b837797622531da97"
owm = pyowm.OWM(owm_key)

#cities = ['Krakow', 'Istanbul', 'Stockholm', 'Dubai', 'Tokyo', 'London', 'Reykjavik', 'Sydney']
cities = ['Krakow', 'Istanbul', 'Stockholm']
city_index = 0

weather_angles_map = {
    'Thunderstorm': 50,
    'Drizzle': 30,
    'Rain': 40,
    'Snow': 40,
    'Mist': 0,
    'Smoke': -10,
    'Haze': 15,
    'Dust': -10,
    'Fog': 20,
    'Sand': -10,
    'Ash': 10,
    'Squall': 25,
    'Tornado': 25,
    'Clear': -70,
    'Clouds': -30
}


def get_weather_angle():
    weather = owm.weather_manager().weather_at_place(cities[city_index]).weather.status
    return weather_angles_map[weather]


def next_city():
    global city_index
    city_index = (city_index + 1) % len(cities)
    print(cities[city_index])


def previous_city():
    global city_index
    city_index = (city_index - 1)
    if city_index < 0:
        city_index = city_index + len(cities)
    print(cities[city_index])


@circuit.run
def main():
    # now just write the code you would use on a real Raspberry Pi

    from time import sleep
    from gpiozero import AngularServo, Button

    servo1 = AngularServo(17, min_angle=-90, max_angle=90)

    button_1 = Button(11)
    button_1.when_activated = previous_city

    button_2 = Button(12)
    button_2.when_activated = next_city

    while True:
        servo1.angle = get_weather_angle()
        sleep(0.1)
