#   LAB 6 PYTHON 
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   PROGRAM DESCRIPTION: This lab allows the user to input a name of 
#   a pokemon and outputs the pokemeon selected to a pastebin 
#   formatted document.
#
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   USAGE: python A6L-NolanKapshey.py
#
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#
#   DUE DATE: MONDAY MARCH 28TH, 2022
#
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   HISTORY:
#       DATE        AUTHOR      Description
#       2022-03-25  N.KAPSHEY   Initial Creation
#
#   _________________________________________________________________
#   
# Import the functions 
from sys import argv
import requests
import time

def main():
    poke = argv[1]
    dict = get_poke_info(poke)
    
    if dict:
        poke_strings = get_poke_strings(dict)
        pastebin_url = post_to_pastebin(poke_strings[0], poke_strings[1])
        print(pastebin_url)
        
        
def post_to_pastebin(title, body):
    print("Posting Pokemon information to PasteBin...", end = '')
    time.sleep(2)
    params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    }
    response = requests.post('https://pastebin.com/api/api_post.php', data=params)
    if response.status_code == 200:
        print('Success!',"\n")
        return response.text # Convert response body to a dictionary
    else:
        print('Action Failed. Response code:', response.status_code)
        return

def get_poke_strings(dict):
    title = dict['name'] + "'s Abilities"
    body_text = ""
    for poke_Type in dict['abilities']:  
        body_text = poke_Type['ability']['name'] + "\n"
    body_text = body_text[:-1]
    return (title, body_text)
    
    
    
def get_poke_info(poke):
    print("Getting Pokemon Info.....")
    time.sleep(2)
    resp_msg = requests.get('https://pokeapi.co/api/v2/pokemon/' + poke) 
    if resp_msg.status_code == 200:
        print('Success!',"\n")
        return resp_msg.json()
    else:
        print('Action Failed. Response code:', resp_msg.status_code)
        return
    
main()