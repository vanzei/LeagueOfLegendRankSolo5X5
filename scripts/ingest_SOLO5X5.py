# %%
import requests
from dotenv import load_dotenv
import os
import json
from datetime import date
 


load_dotenv()


# %%
today = date.today()

# %%
api_key=os.environ.get("API_KEY")

# %%
url = f"https://na1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key={api_key}"

# %%
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com"
}

# %%
res = requests.get(url = url, params=header)

# %%
with open(f'../data/{today}-response.json', 'w') as f:
    json.dump(res.json(), f)


