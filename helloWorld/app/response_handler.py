import sys
import json
from default_responses import outputSpeechTextDefault
from default_responses import outputSpeechTypeDefault
from default_responses import cardTypeDefault
from default_responses import cardTitleDefault
from default_responses import cardContentDefault
from default_responses import shouldEndSession

peopleList   = ['Nick','Doctor Raj','Doctor King','Marco']
messagesList = {'Nick': 'You need to call Dr. Alex A.S.A.P',
              'doctor Raj': 'Lets go and get a coffee after the presentation',
              'doctor King': 'Is the Automata qualifier ready?',
              'Marco':'It is time to move on with the presentation'}

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
    if request['intent']['name'] ==  "Help":
        reponse = helpme(request)
    if request['intent']['name'] ==  "Hello":
        reponse = hello(request)
    if request['intent']['name'] ==  "GetNames":
        reponse = get_names(request)
    if request['intent']['name'] ==  "GetMessages":
        reponse = get_messages(request)
    if request['intent']['name'] ==  "Bye":
        reponse = bye(request)
    return reponse

def helpme(request):
    return build_response()

def hello(request):
    personName = request['intent']['slots']['person']['value']
    responseSpeech = "Hello %s"%personName
    cardContent    = "Hello %s"%personName
    return build_response(outputSpeechText=responseSpeech,
                          cardContent=cardContent,
                          shouldEndSession=True)

def get_names(request):
    responseSpeech = "There are %d people in the list. "%len(peopleList)
    for person in peopleList:
        responseSpeech = responseSpeech + person + " , "
    cardContent = "Get Names"
    return build_response(outputSpeechText=responseSpeech,
                          cardContent=cardContent,
                          shouldEndSession=True)

def get_messages(request):
    personName = request['intent']['slots']['person']['value']
    if personName not in messagesList:
        responseSpeech = "%s is an invalid user"%personName
        cardContent    = "%s is an invalid user"%personName
    else:
        responseSpeech = "%s"%messagesList[personName]
        cardContent    = "%s"%messagesList[personName]
    return build_response(outputSpeechText=responseSpeech,
                          cardContent=cardContent,
                          shouldEndSession=True)

def bye(request):
    personName = request['intent']['slots']['person']['value']
    responseSpeech = "Bye %s"%personName
    cardContent    = "Bye %s"%personName
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
