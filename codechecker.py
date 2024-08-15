import time
import os
import requests
from colorama import Fore, Style, init

init(autoreset=True)

ascii_art = """
██╗░░██╗██╗░░░██╗███████╗
╚██╗██╔╝╚██╗░██╔╝╚════██║
░╚███╔╝░░╚████╔╝░░░███╔═╝
░██╔██╗░░░╚██╔╝░░██╔══╝░░
██╔╝╚██╗░░░██║░░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
"""

# Put Your Token Instagram:  xyzrich.a
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ascii_art():
    print(Fore.RED + ascii_art)
    print(Style.RESET_ALL)

def display_start_message():
    print(Fore.YELLOW + "Finding Servers. 🌎")
    time.sleep(3)
    clear_console()

def display_ascii_art_again():
    display_ascii_art()
    print(Fore.GREEN + "OFFICIAL ACCOUNTS")
    print(Fore.GREEN + "|||  ----->  instagram  :  xyzrich.a")
    print(Fore.GREEN + "|||------>  Discord  :  @9li2")
    print(Fore.GREEN + "Start Gen 💎")

def check_invite(invite_code):
    url = f"https://discord.com/api/v10/invites/{invite_code}"
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        invite_info = response.json()
        if invite_info.get('uses') is None or invite_info.get('uses') == 0:
            print(Fore.GREEN + "Available Inv Code 💎")
        else:
            print(Fore.RED + "Not available")
            guild_id = invite_info['guild']['id']
            members_url = f"https://discord.com/api/v10/guilds/{guild_id}/members"
            members_response = requests.get(members_url, headers=headers)
            
            if members_response.status_code == 200:
                members_info = members_response.json()
                online_members = sum(member['status'] == 'online' for member in members_info)
                offline_members = len(members_info) - online_members
                print(Fore.RED + f"Server who used this invite code:")
                print(Fore.RED + f"Members: {len(members_info)}")
                print(Fore.RED + f"Online: {online_members}")
                print(Fore.RED + f"Offline: {offline_members}")
            else:
                print(Fore.RED + "Unable to fetch member information.")
    else:
        print(Fore.RED + "Invalid invite code or unable to fetch invite information.")
        print(Fore.RED + f"Status Code: {response.status_code}")

def check_login():
    url = "https://discord.com/api/v10/users/@me"
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_info = response.json()
        username = user_info['username']
        print(Fore.GREEN + f"Logged in [ Username: {username}, Token: {BOT_TOKEN} ]")
    else:
        print(Fore.RED + "Failed to authenticate with the provided token.")
        print(Fore.RED + f"Status Code: {response.status_code}")

def main():
    check_login()
    display_ascii_art()
    display_start_message()
    display_ascii_art_again()
    
    while True:
        invite_code = input("Enter the invite code to check (or type 'exit' to quit): ")
        if invite_code.lower() == 'exit':
            break
        check_invite(invite_code)

if __name__ == "__main__":
    main()
