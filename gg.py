from time import sleep
import requests_cache

TIME_URL =  'https://timeapi.io/api/Time/current/'

if __name__ == '__main__':

    vostok_url = TIME_URL + 'zone?timeZone=Europe/Moscow'
    
    for iteration in range(5):
        if iteration > 2:
            session.cache.clear()

        session = requests_cache.CachedSession()
        response = session.get(vostok_url)

        data = response.json()

        result = data.get('dateTime')
        print(iteration, result)
        sleep(1)

        utc_offset = data.get('time')
    # Печать часового пояса.
    print('Часовой пояс антарктической станции «Восток»:', utc_offset) 