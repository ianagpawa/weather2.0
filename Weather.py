import pprint

class WeatherDay():

    def __init__(self, result):
        fcttime = result['FCTTIME']

        time = fcttime['civil']
        mday = fcttime['mday']
        month = fcttime['month_name']
        weekday = fcttime['weekday_name']
        year = fcttime['year']

        condition = result['condition']
        feels = result['feelslike']
        humidity = result['humidity']
        icon_url = result['icon_url']
        temp = result['temp']
        wind_direction = result['wdir']
        wind_speed = result['wspd']

        self.time = time
        self.mday = mday
        self.month = month
        self.weekday = weekday
        self.year = year
        self.condition = condition
        self.feels = feels
        self.humidity = humidity
        self.icon_url = icon_url
        self.temp = temp
        self.wind_direction = wind_direction
        self.wind_speed = wind_speed




def get_forecast(result):
    arr = []

    for i in range(7):
        simpleforecast = result['forecast']['simpleforecast']['forecastday'][i]
        txtforecast = result['forecast']['txt_forecast']['forecastday'][i]

        date = simpleforecast['date']

        day = date['day']
        monthname = date['monthname']
        year = date['year']
        weekday = date['weekday']
        tz_long = date['tz_long']
        city_name = tz_long.split("/")[1]
        location = " ".join(city_name.split("_"))

        high = simpleforecast['high']
        # {u'celsius': u'19', u'fahrenheit': u'66'}

        low = simpleforecast['low']
        # {u'celsius': u'16', u'fahrenheit': u'61'}

        icon = simpleforecast['icon']
        icon_url = simpleforecast['icon_url']
        conditions = simpleforecast['conditions']

        humidity = simpleforecast['avehumidity']
        wind = simpleforecast['avewind']
        direction = wind['dir']
        mph = wind['mph']
        kph = wind['kph']

        fcttext = txtforecast['fcttext']
        fcttext_metric = txtforecast['fcttext_metric']


        current = {
            "day": day,
            "monthname": monthname,
            "year": year,
            "weekday": weekday,
            "location": location,
            "high": high,
            "low": low,
            "icon": icon,
            "icon_url": icon_url,
            "conditions": conditions,
            "humidity": humidity,
            "wind": [direction, [mph, kph]],
            "text": [fcttext, fcttext_metric]
            }
        arr.append(current)
    return arr


def get_hourly(hourly):
    today = []
    rest_of_days = []
    # for i in range(3):
    #     day = WeatherDay(hourly[i])
    #     print vars(day)
    j = 3
    i = 0
    while i < 6:
        day_obj = hourly[j]
        hour = day_obj['FCTTIME']['hour']
        if hour == '12':

            feels = day_obj['feelslike']
            temp = day_obj['temp']

            day = [feels, temp]
            rest_of_days.append(day)

            i += 1
        j += 1
    return rest_of_days
