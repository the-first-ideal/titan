import random

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import pyaudio
import time
import ctypes

# credit to mmirthula02 for the beginning framework of Titan.
# credit to Paradoxis for the class Keyboard and class Sound.
# licensing information for SpeechRecognition can be found within the SpeechRecognition README,
# and make sure SpeechRecognition is visible to users if they wish to see it.

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')
engine.setProperty('rate', 150)  # setting up new voice rate

# Import the SendInput object
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greetings():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif 12 <= hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Titan is listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said:{statement}\n")

        except Exception as e:
            # speak("Pardon me, please say that again")
            print("Waiting for user to say something.")
            return "None"
        return statement


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort), ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong), ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong), ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long), ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong), ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong), ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput), ("mi", MouseInput), ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong), ("ii", Input_I)]


class Keyboard:
    # Keyboard key constants
    # More information: https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
    VK_BACKSPACE = 0x08
    VK_ENTER = 0x0D
    VK_CTRL = 0x11
    VK_ALT = 0x12
    VK_0 = 0x30
    VK_1 = 0x31
    VK_2 = 0x32
    VK_3 = 0x33
    VK_4 = 0x34
    VK_5 = 0x35
    VK_6 = 0x36
    VK_7 = 0x37
    VK_8 = 0x38
    VK_9 = 0x39
    VK_A = 0x41
    VK_B = 0x42
    VK_C = 0x43
    VK_D = 0x44
    VK_E = 0x45
    VK_F = 0x46
    VK_G = 0x47
    VK_H = 0x48
    VK_I = 0x49
    VK_J = 0x4A
    VK_K = 0x4B
    VK_L = 0x4C
    VK_M = 0x4D
    VK_N = 0x4E
    VK_O = 0x4F
    VK_P = 0x50
    VK_Q = 0x51
    VK_R = 0x52
    VK_S = 0x53
    VK_T = 0x54
    VK_U = 0x55
    VK_V = 0x56
    VK_W = 0x57
    VK_X = 0x58
    VK_Y = 0x59
    VK_Z = 0x5A
    VK_VOLUME_MUTE = 0xAD
    VK_VOLUME_DOWN = 0xAE
    VK_VOLUME_UP = 0xAF
    VK_MEDIA_NEXT_TRACK = 0xB0
    VK_MEDIA_PREV_TRACK = 0xB1
    VK_MEDIA_PLAY_PAUSE = 0xB3
    VK_MEDIA_STOP = 0xB2
    VK_LBUTTON = 0x01
    VK_RBUTTON = 0x02
    VK_CANCEL = 0x03
    VK_MBUTTON = 0x04
    VK_XBUTTON1 = 0x05
    VK_XBUTTON2 = 0x06
    VK_BACK = 0x08
    VK_TAB = 0x09
    VK_CLEAR = 0x0C
    VK_RETURN = 0x0D
    VK_SHIFT = 0x10
    VK_CONTROL = 0x11
    VK_MENU = 0x12
    VK_PAUSE = 0x13
    VK_CAPITAL = 0x14
    VK_KANA = 0x15
    VK_HANGUEL = 0x15
    VK_HANGUL = 0x15
    VK_JUNJA = 0x17
    VK_FINAL = 0x18
    VK_HANJA = 0x19
    VK_KANJI = 0x19
    VK_ESCAPE = 0x1B
    VK_CONVERT = 0x1C
    VK_NONCONVERT = 0x1D
    VK_ACCEPT = 0x1E
    VK_MODECHANGE = 0x1F
    VK_SPACE = 0x20
    VK_PRIOR = 0x21
    VK_NEXT = 0x22
    VK_END = 0x23
    VK_HOME = 0x24
    VK_LEFT = 0x25
    VK_UP = 0x26
    VK_RIGHT = 0x27
    VK_DOWN = 0x28
    VK_SELECT = 0x29
    VK_PRINT = 0x2A
    VK_EXECUTE = 0x2B
    VK_SNAPSHOT = 0x2C
    VK_INSERT = 0x2D
    VK_DELETE = 0x2E
    VK_HELP = 0x2F
    VK_LWIN = 0x5B
    VK_RWIN = 0x5C
    VK_APPS = 0x5D
    VK_SLEEP = 0x5F
    VK_NUMPAD0 = 0x60
    VK_NUMPAD1 = 0x61
    VK_NUMPAD2 = 0x62
    VK_NUMPAD3 = 0x63
    VK_NUMPAD4 = 0x64
    VK_NUMPAD5 = 0x65
    VK_NUMPAD6 = 0x66
    VK_NUMPAD7 = 0x67
    VK_NUMPAD8 = 0x68
    VK_NUMPAD9 = 0x69
    VK_MULTIPLY = 0x6A
    VK_ADD = 0x6B
    VK_SEPARATOR = 0x6C
    VK_SUBTRACT = 0x6D
    VK_DECIMAL = 0x6E
    VK_DIVIDE = 0x6F
    VK_F1 = 0x70
    VK_F2 = 0x71
    VK_F3 = 0x72
    VK_F4 = 0x73
    VK_F5 = 0x74
    VK_F6 = 0x75
    VK_F7 = 0x76
    VK_F8 = 0x77
    VK_F9 = 0x78
    VK_F10 = 0x79
    VK_F11 = 0x7A
    VK_F12 = 0x7B
    VK_F13 = 0x7C
    VK_F14 = 0x7D
    VK_F15 = 0x7E
    VK_F16 = 0x7F
    VK_F17 = 0x80
    VK_F18 = 0x81
    VK_F19 = 0x82
    VK_F20 = 0x83
    VK_F21 = 0x84
    VK_F22 = 0x85
    VK_F23 = 0x86
    VK_F24 = 0x87
    VK_NUMLOCK = 0x90
    VK_SCROLL = 0x91
    VK_LSHIFT = 0xA0
    VK_RSHIFT = 0xA1
    VK_LCONTROL = 0xA2
    VK_RCONTROL = 0xA3
    VK_LMENU = 0xA4
    VK_RMENU = 0xA5
    VK_BROWSER_BACK = 0xA6
    VK_BROWSER_FORWARD = 0xA7
    VK_BROWSER_REFRESH = 0xA8
    VK_BROWSER_STOP = 0xA9
    VK_BROWSER_SEARCH = 0xAA
    VK_BROWSER_FAVORITES = 0xAB
    VK_BROWSER_HOME = 0xAC
    VK_LAUNCH_MAIL = 0xB4
    VK_LAUNCH_MEDIA_SELECT = 0xB5
    VK_LAUNCH_APP1 = 0xB6
    VK_LAUNCH_APP2 = 0xB7
    VK_OEM_1 = 0xBA
    VK_OEM_PLUS = 0xBB
    VK_OEM_COMMA = 0xBC
    VK_OEM_MINUS = 0xBD
    VK_OEM_PERIOD = 0xBE
    VK_OEM_2 = 0xBF
    VK_OEM_3 = 0xC0
    VK_OEM_4 = 0xDB
    VK_OEM_5 = 0xDC
    VK_OEM_6 = 0xDD
    VK_OEM_7 = 0xDE
    VK_OEM_8 = 0xDF
    VK_OEM_102 = 0xE2
    VK_PROCESSKEY = 0xE5
    VK_PACKET = 0xE7
    VK_ATTN = 0xF6
    VK_CRSEL = 0xF7
    VK_EXSEL = 0xF8
    VK_EREOF = 0xF9
    VK_PLAY = 0xFA
    VK_ZOOM = 0xFB
    VK_NONAME = 0xFC
    VK_PA1 = 0xFD
    VK_OEM_CLEAR = 0xFE

    def keyDown(keyCode):
        """
        Key down wrapper
        :param keyCode: int
        :return: void
        """
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def keyUp(keyCode):
        """
        Key up wrapper
        :param keyCode: int
        :return: void
        """
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def key(keyCode, length=0):
        """
        Type a key
        :param keyCode: int
        :param length: int
        :return:
        """
        Keyboard.keyDown(keyCode)
        time.sleep(length)
        Keyboard.keyUp(keyCode)


