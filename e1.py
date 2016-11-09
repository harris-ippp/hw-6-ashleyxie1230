import requests
from bs4 import BeautifulSoup as bs
resp = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General")
soup = bs(resp.content , "html.parser")
ID = soup.find_all("tr", "election_item")
with open("ELECTION_ID", "w") as out:
    for row in ID:
        year = row.find("td", "year first").string
        electionId = row.get("id").replace("election-id-", "")
        out.write(year+" "+electionId+"\n")
