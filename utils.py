import os
import random
from workingcode import youtube_search_keyword
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "assignment-psydel-da7b8d90b0e7.json"

from pymongo import MongoClient
client = MongoClient("mongodb+srv://youtubebot:cnC4.H62_XThAv5@cluster0-xhmtv.mongodb.net/test?retryWrites=true&w=majority")
db=client.get_database("youtubebotname")
records = db.userdata



import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()

PROJECT_ID = "assignment-psydel"

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(msg, session_id):
	response = detect_intent_from_text(msg, session_id)
	print('util')
	y=[]
	y = dict(y)
	y[session_id]=msg
	records.insert_one(y)
	print('till here')

	print('database working')
	if response.intent.display_name == 'get_video':

		print('here in utils file')
		video = dict(response.parameters)
		if type(video.get('topic'))=='list':
			print(type(video.ger('topic')))
			topicname = video.get('topic')[0]
		else:
			topicname = video.get('topic')
		query = "{} {} {} {} {}".format(topicname ,video.get('channel_name') ,video.get('data_type') ,video.get('geo-country') , video.get('language') , video.get('video_type'))
		print(video)
		p=""
		print(query)
		finalstring = youtube_search_keyword(str(query)  , video, max_results=7)
		print(str(finalstring))
		return str(finalstring),p
	elif response.intent.display_name == 'pfeedback':
		p=""
		positive = ['I am really happy that you like me!!!! 😁' , 'Happy to serve you 😎' , "it's just kind of you 😄" , 'I am happy you are happy 😁' , 'You are Awesome 🤘']

		return positive[random.randrange(0 ,len(positive))] ,p
	elif response.intent.display_name == 'nfeedback':
		p=""
		negative = ['Sorry to disappoint you 😟' , 'will surely imporve 😞' ,' I am Still in beta phase 😕' , 'That is sad 😔' , 'Hope you are not angry with me 🥺']
		return negative[random.randrange(0, len(negative))],p
	elif response.intent.display_name == 'info':
		p="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoUO0V_5uWey2jhMwqun078nUrFIbDzbwX_slnSCCriewm4esCdw"
		return '''I am Shutterclosed bot Created by Puru Arora 
I am a AI based bot who is ready to serve you with amazing content from youtube at any moment.
I provide you an easy way to fetch information from YOUTUBE to share on Whatsapp without the need to go to Youtube app.
Enjoy.
Git Hub profile = https://www.github.com/puruarora12
Follow him on Instagram - https://www.instagram.com/shutterclosed
		
		''',p
	elif response.intent.display_name=='help':
		p="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoUO0V_5uWey2jhMwqun078nUrFIbDzbwX_slnSCCriewm4esCdw"
		return '''My working is very simple.
just search what you want to search on youtube followed by video
if i fail to give results try with a keyword like video , channel , playlist or any other keyword that better describes your query
ex  's10 review by shutterclosed video'
		
		''',p

	elif response.intent.display_name=='Default Welcome Intent':
		print("hello")
		p = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoUO0V_5uWey2jhMwqun078nUrFIbDzbwX_slnSCCriewm4esCdw"
		return response.fulfillment_text,p

	else:
		p=''
		return response.fulfillment_text ,p
