import pprint

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

        current = [day, monthname, year, weekday, location, high, low, icon, icon_url, conditions, humidity, [direction, [mph, kph]], [fcttext, fcttext_metric]]
        arr.append(current)

    return arr


def get_hourly(hourly):
    today = []
    rest_of_days = []
    all_days = []
    for i in range(5):
        day = hourly[i]
        temp = day['temp']
        icon_url = day['icon_url']
        condition = day['condition']

        fcttime = day['FCTTIME']
        time = fcttime['civil']
        mday = fcttime['mday']
        mon =fcttime['mon']

        today_hour = {
            'condition': condition,
            "icon_url": icon_url,
            'temp': temp,
            'time': time,
            'mon': mon,
            'mday': mday
        }

        today.append(today_hour)

    j = 0
    count = 0
    while count < 7:
        day_obj = hourly[j]
        hour = day_obj['FCTTIME']['hour']
        feels = day_obj['feelslike']
        temp = day_obj['temp']
        # civil = day_obj['FCTTIME']['civil']
        # mday = day_obj['FCTTIME']['mday']
        day = [feels, temp]
        if count == 0 or hour == '12':
            all_days.append(day)
            count += 1
        j += 1
    return today, all_days


class WeatherDay():
    def __init__(self, forecast, hourly):

        feels = hourly[0]
        self.feels = feels
        current_temp = hourly[1]
        self.current_temp = current_temp

        day = forecast[0]
        self.day = day
        monthname = forecast[1]
        self.monthname = monthname
        year = forecast[2]
        self.year = year
        weekday = forecast[3]
        self.weekday = weekday
        location = forecast[4]
        self.location = location
        high = forecast[5]
        self.high = high
        low = forecast[6]
        self.low = low
        icon = forecast[7]
        self.icon = icon
        icon_url = forecast[8]
        self.icon_url = icon_url
        conditions = forecast[9]
        self.conditions = conditions
        humidity = forecast[10]
        self.humidity = humidity
        wind = forecast[11]
        self.wind = wind
        text = forecast[12]
        self.text = text


class Today(WeatherDay):
    def __init__(self, forecast, hourly, hours):
        WeatherDay.__init__(self, forecast, hourly)
        self.hours = hours

def get_all_weather(hourly_result, forecast_result):
    rest = []
    hourly_forecast = hourly_result['hourly_forecast']
    today_hours, all_hours = get_hourly(hourly_forecast)

    forecast_10day = get_forecast(forecast_result)

    for i in range(len(forecast_10day)):
        hourly = all_hours[i]
        forecast = forecast_10day[i]
        if i == 0:
            today = Today(forecast, hourly, today_hours)
        else:
            day = WeatherDay(forecast, hourly)
            rest.append(day)

    return today, rest
