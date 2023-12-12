import pandas as pd
import streamlit as st
import datetime
import altair as alt
import time

with st.spinner('Loading project...'):
    time.sleep(1)
st.success('The project was loaded successfully', icon="✅")
st.header("Welcome to League of Legends GM Daily Rank👑")
d = st.date_input("Select the interest date: ", datetime.date(2023, 12, 9),min_value=datetime.date(2023, 12, 9), max_value = datetime.date(2023, 12, 12) )

date = d.strftime("%Y-%m-%d")
df = pd.read_csv("../processed/processed.csv")

with st.spinner('Loading project...'):
    time.sleep(0.5)
st.write(df[['date','summonerName', 'leaguePoints', 'rank', 'wins', 'losses', 'veteran',
       'inactive', 'freshBlood', 'hotStreak']].query("date == @date").sort_values('leaguePoints', ascending=False))


st.write('Top 15 Grandmaster players for the', d)
show = df.query("date == @date").sort_values('leaguePoints', ascending=False).head(15)

graph = alt.Chart(show).mark_bar(color = 'gray').encode(x=alt.X('summonerName', sort=None),y='leaguePoints').properties(width=700,height=500)
st.write(graph)

img = '../image/diagram.png'

st.info('Project Diagram', icon="ℹ️")
st.image(img, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")