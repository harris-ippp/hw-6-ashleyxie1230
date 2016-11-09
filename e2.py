import requests
from bs4 import BeautifulSoup as bs

for line in open("ELECTION_ID"):
    a = line.split()
    resp = requests.get("http://historical.elections.virginia.gov/elections/download/"+a[1]+"/precincts_include:0/")
    soup = bs(resp.content , "html.parser")
    file_name = a[0] + ".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)