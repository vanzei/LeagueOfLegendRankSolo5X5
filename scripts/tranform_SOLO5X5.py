# %%
import pandas as pd
import json
import glob
import datetime

dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# %%
json_files = glob.glob('../data/*.json')

# %%
try:
    agg = pd.read_csv("../processed/processed.csv")
except:
    agg = pd.DataFrame(columns = ['tier', 'leagueId', 'queue', 'name', 'date', 'summonerId',
       'summonerName', 'leaguePoints', 'rank', 'wins', 'losses', 'veteran',
       'inactive', 'freshBlood', 'hotStreak'])

# %%
dates = agg['date'].astype(str).unique()

# %%
for file in json_files:
    file_date = file[8:18]
    if file_date in dates:
        continue
    else:
        df = pd.read_json(f'../data/{file_date}-response.json')
        df['date'] = pd.Timestamp(file_date)
        df = df.join(pd.json_normalize(df.entries)).drop(columns='entries')
        agg = pd.concat([agg, df])


# %%
agg.to_csv("../processed/processed.csv", index=False)

# %%
metadata = open(f"../processed/metadata-{dt_now}", "w")
metadata.close()


