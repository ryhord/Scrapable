from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
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
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can make it do anything
    """
    print(e)


def get_selections(url):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    songs = html.select('.article-detial h3')
    songs = list(songs)
    songs_as_strings = []
    for song in songs:
        songs_as_strings.append(song.string.extract())
    return songs_as_strings

def put_to_file(items):
    file = open("list.txt", "w")
    for item in items:
        file.write(item)

# url = input('enter the url you want to get: ')
# list_of_songs = get_selections(url)
# put_to_tile(list_of_songs)
#
#

url = input('enter the url you want to get: ')
list_of_songs = get_selections(url)
for song in list_of_songs:
    print(song)