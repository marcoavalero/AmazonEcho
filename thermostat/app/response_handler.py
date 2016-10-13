import sys
import json
from nest import getTemperature
from nest import setTemperature
from default_responses import outputSpeechTextDefault
from default_responses import outputSpeechTypeDefault
from default_responses import cardTypeDefault
from default_responses import cardTitleDefault
from default_responses import cardContentDefault
from default_responses import shouldEndSession

UPDATE_FACTOR=2

def request_handler(request):
    currentRequest = request['request']
    response = request_parser(currentRequest)
    return json.dumps({"version":"1.0","response":response})

def request_parser(request):
    requestType = request['type']
    if requestType == "LaunchRequest":
        return launch_request(request)
    elif requestType == "IntentRequest":
        return intent_request(request)
    else:
        return launch_request(request)

def launch_request(request):
    return build_response()

def intent_request(request):
    if request['intent']['name'] ==  "Increase":
        reponse = increaseT(request)
    if request['intent']['name'] ==  "Reduce":
        reponse = reduceT(request)
    if request['intent']['name'] ==  "Update":
        reponse = updateT(request)
    return reponse

def increaseT(request):
    current = getTemperature()
    newtemp = int(current)+UPDATE_FACTOR
    attemp  = setTemperature('target_temperature_f', newtemp)
    if attemp:
        responseSpeech = "Increasing temperature to %d degrees"%newtemp
        cardContent    = "Increasing temperature to %d degrees"%newtemp
    else:
        responseSpeech = "Failed to increase temperature"
        cardContent    = "Failed to increase temperature"
    return build_response(outputSpeechText=responseSpeech,
                          cardContent=cardContent,
                          shouldEndSession=True)

def reduceT(request):
    current = getTemperature()
    newtemp = int(current)-UPDATE_FACTOR
    attemp  = setTemperature('target_temperature_f', newtemp)
    if attemp:
        responseSpeech = "Reducing temperature to %d degrees"%newtemp
        cardContent    = "Reducing temperature to %d degrees"%newtemp
    else:
        responseSpeech = "Failed to reduce temperature"
        cardContent    = "Failed to reduce temperature"
    return build_response(outputSpeechText=responseSpeech,
                          cardContent=cardContent,
                          shouldEndSession=True)

def updateT(request):
    temperature = int(request['intent']['slots']['temp']['value'])
    attemp  = setTemperature('target_temperature_f', temperature)
    if attemp:
        responseSpeech = "Setting temperature to %s degrees"%str(temperature)
        cardContent    = "Setting temperature to %s degrees"%str(temperature)
    else:
        responseSpeech = "There was an error adjusting the temperature"
        cardContent    = "There was an error adjusting the temperature"
    return build_response(outputSpeechText=responseSpeech,
                          cardContent=cardContent,
                          shouldEndSession=True)

def build_response(outputSpeechText=outputSpeechTextDefault, 
                   outputSpeechType=outputSpeechTypeDefault,
                   cardType=cardTypeDefault,
                   cardTitle=cardTitleDefault,
                   cardContent=cardContentDefault,
                   shouldEndSession=False):
    response = {"outputSpeech": {"type": outputSpeechType, 
                                 "text": outputSpeechText},
                "card": {"type": cardType, 
                         "title": cardTitle, 
                         "content":cardContent},
                "shouldEndSession": shouldEndSession}
    return response
