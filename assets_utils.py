##get Team Logos
from data.data import teams
import urllib
import urllib.request

def retrieve_logo(url, name):
    try:
        urllib.request.urlretrieve(url, "assets\\logos\\" + name + ".svg")
    except:
        print(name)


##get Team Logos
for index, row in teams.iterrows():
    url = urllib.parse.urljoin("https://assets.nhle.com/logos/nhl/svg/", row["abbreviation"] + "_light.svg")
    retrieve_logo(url, row["abbreviation"])

##get NHL Logo
url = urllib.parse.urljoin("https://assets.nhle.com/logos/nhl/svg/", "NHL_light.svg")
retrieve_logo(url, "NHL")