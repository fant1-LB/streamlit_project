import streamlit as st
import pandas as pd

st.html("Bienvenue sur l'app de démo du travail du projet ANR <a href ='https://highvision.hypotheses.org/'> Highvision </a>. <br> Vous trouverez ci contre des exemples d'images du projet, de journaux du projet, et les liens qui ont pu être réalisés entre ceux-ci. ")
st.write("Voici des exemples de circulations repérées manuellement dans le cadre du projet Highvision")
df=pd.read_csv("liensghub_et_images.csv", sep=";")
st.dataframe(df,
    column_config={
    "Image recto":st.column_config.ImageColumn("Image recto", width="large"), "Image verso":st.column_config.ImageColumn("Image verso", width="large")},hide_index=True)
