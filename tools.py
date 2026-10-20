import httpx

URL = 'https://api.weatherapi.com/v1/current.json?'
API_KEY = '012ac3d27fd44834bde173546261910'

if not API_KEY:
    raise RuntimeError("API_KEY is not set")


async def get_weather(city):
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(URL, params={'q': city, 'key': API_KEY})
    except httpx.RequestError:
        return f'Could not reach the city {city}'
    data = resp.json()
    if resp.status_code != 200:
        return f'Could not get current weather for {city}'

    try:
        location_name = data['location']['name']
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind = data['current']['wind_mph']
    except (KeyError, TypeError):
        return f"Invalid data format received for {city}"

    return f"City name:{location_name}, Temperature:{temp}°С, Condition:{condition}, Humidity:{humidity}, Wind speed:{wind}"


TOOLS = {
    'get_weather': get_weather
}
