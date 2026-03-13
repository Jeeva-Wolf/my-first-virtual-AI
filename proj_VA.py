import pyttsx3
import speech_recognition as sr
import wikipedia
from datetime import datetime 
import random
import os
import subprocess 
import time

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate",170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# Speech recognition
def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=7)
            command = r.recognize_google(audio, language="en-IN")
            print("You said:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            return ""

        except Exception as e:
            print("Error:", e)
            return ""
        

def ask_quiz():
    while True:
        speak("Welcome to the quiz game!")

        # Question 1
        speak("Question 1. What is the capital of India?")
        speak(" Chennai")
        print('a.Chennai')
        speak(" Delhi")
        print('b.Dehli')
        speak(" Mumbai")
        print('c.Mumbai')
        answer1 = recognize_speech()

        if 'delhi' in answer1:
            speak("Correct! The capital of India is Delhi!")
        else:
            speak("Incorrect! The capital of India is Delhi.")

        # Question 2
        speak("Question 2. What is the full form of CD?")
        speak(" Control Data")
        print('a.Control Data')
        speak(" Control Disk")
        print('b.Control Disk')
        speak(" Compact Disk")
        print('c.Compact Disk')
        answer2 = recognize_speech()

        if 'compact disk' in answer2:
            speak("Correct! The full form of CD is Compact Disk.")
        else:
            speak("Incorrect! The full form of CD is Compact Disk.")

        # Question 3
        speak("Question 3. What is the largest planet in our solar system?")
        speak(" Earth")
        print("a.Earth")
        speak(" Jupiter")
        print('b.Jupiter')
        speak(" Saturn")
        print('c.Saturn')
        answer3 = recognize_speech()

        if 'jupiter' in answer3:
            speak("Correct! The largest planet is Jupiter!")
        else:
            speak("Incorrect! The largest planet is Jupiter.")   

        speak("Thank you for participating in the quiz game.")
        repeat()

def wikipedia_search():
    while True:  
        speak("Tell me a word! to search?")
        query = recognize_speech()

        if query:
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia: {result}")
            except wikipedia.DisambiguationError:
                speak(f"There are multiple results for {query}. Please be more specific.")
            except wikipedia.PageError:
                speak(f"Sorry, I couldn't find any information on {query}.")
        else:
            speak("I didn't hear your query.")

    
        speak("Would you like to ask another question or go back to the main menu?")
        command = recognize_speech()
        
        if 'back' in command or 'menu' in command:
            speak("Going back to the main menu.")
            repeat()
            break

def what_are_you_doing():
    while True:
        replies=['i am taking commands from my captain.','talking with my dear sir.','waiting for.  my commands from you!.']
        speak(random.choice(replies))
        repeat()
    
    
def who_are_you():
    replies=['I am your lovely personal assistant.', 'iam your voice assistant']
    speak(random.choice(replies))
    
    
def how_am_i(): 
    replies =['You are goddamn handsome!','You look like the kindest person that I have met.','you looking so beautiful'] 
    speak(random.choice(replies))
 
 
def tell_joke(): 
    jokes = ['10   20 .  30   40   50.  what comes.  after 50...  any guess....  you think its 60..  your wrong its 51','two friends. going in the bike.  one friend said. iam hungry. the other friend. stop bike fastly. is hunger got over. how. any guesses.. because he put the break fastly. that why breakfast']
    speak(random.choice(jokes))  
    
    
def where_born(): 
    speak('I was created by a Python code by. jeevaa')
    
def age():
    speak('No age for me. because iam a machine ')      
         

def how_are_you(): 
    speak('I am fine sir, thank you.')

    
def what_you_can_do():
    replies=['you can say to read. any  artical from wikipedia.','you can ask me general questions. or you can ask also jokes.']     
    speak(random.choice(replies))   
    speak('and many more sir! ')
      
def play_random_song():
    songs = os.listdir('D:/songs')
    song = random.choice(songs)
    song_path = os.path.join('D:/songs', song)
    
    speak(f"Playing {song}")

    subprocess.Popen(['start', '', song_path], shell=True)

    time.sleep(40) 

    speak("The song has finished playing.")
    repeat()  

def exit_0():
    speak('thank you. goodbye.')
    exit()

def my_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M %p")  
    speak(f"The current time is {current_time}.")
    print(f"The current time is {current_time}.")

def my_date():
    now = datetime.now()
    current_date = now.strftime("%B %d, %Y")  
    speak(f"Today's date is {current_date}.")
    print(f"Today's date is {current_date}.")    

def repeat():
    speak('tell me. what want to do')   
    while True:  
        command = recognize_speech()

        if 'quiz' in command:
            ask_quiz()
            break  
        elif 'wiki' in command or 'wikipedia' in command:
            wikipedia_search()
            break  
        elif 'doing' in command :
            what_are_you_doing()
            break
        elif 'how are you' in command:
            how_are_you()

        elif 'who created you' in command or 'where did you born' in command:
            where_born()
        elif 'age' in command:
            age()
        elif 'look' in command:
            how_am_i()
        elif 'joke' in command:
            tell_joke()
        elif 'who are you' in command:
            who_are_you()
        elif 'do' in command:
            what_you_can_do()    
        elif 'date' in command:
            my_date()
        elif 'time' in command:
            my_time()     
        elif 'exit' in command or 'bye' in command or 'stop' in command:
            exit_0()  
        elif 'hello' in command or 'hi' in command:
            speak('hello. whatsapp. nice to meet you')   
        elif 'song' in command:
            play_random_song()         
        else:
            speak("Sorry, I didn't catch that. Please say it slowly. ")

       
def main():

    speak("Hello! I am your voice assistant!")
    speak("What can I do for you today?")

    speak("You can say 'Wikipedia'.  to search a word, or ask me gendral questions, or we can play a quiz game. or, i can also play a song.")

    while True:  
        command = recognize_speech()

        if 'quiz' in command:
            ask_quiz()
            break  
        elif 'wiki' in command or 'wikipedia' in command:
            wikipedia_search()
            break  
        elif 'doing' in command:
            what_are_you_doing()
            break
        elif 'how are you' in command:
            how_are_you()

        elif 'who created you' in command or 'where did you born' in command:
            where_born()

        elif 'do' in command:
            what_you_can_do()

        elif 'age' in command:
            age()
        elif 'look' in command:
            how_am_i()
        elif 'joke' in command:
            tell_joke()
        elif 'who are you' in command:
            who_are_you()
        elif 'date' in command:
            my_date()
        elif 'time' in command:
            my_time()     
        elif 'exit' in command or 'bye' in command or 'stop' in command:
            exit_0()  
        elif 'hello' in command or 'hi' in command:
            speak('hello. whatsapp. nice to meet you')   
        elif 'song' in command:
            play_random_song()         
        else:
            speak("Sorry, I didn't catch that. Please say correctly. or repeat it ")

obj=main()
