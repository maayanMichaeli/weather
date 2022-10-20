from requests import get
import json
from datetime import datetime
import random


def seven_days_forecast(city):
    """
    A function that gets the weather forecast for the next 7 days for the requested city.
    :param city: the city to get the forecast for.
    :return: a list for 7 days with the following attr for each day: date, max temp, min temp, avg temp, humidity.
    """

    if ' ' not in city:
        city += ','

    baseurl = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + \
              city + \
              '/next7days?'
    params = {'unitGroup': 'metric',
              'elements': 'datetime,tempmax,tempmin,temp,humidity',
              'key': '5UNU7BCKU5MGMGA2AEVAETFS8',
              'contentType': 'json'}

    data = get(baseurl, params)
    status = data.status_code
    fantasy_lands = ['on Mars', 'in Narnia', 'in Middle Earth', 'in Asgard','in Omicron', 'on the moon','in the 7 kingdoms']
    if status != 200:
        return {'status': status,
                'message': f"Sorry, We do not support cities {random.choice(fantasy_lands)}. Yet"}
    content = json.loads(data.content)
    res_addr = content['resolvedAddress']
    curr_cond = content['currentConditions']
    days_list = [{attr: day[attr]
                  for attr in ['datetime', 'temp', 'tempmin', 'tempmax', 'humidity']}
                 for day in content['days']]
    for day in days_list:
        day['weekday'] = datetime.strptime(day['datetime'], '%Y-%m-%d').strftime('%A')
        day['datetime'] = "/".join(day['datetime'].split("-")[::-1])
    fdict = {'status': status, 'res_addr': res_addr, 'curr_cond': curr_cond, 'days': days_list}
    with open("./history/searchHistory.txt","a+") as file:
        file.write(city+'\n')
    return fdict


if __name__ == "__main__":
    print(seven_days_forecast('haifa'))
