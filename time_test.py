import sys
import urllib.request

resp = urllib.request.urlopen('https://grant-miller.com/notify?apiKey=2022-02-11&text={}'.format(
    sys.platform
))
