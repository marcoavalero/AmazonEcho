import requests
import simplejson as json

id1='your_thermostat_id'
token='your_nest_token'

def getTemperature():
    url='https://developer-api.nest.com/?auth='+token
    r = requests.get(url)
    response = r.json()
    for element in response['devices']['thermostats']:
        if element == id1:
            return response['devices']['thermostats'][element]['target_temperature_f']
    return 99

def setTemperature(parameter, value):
    headers = {'content-type':'application/json'}
    data = value
    url = 'https://developer-api.nest.com/devices/thermostats/'+id1+'/'+parameter+'?auth='+token
    try:
        r = requests.put(url, data=json.dumps(data), headers=headers, allow_redirects=True)
    except Exception, e:
        return False
    response = json.loads(r.content)
    if response == value:
       return True
    else:
       return False

if __name__ == '__main__':
    print getTemperature()
    print str(setTemperature('target_temperature_f',72))
