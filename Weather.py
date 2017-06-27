import pprint
def get_weather(result):
    main = result['list']
    for reading in main:
        thing = reading['dt_txt']
        temp = reading['main']['temp']

        print "On %s it is %s" % (thing, temp)



    # arr = []
    #
    # for i in range(7):
    #     simpleforecast = result['forecast']['simpleforecast']['forecastday'][i]
    #     txtforecast = result['forecast']['txt_forecast']['forecastday'][i]
    #
    #     date = simpleforecast['date']
    #
    #     day = date['day']
    #     monthname = date['monthname']
    #     year = date['year']
    #     weekday = date['weekday']
    #     tz_long = date['tz_long']
    #     city_name = tz_long.split("/")[1]
    #     location = " ".join(city_name.split("_"))
    #
    #     high = simpleforecast['high']
    #     # {u'celsius': u'19', u'fahrenheit': u'66'}
    #
    #     low = simpleforecast['low']
    #     # {u'celsius': u'16', u'fahrenheit': u'61'}
    #
    #     icon = simpleforecast['icon']
    #     icon_url = simpleforecast['icon_url']
    #     conditions = simpleforecast['conditions']
    #
    #     humidity = simpleforecast['avehumidity']
    #     wind = simpleforecast['avewind']
    #     direction = wind['dir']
    #     mph = wind['mph']
    #     kph = wind['kph']
    #
    #     fcttext = txtforecast['fcttext']
    #     fcttext_metric = txtforecast['fcttext_metric']
    #
    #
    #     current = {
    #         "day": day,
    #         "monthname": monthname,
    #         "year": year,
    #         "weekday": weekday,
    #         "location": location,
    #         "high": high,
    #         "low": low,
    #         "icon": icon,
    #         "icon_url": icon_url,
    #         "conditions": conditions,
    #         "humidity": humidity,
    #         "wind": [direction, [mph, kph]],
    #         "text": [fcttext, fcttext_metric]
    #         }
    #     arr.append(current)