class Sound:
    # Current volume, we will set this to 100 once initialized
    __current_volume = None

    @staticmethod
    def current_volume():
        """
        Current volume getter
        :return: int
        """
        if Sound.__current_volume is None:
            return 0
        else:
            return Sound.__current_volume

    @staticmethod
    def __set_current_volume(volume):
        """
        Current volumne setter
        prevents numbers higher than 100 and numbers lower than 0
        :return: void
        """
        if volume > 100:
            Sound.__current_volume = 100
        elif volume < 0:
            Sound.__current_volume = 0
        else:
            Sound.__current_volume = volume

    # The sound is not muted by default, better tracking should be made
    __is_muted = False

    @staticmethod
    def is_muted():
        """
        Is muted getter
        :return: boolean
        """
        return Sound.__is_muted

    @staticmethod
    def __track():
        """
        Start tracking the sound and mute settings
        :return: void
        """
        if Sound.__current_volume == None:
            Sound.__current_volume = 0
            for i in range(0, 50):
                Sound.volume_up()

    @staticmethod
    def mute():
        """
        Mute or un-mute the system sounds
        Done by triggering a fake VK_VOLUME_MUTE key event
        :return: void
        """
        Sound.__track()
        Sound.__is_muted = (not Sound.__is_muted)
        Keyboard.key(Keyboard.VK_VOLUME_MUTE)

    @staticmethod
    def volume_up():
        """
        Increase system volume
        Done by triggering a fake VK_VOLUME_UP key event
        :return: void
        """
        Sound.__track()
        Sound.__set_current_volume(Sound.current_volume() + 4)
        Keyboard.key(Keyboard.VK_VOLUME_UP)

    @staticmethod
    def volume_down():
        """
        Decrease system volume
        Done by triggering a fake VK_VOLUME_DOWN key event
        :return: void
        """
        Sound.__track()
        Sound.__set_current_volume(Sound.current_volume() - 4)
        Keyboard.key(Keyboard.VK_VOLUME_DOWN)

    @staticmethod
    def volume_set(amount):
        """
        Set the volume to a specific volume, limited to even numbers.
        This is due to the fact that a VK_VOLUME_UP/VK_VOLUME_DOWN event increases
        or decreases the volume by two every single time.
        :return: void
        """
        Sound.__track()

        if Sound.current_volume() > amount:
            for i in range(0, int((Sound.current_volume() - amount) / 2)):
                Sound.volume_down()
        else:
            for i in range(0, int((amount - Sound.current_volume()) / 2)):
                Sound.volume_up()

    @staticmethod
    def volume_min():
        """
        Set the volume to min (0)
        :return: void
        """
        Sound.volume_set(0)

    @staticmethod
    def volume_max():
        """
        Set the volume to max (100)
        :return: void
        """
        Sound.volume_set(100)


