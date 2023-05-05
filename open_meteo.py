import requests
import json
import datetime
from pytz import timezone

# api url format for https://open-meteo.com/
# need to replace <lat> and <long> with values
api_base = "https://api.open-meteo.com/v1/forecast?latitude=<lat>&longitude=<long>&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph&timezone=America%2FLos_Angeles"

class OpenMeteo:
    def __init__(self, lat: float, long: float):
        """
            Input: lat and long

            values and an API call is made to https://open-meteo.com/.
            Current weather values are queried and stored in the object
        """
        # gather input values
        self.lat = lat
        self.long = long

        # make api call
        self.api_url = self.get_api_url()
        self.api_raw_json = self.get_api_response()
        self.output = self.get_output()

    def __str__(self):
        return f'lat: {self.lat}, long: {self.long}, api_url: {self.api_url}, output: {self.output}'

    def get_curr_time(self, tz="US/Pacific"):
        """

            Get current datetime in the following format (PST):
            2023-04-11 11:20 AM
        """
        return datetime.datetime.now(timezone(tz)).strftime("%Y-%m-%d %H:%M %p")


    def get_output(self) -> dict:
        """
            Parse values out of the 'current_weather' portion of the api return value
        """
        curr_weather = self.api_raw_json['current_weather']
        return (f"{curr_weather['temperature']} F",
                f"{curr_weather['windspeed']} mph",
                self.get_curr_time())

    def get_api_url(self) -> str:
        """
            Take the api_base string (Global variable) and replace
            <lat> and <long> with the inputted values.
        """
        api_url_str = api_base.replace('<lat>', str(self.lat))
        api_url_str = api_url_str.replace('<long>', str(self.long))
        return api_url_str

    def get_api_response(self):
        """
            Make api call and return the json response received.
        """
        res = requests.get(self.api_url)

        if res.status_code != 200:
            raise Exception(f'Error during API call. Please check the URL provided: {self.api_url}')
        return json.loads(res.text)


if __name__ == '__main__':
    ws = OpenMeteo(31.284788, -92.471176)
    print(ws)
