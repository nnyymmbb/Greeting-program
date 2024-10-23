import os
import getpass
from datetime import datetime
import platform
import time
import random
import requests

RE = '\033[0m'
BO = '\033[1m'
IT = '\033[3m'
UL = '\033[4m'
IN = '\033[7m'

now = datetime.now()
day = now.strftime('%A')
date = now.day
cTime = now.strftime('%H:%M')

phrases2 = [
    "Today is a great day for new achievements!",
    "Don't forget to smile!",
    "You are capable of everything you set your mind to!",
    "It's time for a new adventure!"
]
phrases1 = [
    f"It's currently {IN}{cTime}{RE}, and outside it is already the {IN}{date}-th{RE}. I hope the day brings only pleasant moments.",
    f"Today is already {IN}{day}{RE}, it's the perfect time to start a new project or finish what you've started.",
    f"Today is {IN}{day}{RE}, and it's time to check your plans for the day. Is everything on schedule?",
    f"Current OS version: {IN}{platform.version()}{RE}. Everything is running smoothly and without hiccups."
]

def tGreet():
    cHour = now.hour
    if 5 <= cHour < 12:
        return "Good morning"
    elif 12 <= cHour < 18:
        return "Good afternoon"
    elif 18 <= cHour < 23:
        return "Good evening"
    else:
        return "Good night"

print(f"╔═{BO}System Information{RE}═╗")
print(f"{IN}Processor:{RE} \t\t{platform.processor()}")
print(f"{IN}OS Version:{RE} \t\t{platform.version()}")
print(f"{IN}Current Time:{RE} \t{cTime}")
print("╚══════════════════════╝")

print(f"\n{tGreet()}, {IN}{os.getlogin()}{RE}! {random.choice(phrases1)}")
print(f"✧ {IT}{random.choice(phrases2)}{RE} ✧")