usernameSaid = None
websiteSaid = None
fileFound = None
dataSaid = None
passwordSaid = None
print("Loading Titan.")
speak("Loading Titan.")
greetings()
speak("Titan has loaded, how may I assist you?")
print("Titan has loaded, how may I assist you?")
speak("For a glimpse of possible commands, speak commands.")
print("For a glimpse of possible commands, speak commands.")

if __name__ == '__main__':

    while True:
            statement = takeCommand().lower()

            if statement == 0:
                continue

            if "good bye" in statement or "ok bye" in statement or "stop" in statement or "goodbye" in statement:
                speak('Titan is shutting down, Good bye.')
                print('Titan is shutting down, Good bye.')
                break

            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                time.sleep(2)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("Youtube is open now.")
                time.sleep(2)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google is open on preferred browser.")
                time.sleep(2)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("https://mail.google.com")
                speak("Google Mail is open.")
                time.sleep(2)

            elif 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
                time.sleep(2)

            elif 'open text file' in statement:
                speak("What is the file name?")
                print("What is the file name?")
                inp1 = takeCommand()
                inp2 = '.txt'
                inp = inp1 + inp2
                thisdir = os.getcwd()
                for r, d, f in os.walk(
                        "C:\\"):  # change the hard drive, if you want
                    for file in f:
                        filepath = os.path.join(r, file)
                        if inp in file:
                            fileFound = os.path.join(r, file)
                if fileFound != 0:
                    os.startfile(fileFound, 'open')
                elif fileFound == 0:
                    speak("Could not find text file..")
                fileFound = 0
                time.sleep(2)

            elif 'open application' in statement:
                speak("What is the application name?")
                print("What is the application name?")
                inp1 = takeCommand()
                inp2 = '.exe'
                inp = inp1 + inp2
                thisdir = os.getcwd()
                for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
                    for file in f:
                        filepath = os.path.join(r, file)
                        if inp in file:
                            fileFound = os.path.join(r, file)
                if fileFound != 0:
                    os.startfile(fileFound, 'open')
                elif fileFound == 0:
                    speak("Could not find application file..")
                fileFound = 0
                time.sleep(2)

            elif 'open picture' in statement:
                speak("What is the picture name?")
                print("What is the picture name?")
                inp1 = takeCommand()
                inp2 = '.png'
                inp = inp1 + inp2
                thisdir = os.getcwd()
                for r, d, f in os.walk(
                        "C:\\"):  # change the hard drive, if you want
                    for file in f:
                        filepath = os.path.join(r, file)
                        if inp in file:
                            fileFound = os.path.join(r, file)
                if fileFound != 0:
                    os.startfile(fileFound, 'open')
                elif fileFound == 0:
                    speak("Could not find picture file..")
                fileFound = 0
                time.sleep(2)

            elif 'news' in statement:
                news = webbrowser.open_new_tab("https://news.google.com/")
                speak('Here are some headlines from Google News.')
                time.sleep(2)

            elif 'search' in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(str(statement))
                time.sleep(2)

            elif 'help' in statement:
                speak("Hello! My name is Titan. I am a simple voice assistant programmed to assist you in minor tasks.")
                speak("If you want a full list of commands, say commands.")

            elif 'volume mute' in statement:
                Sound.mute()

            elif 'set volume' in statement:
                statement = int(statement.replace("set volume", ""))
                Sound.volume_min()
                Sound.volume_set(statement)
                time.sleep(1)

            elif 'save data' in statement:
                speak("What type of data?")
                dataSaid = takeCommand().lower()
                if 'password' in dataSaid:
                    speak("What website?")
                    websiteSaid = takeCommand().lower()
                    speak("What is the password for " + websiteSaid)
                    passwordSaid = str(input())
                    speak("Password has been saved as " + passwordSaid)
                elif 'username' in dataSaid:
                    speak("What website?")
                    websiteSaid = takeCommand().lower()
                    speak("What is the username for " + websiteSaid)
                    usernameSaid = takeCommand().lower()
                    speak("Username has been saved as " + usernameSaid)

            elif 'username' in statement:
                if usernameSaid is not None and websiteSaid is not None:
                    speak("Your username is " + usernameSaid + "for website " + websiteSaid)
                elif usernameSaid is None:
                    speak("Please set a username with the command set data")

            elif 'password' in statement:
                if passwordSaid is not None and websiteSaid is not None:
                    speak("Your username is " + passwordSaid + "for website " + websiteSaid)
                elif passwordSaid is None:
                    speak("Please set a username with  the command set data")

            elif 'commands' in statement:
                print('Here are all of the current commands:\n'
                      'wikipedia\n'
                      'password\n'
                      'username\n'
                      'open youtube\n'
                      'open gmail\n'
                      'open google\n'
                      'time\n'
                      'open text file\n'
                      'open application\n'
                      'open picture\n'
                      'news\n'
                      'search\n'
                      'help\n'
                      'volume mute\n'
                      'set volume\n'
                      'good bye\n'
                      'weather\n'
                      'coin flip\n'
                      'dice roll\n')

            elif 'weather' in statement:
                webbrowser.open_new_tab(
                    "https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.69i59j69i60j5.1274j0j4&sourceid"
                    "=chrome&ie=UTF-8")
                speak("Weather open on preferred browser.")

            elif 'coin flip' in statement:
                flip = random.randint(0, 1)
                if flip == 0:
                    speak("Heads")
                    print("Heads")
                else:
                    speak("Tails")
                    print("Tails")

            elif 'dice roll' in statement:
                speak("You rolled" + str(random.randint(1, 6)))
