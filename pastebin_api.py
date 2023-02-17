import requests
DEVELOPER_KEY = '49msVf603u-ut6bcM9Ug5o_8pniO5xR-'
PASTEBIN_API_URL ='https://pastebin.com/api/api_post.php'
def main():
   
   url = post_new_paste('this is a title', 'this is the body')
   print(f'New past URL: {url}')

def post_new_paste(title, body_text, expiration='10M', listed=False):
    """Creates a new public PasteBin paste

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): Expiration date of paste (n= never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to '10M'.
        listed (bool, optional): Whether paste is publicly listed (True) or not (False) Defaults to False.

    Returns:
        str: URL of the new paste, if successful. None if unsuccessful.
    """

# setup parameters for the request message
    past_params = {
        'api_dev_key': DEVELOPER_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }
    # Send the post request to the pastebin api
    print('Sending POST request to PasteBin API...', end='')
    resp_msg = requests.post(PASTEBIN_API_URL, data=past_params)

    # check whether post requeset was successsful
    if resp_msg.ok:
        print('success.')
        return resp_msg.text
    else:
        print('request failed.')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason}).') 
        print(f'Reason: {resp_msg.text}.')

if __name__ == '__main__':
    main()