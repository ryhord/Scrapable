from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None"""
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """    It is always a good idea to log errors.
    This function just prints them, but you can make it do anything
    """
    print(e)


def get_selections(url, selection):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    songs = html.select(selection)
    """
    songs = list(songs)
   
    songs_as_strings = []
    for song in songs:
        songs_as_strings.append(song.string.extract())
    """
    return songs


def put_to_file(items):
    file = open("list.txt", "w")
    for item in items:
        file.write(item)

# url = input('enter the url you want to get: ')
# list_of_songs = get_selections(url)
# put_to_tile(list_of_songs)
#
#


def get_names(url, selector):
    """
    Downloads the page where the list of music is found
    and returns a list of strings, one per n
    """
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select(selector):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))



"""  
url = input('enter the url you want to get: ')
selection = input("What's the selector of the content you want?")
list_of_songs = get_names(url, selection)
for song in list_of_songs:
    print(song)
"""