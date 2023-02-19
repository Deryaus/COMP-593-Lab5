from pastebin_api import post_new_paste
from poke_api import search_for_pokemon
from sys import argv, exit

def main():
    search_term = get_pokemon_name()
    ability_list = search_for_pokemon(search_term)
    if ability_list:
        title, body_text = get_paste_data(ability_list, search_term)
        paste_url = post_new_paste(title, body_text, '1M')
        print(f'URL of new paste {paste_url}')
    
def get_pokemon_name():
    num_params = len(argv) - 1
    if num_params > 0:
        return argv[1]
    else:
        print('Error: Missing search term.')
        exit(1)
    
def get_paste_data(ability_list, search_term):
    title = f"{search_term}'s Abilities"
    separator = '\n- '
    body_text = '- ' + separator.join(ability_list)
    return title, body_text

if __name__ == '__main__':
    main()