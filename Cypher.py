import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import random
import requests
import json
import subprocess
import pyjokes
import sys
import operator
import pyautogui
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from flask import request
import wolframalpha

greetings = ["Cypher this side, at your service sir"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    greet = random.choice(greetings)

    speak(greet)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.phrase_threshold = 0.5
        r.energy_threshold = 50
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User : {query}\n")

    except Exception:
        speak('Say that again please')
        print("Say that again pls.....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mukundtaneja2004@gmail.com', "!@#MT149")
    server.sendmail('mukundtaneja2004@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    ############# FOR MY SNAKE WATER GUN GAME ##############
    number_of_turns = 1
    computer_point = 0
    your_point = 0
    l = ["s", "p", "sc"]
    ############# FOR MY SNAKE WATER GUN GAME ##############
    while True:
        query = takeCommand().lower()
        if 'according to wikipedia' in query:
            try:
                speak('Hold on sir')
                query = query.replace("according to wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry I did not get any results")


        elif 'news' in query:
            speak('News for today')
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=ba33177cb9874551a67ef5abf4f9f773"
            news = requests.get(url).text
            news = json.loads(news)
            arts = news['articles']
            for i in range(0,5):
                print(arts[i]['title'])
                speak(arts[i]['title'])
                speak('Next,')
            speak('Thats all for today')


        elif 'game' in query:
            speak('Which game do you wanna play, I have stone paper scissor and guess the number')
            g = takeCommand()
            if g == "stone paper scissor":
                speak('Lets play stone paper scissor')
                print("s for stone\n p for scissor\n sc for scissor")
                while (number_of_turns <= 10):
                    c = input("Enter here:-\n")
                    a = random.choice(l)
                    print(a)
                    if c == "p" and a == "s":
                        your_point = your_point + 1
                        speak(f"your guess was {c} and my guess was {a}")
                        print(f"your guess was {c} and my guess was {a}")
                        print(f"Your point is {your_point} and my point is {computer_point}")
                        speak(f"Your point is {your_point} and my point is {computer_point}")
                        print(10 - number_of_turns, "number of turns left")
                        speak(f"{10 - number_of_turns}, number of turns left")
                        number_of_turns = number_of_turns + 1
                    elif c == "sc" and a == "p":
                        your_point = your_point + 1
                        print(f"Your guess was {c} and my guess was {a}")
                        speak(f"Your guess was {c} and my guess was {a}")
                        print(f"my point is {computer_point} and your point is {your_point}\n")
                        speak(f"my point is {computer_point} and your point is {your_point}\n")
                        print(10 - number_of_turns, "number of turns left\n")
                        speak(f"{10 - number_of_turns}, number of turns left\n")
                        number_of_turns = number_of_turns + 1
                        continue
                    elif c == "s" and a == "sc":
                        your_point = your_point + 1
                        print(f"Your guess was {c} and my guess was {a}")
                        speak(f"Your guess was {c} and my guess was {a}")
                        print(f"my point is {computer_point} and your point is {your_point}\n")
                        speak(f"my point is {computer_point} and your point is {your_point}\n")
                        print(10 - number_of_turns, "number of turns left\n")
                        speak(f"{10 - number_of_turns}, number of turns left\n")
                        number_of_turns = number_of_turns + 1
                        continue
                    elif c == a:
                        your_point = your_point
                        computer_point = computer_point
                        print(f"Your guess was {c} and my guess was {a}")
                        speak(f"Your guess was {c} and my guess was {a}")
                        print(f"my point is {computer_point} and your point is {your_point}\n")
                        speak(f"my point is {computer_point} and your point is {your_point}\n")
                        print(10 - number_of_turns, "number of turns left\n")
                        speak(f"{10 - number_of_turns}, number of turns left\n")
                        number_of_turns = number_of_turns + 1
                        continue
                    elif c != l:
                        print("please type the correct value")
                        speak("please type The Correct Value")
                        print(f"my point is {computer_point} and your point is {your_point}")
                        speak(f"my point is {computer_point} and your point is {your_point}")
                        print(10 - number_of_turns, "number of turns left\n")
                        speak(f"{10 - number_of_turns}, number of turns left\n")
                        number_of_turns = number_of_turns + 1
                        continue
                    elif c == "sc" and a == "s":
                        computer_point = computer_point + 1
                        speak(f"Your guess was {c} and my guess was {a}")
                        print(f"Your guess was {c} and my guess was {a}")
                        speak(f"My point is {computer_point} and your point is {your_point}\n")
                        print(f"My point is {computer_point} and your point is {your_point}\n")
                        print(10 - number_of_turns, "number of turns left\n")
                        speak(f"{10 - number_of_turns}, number of turns left\n")
                        number_of_turns = number_of_turns + 1
                        continue
                    elif c == "s" and a == "p":
                        computer_point = computer_point + 1
                        speak(f"Your guess was {c} and my guess was {a}")
                        print(f"Your guess was {c} and my guess was {a}")
                        speak(f"My point is {computer_point} and your point is {your_point}\n")
                        print(f"My point is {computer_point} and your point is {your_point}\n")
                        print(10 - number_of_turns, "number of turns left\n")
                        speak(f"{10 - number_of_turns}, number of turns left\n")
                        number_of_turns = number_of_turns + 1
                        continue
                    elif c == "p" and a == "sc":
                        computer_point = computer_point + 1
                        speak(f"Your guess was {c} and my guess was {a}")
                        print(f"Your guess was {c} and my guess was {a}")
                        speak(f"My point is {computer_point} and your point is {your_point}\n")
                        print(f"My point is {computer_point} and your point is {your_point}\n")
                        print(10 - number_of_turns, "number of turns left\n")
                        speak(f"{10 - number_of_turns}, number of turns left\n")
                        number_of_turns = number_of_turns + 1
                        continue

                if number_of_turns == 10:
                    print(f"Your points were {your_point} and my points were {computer_point}\n")
                    speak(f"Your points were {your_point} and my points were {computer_point}\n")

                if your_point > computer_point:
                    print(f"!!!!!! YOU WON !!!!!! BY {your_point - computer_point} points")
                    speak(f"!!!!!! YOU WON !!!!!! BY {your_point - computer_point} points")
                elif your_point == computer_point:
                    print("!!!!!! IT'S A TIE !!!!!!")
                    speak("!!!!!! IT'S A TIE !!!!!!")
                else:
                    print(f"!!!!!! YOU LOSE !!!!!! BY {computer_point - your_point} points")
                    speak(f"!!!!!! YOU LOSE !!!!!! BY {computer_point - your_point} points")

            if g == "guess the number":
                n = random.randint(50, 100)
                r = random.randint(1, 10)
                w = random.randint(10, 20)
                number_of_guesses = 1
                print("WELCOME TO GUESS THE NUMBER CHALLENGE \n ")
                print("Try To Guess The Number Between", int(n - r), "and", int(n + w))
                speak(f"Try To Guess The Number Between {int(n - r)} and {int(n + w)}")
                print("You will get only 9 chance")
                speak('You will get only 9 chance')
                while (number_of_guesses <= 9):
                    num1 = int(input(" \n Enter a number to start \n "))
                    if num1 < n - r or num1 > n + w:
                        print("Type the number between the sequence", int(n - 10), "and", int(n + 10))
                        speak(f"Type the number between the sequence of {int(n - 10)} and {int(n + 10)}")
                        print(9 - number_of_guesses, "no. of guesses left")
                        speak(f"{9 - number_of_guesses} number of guesses left")
                        number_of_guesses = number_of_guesses + 1
                    elif num1 > n:
                        print("Oooops!!!!!!!! \n Think of a smaller number")
                        speak("Oooops, Think of a smaller number")
                        print(9 - number_of_guesses, "no. of guesses left")
                        speak(f"{9 - number_of_guesses} number of guesses left")
                        number_of_guesses = number_of_guesses + 1
                        continue
                    elif num1 < n:
                        print("Oooops!!!!!!!! \n Think of a larger number")
                        speak("Oooops, Think of a larger number")
                        print(9 - number_of_guesses, "no. of guesses left")
                        speak(f"{9 - number_of_guesses} number of guesses left")
                        number_of_guesses = number_of_guesses + 1
                        continue
                    else:
                        print("You Guessed The Number \n YOU WON!!!!!!\n")
                        speak("You Guessed The Number, YOU WON")
                        print(number_of_guesses, "guesses you took to finish")
                        speak(f"{number_of_guesses} guesses you took to finish")
                        break

                if number_of_guesses > 9:
                    print("!!!!!!!!GAME OVER!!!!!!!!")
                    speak("!!!!!!!!GAME OVER!!!!!!!!")
                    print(f"The number was {n}")
                    speak(f"The number was {n}")
                    continue

        elif 'valorant' in query:
            valorant = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            speak('opening valorant, Please wait a while')
            os.startfile(valorant)

        elif 'close valorant' in query:
            speak('closing valorant')
            os.system("taskkill /f /im RiotClientServices.exe")

        elif 'rest' in query:
            try:
                speak('For how much time should I sleep')
                n = takeCommand()
                sleep = n.replace("seconds" or "second" or "2nd", "")
                speak('Going for a short nap')
                time.sleep(int(sleep))
                speak('I am back, Now tell me what to do')
            except Exception:
                continue

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'shut down' in query:
            speak('are you sure sir you want to exit')
            shut = takeCommand()
            if 'yes' in shut:
                os.system("shutdown /s /t 10")
            else:
                continue

        elif 'restart' in query:
            speak('are you sure sir')
            r1 = takeCommand()
            if 'yes' in r1:
                os.system("shutdown /r /t 10")
            else:
                continue

        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 10:
                speak('Sir please wake')
            strtime = datetime.datetime.now().strftime("%I:%M")
            newtime = strtime.replace("hour" and "minute", "" and "")
            speak(f"Sir, The time is {newtime}")
            api_key = "24b1a773451de8c98e442f9318d05b34"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            city_name = "amritsar"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature = current_temperature - 273
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak('the temperature outside is %.0f' % current_temperature + 'degree')
                speak(
                    f"\nhumidity is {str(current_humidiy)}percent\ntoday the atmosphere consist of {str(weather_description)}")
                print('outside temperatue is %.0f' % current_temperature + ' degree')
                print(
                    f"humidity is {str(current_humidiy)}%\ntoday, the atomosphere consisit of {str(weather_description)}")

        elif "weather" in query:
            api_key = "24b1a773451de8c98e442f9318d05b34"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature = current_temperature - 273
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak('the temperature outside is %.0f' % current_temperature + 'degree')
                speak(
                    f"\nhumidity is {str(current_humidiy)}percent\ntoday the atmosphere consist of {str(weather_description)}")
                print('outside temperatue is %.0f' % current_temperature + ' degree')
                print(
                    f"humidity is {str(current_humidiy)}%\ntoday, the atomosphere consisit of {str(weather_description)}")

        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak('sir please tell me the name for this screenshot')
            name = takeCommand().lower()
            speak('sir please hold while I take the screenshot')
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Sir, the screenshot is saved in your main folder")

        elif 'hi' or 'hey' or 'hello' in query:
            reply = ('hi sir', 'hello i am cypher', 'hello there')
            speak(random(reply))
            print(random(reply))

        elif 'so good' in query:
            speak('Because I was made by Mukund Taneja')

        elif 'how are you' or 'are you fine' in query:
            greets = ('i am fine', 'absolutely fine sir', 'excellent')
            speak(random(greets))
            print(random(greets))

        elif 'thank you' or 'thanks' in query:
            welcome = ('most welcome, sir', 'no problem sir')
            speak(random(welcome))
            print(random(welcome))

        elif 'fine' in query:
            speak('Nice to listen, Sir')


        elif 'nice' in query:
            speak('Thank you sir')

        elif 'owner' in query:
            speak('The legend of all time, Mister Mukund taneja is my master')

        elif 'addition' in query:
            speak('What is the first number')
            val1 = int(input("Enter your first numbert\n"))
            speak('What is your second number')
            val2 = int(input("Enter your second number\n"))
            speak(f"The sum of {val1} and {val2} is {val1 + val2}")
            print(f"The sum of {val1} and {val2} is {val1 + val2}")

        elif 'subtract' in query:
            speak('What is the first number')
            val3 = int(input("Enter your first numbert\n"))
            speak('What is your second number')
            val4 = int(input("Enter your second number\n"))
            speak(f"The sum of {val3} and {val4} is {val3 - val4}")
            print(f"The sum of {val3} and {val4} is {val3 - val4}")


        elif 'multiply' in query:
            speak('What is the first number')
            val5 = int(input("Enter your first numbert\n"))
            speak('What is your second number')
            val6 = int(input("Enter your second number\n"))
            speak(f"The product of {val5} and {val6} is {val5 * val6}")
            print(f"The product of {val5} and {val6} is {val5 * val6}")


        elif 'divide' in query:
            speak('What is the first number')
            val7 = int(input("Enter your first numbert\n"))
            speak('What is your second number')
            val8 = int(input("Enter your second number\n"))
            speak(f"On dividing {val7} from {val8} the answer is {val7 / val8}")
            print(f"On dividing {val7} from {val8} the answer is {val7 / val8}")


        elif 'square' in query:
            speak('What is the number')
            val9 = int(input("Enter the number"))
            speak(f"The square of {val9} is {val9 * val9}")
            print(f"The square of {val9} is {val9 * val9}")


        elif 'cube' in query:
            speak('What is the number')
            val0 = int(input("Enter the number"))
            speak(f"The cube of {val0} is {val0 * val0 * val0}")
            print(f"The cube of {val0} is {val0 * val0 * val0}")

        elif 'do some calculation' in query or 'can you calculate' in query:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak('say what you want me to calculate')
                    print("Listening.......")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)


                    def get_operator_fn(op):
                        return {'+': operator.add,
                                '-': operator.sub,
                                'x': operator.mul,
                                'divided by': operator.truediv,
                                }[op]


                    def eval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)


                    speak('your result is')
                    speak(eval_binary_expr(*(my_string.split())))
                    print("Your result is")
                    print(eval_binary_expr(*(my_string.split())))
            except Exception as e:
                speak('I could not get you, Please ask again for calculation')


        elif 'where i am' in query or 'where are we' in query or 'where am i' in query:
            try:
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
                geo_request = requests.get(url)
                geo_data = geo_request.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir I think we are in the {city} city of {country}")
            except Exception as e:
                speak('Sorry sir, due to network issues i am not able to find where we are')
                print(e)

        elif 'open youtube' in query:
                speak('opening youtube')
                webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("https://www.google.com")

        elif 'close google' in query:
            speak('Closing google')
            os.system("taskkill /f /im brave.exe")

        elif 'gmail' in query:
            speak('ok sir, opening your account')
            webbrowser.open("gmail.com")

        elif 'open facebook' in query:
                speak('opening facebook')
                webbrowser.open("https://www.facebook.com/")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%I:%M")
            newtime = strtime.replace("hour" and "minute", "" and "")
            speak(f"Sir, The time is {newtime}")

        elif 'date' in query:
            date = int(datetime.datetime.now().day)
            month = int(datetime.datetime.now().month)
            year = int(datetime.datetime.now().year)

            speak(f"Sir, the date is {date} {month} {year}")

        elif 'open code' in query:
            speak('Opening visual studio code for your coding purpose')
            codepath = "C:\\Users\\MUKUND\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open epic games' in query:
            epic = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
            speak('ok sir, opening epic games')
            os.startfile(epic)

        elif 'close collection' in query:
            speak("ok sir, closing epic games")
            os.system("taskkill /f /im EpicGamesLauncher.exe")

        elif 'telegram' in query:
            try:
                speak('Opening telegram')
                msg = " C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe "
                os.startfile(msg)
            except Exception as e:
                print("cannot open telegram at the moment sir")
                speak('cannot open telegram at the moment sir')

        elif 'question' in query:
            speak('what is your question')
            while True:
                try:
                    question1 = takeCommand()

                    if 'stop' in question1:
                        speak("ok sir")
                        print("ok sir")
                        break
    
                    app_id = "26YJL4-K5PP27G9X2"
                    client = wolframalpha.Client(app_id) 

                    res = client.query(question1) 

                    answer = next(res.results).text 
                    speak(answer)
                    print(answer)
                    speak('next question please')
                except Exception as e:
                    speak('i dont know about that sir')
                    print('i dont know about that sir')
                    speak('next question pls')
                    continue

        elif 'close telegram' in query:
            speak('ok sir, closing telegram')
            os.system("taskkill /f /im Telegram.exe")

        elif 'open steam' in query:
                speak('Opening steam, Please wait a while')
                games = "C:\\Program Files (x86)\\Steam\\steam.exe"
                os.startfile(games)

        elif 'close steam' in query:
            speak('ok sir, closing steam')
            os.system("taskkill /f /im steam.exe")

        elif 'email to anupama' in query:
            try:
                speak("what should I say ?")
                content = takeCommand()
                to = "7837anu@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry Sir, I am not able to send this email a the moment")
                print("Sorry Sir, 7not able to send this email a the moment")
                print(e)

        elif 'exit' in query or 'leave' in query:
            speak('Are you sure Sir ?')
            ex = takeCommand()
            if "yes" in ex or "proceed" in ex:
                speak('Going to exit, Bye bye ,')
                break
            else:
                speak('On your command')
                continue

        elif 'search' in query:
            question = query.replace("search", "")
            speak('searching google')
            webbrowser.open('https://www.google.com/search?q=' + question)

