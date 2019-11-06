import datetime
import pyaudio
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import sqlite3
import requests
from googletrans import Translator
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak now....")
		audio = r.listen(source)
		r.pause_threshold = .5
		# r.energy_threshold = 400
		try:
			print("Recogizing.....")
			query = r.recognize_google(audio,language = 'en-in')
		except:
			print("sorry")
			return "none"
	return query

def name():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		r.pause_threshold = .10
		# r.energy_threshold = 400
		try:
			name = r.recognize_google(audio,language = 'en-in')
		except:
			return "none"
	return query
	#return query

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def wish():
	hour = int(datetime.datetime.now().hour)
	if hour>0 and hour<12:
		speak("good morning, master")
	elif hour ==12 and hour<18:
		speak("good afternoon , master")
	else:
		speak("good evening , master")

def temperature(city):
	api_add = f'http://api.openweathermap.org/data/2.5/weather?appid=1ff1ec03072dc3e27d75e920aebd67a9&q={city}&units=metric'
	
	json_data = requests.get(api_add).json()
	temp = json_data["main"]["temp"]
	cond = json_data["weather"][0]["description"]
	name = json_data["name"]
	speak(f"temperature of {name} is {temp} degree celcius and the condition is {cond}")
	print(f"temperature of {name} is {temp} degree celcius and the condition is {cond}")



# def remind(job):
# 	speak(job)
# 	conn = sqlite3.connect('reminder.db')
# 	c = conn.cursor()
# 	c.execute("INSERT INTO jobs VALUES ('2006-01-05', 'slepping')")
# 	conn.commit()
# 	conn.close()

# def fetchreminder():
# 	conn = sqlite3.connect('reminder.db')
# 	c = conn.cursor()
# 	c.execute("CREATE TABLE jobs (date text,task text) IF NOT EXISTS")
# 	c.execute("SELECT * FROM jobs")
# 	data = c.fetchall()
# 	conn.close()
# 	speak(f"you have remind me that {data}")

if __name__=="__main__":
	wish()
	speak("Tell me the access code")
	name = name().lower()
	print(name)
	if "hello" in name:

		speak("hello master i am jack , how may i help you")
		while True:
			query = command().lower()
			later =  query[0:9]

			if 'wikipedia' in query:
				speak("searching wikipedia..")
				query = query.replace("wikipedia","")
				results = wikipedia.summary(query,sentences=2)
				speak(results)
				print(results)

			elif 'play mp4' in query:
				mp4_dir = "C:\\Users\\saura\\Videos"
				video = os.listdir(mp4_dir)
				c = 0
				vlist = []
				for x in video:
					c=c+1
					vlist.append(c)
				idx = random.choice(vlist)
				os.startfile(os.path.join(mp4_dir,video[idx]))
				speak("just a second master, playing a lovely video song for you")
				print("playing music video")


			elif 'show photos' in query:
		   		images_dir = "C:\\Users\\saura\\OneDrive\\Pictures\\cmera"
		   		Pictures = os.listdir(images_dir)
		   		d = 0
		   		plist = []
		   		for x in Pictures:
		   			d=d+1
		   			plist.append(d)
		   			idx = random.choice(plist)
		   		os.startfile(os.path.join(images_dir,Pictures[idx]))
		   		speak("just a second master, showing your photos")


			elif 'youtube' in query:
				speak("opening youtube..")
				webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

			elif 'facebook' in query:
				speak("opening facebook..")
				webbrowser.open(f"https://www.facebook.com/")

			elif 'the time' in query:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")		
				speak(f"master, the time is {strTime}")

			elif 'close' in query:
				speak("okay master , as your wish , im leaving bye bye , take  care ")
				break
			
			# elif 'remind me' in later:
			# 	reminder = query[9:]
			# 	remind(reminder)

			# elif 'what i remind you' in query:
			# 	fetchreminder()

			elif 'translate' in query:
				tword = query[9:]
				translator = Translator()
				lang = translator.translate(tword , dest = 'la')
				speak(lang.text)
				print(lang)

			elif "temperature of" in query:
				speak("please wait")
				idx = query.index("f")+ 2
				city = query[idx:]
				temperature(city)

			
			elif 'love you' in query:
				engine.setProperty('voice',voices[1].id)
				speak("WOW , thank you so much , you are so cute , your partner should be so lucky.., love you infinity bae..")

			else:
				speak("searching on google..")
				webbrowser.open(f"https://www.google.com")


	else:
		speak("sorry you are not my master")
