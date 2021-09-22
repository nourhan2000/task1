import requests

def temp(city):
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a65647ad75178ccc9fd9ccafa6eb8ee4")
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return str(temp_f)
