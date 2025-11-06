import time 
import requests
import colorama
import os
import random

colorama.init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

ascii_texte = r"""
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █ 
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░ 
         ░  ░              ░         ░ ░           ░    ░  ░         ░ 
                                                                       
"""

def ascii(color):
    color = getattr(colorama.Fore, color.upper(), colorama.Fore.WHITE)
    print(color + f"{ascii_texte}")

def gen():
    random_code = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
    response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{random_code}?with_application=false&with_subscription_plan=true")
    if response.status_code == 200:
        print(colorama.Fore.GREEN + f"[200] Code nitro valide : discord.gift/{random_code}")
    
    elif response.status_code == 429:
        print(colorama.Fore.YELLOW + "[429] Rate limit atteinte, attente de 16 secondes...")
        time.sleep(16)

    else : 
        print(colorama.Fore.RED + f"[404] Code nitro invalide : discord.gift/{random_code}")

def hello():
    print(colorama.Fore.YELLOW + "Développé par 𝖑𝖆𝖈𝖈ø𝖒 💖")
    hello_choice = input(colorama.Fore.RED + "Voullez vous démarrez la génération ? O/N ")
    if hello_choice  in ['0', 'o', 'O']:
        clear()
        ascii("RED")
        print(colorama.Fore.BLUE + "Démarrage de la génération des codes nitro...")
        while True :
            gen()
            time.sleep(0.5)
    else :
        exit()

clear()
ascii("RED")
hello()