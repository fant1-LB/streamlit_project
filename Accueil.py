import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.html("<p  style='text-align:center'>Bienvenue sur l'app de démo du travail du projet ANR <a href ='https://highvision.hypotheses.org/'> Highvision </a>. <br> Vous trouverez ci dessous des exemples d'images du projet, de journaux du projet, et les liens qui ont pu être réalisés entre ceux-ci.</p> ")
st.write("Les images peuvent prendre un peu de temps à charger, n'hésitez pas à cliquer dessus ou à mettre le tableau en plein écran pour voir mieux.")
df=pd.read_csv("liensghub_et_images.csv", sep=";")

col1, col2, col3 =st.columns((2,1,1))
tableau=col1.dataframe(df,
    column_config={
    "Image recto":st.column_config.ImageColumn("Image recto", width="large"), "Image verso":st.column_config.ImageColumn("Image verso", width="large")},hide_index=True, on_select="rerun", selection_mode="single-row")

try :
    image_recto = col2.image(df.loc[(tableau.selection['rows'][0]), "Image recto"])
    image_verso = col3.image(df.loc[(tableau.selection['rows'][0]), "Image verso"])
except:
    col2.write = "Sélectionner une ligne pour afficher les images."


st.html("<p  style='text-align:center'>Application réalisée par Fantin Le Ber, données annotées par Marie-Louise Kitoko et Sihem Yousfi dans le cadre du projet ANR highvision <br><img src='https://highvision.hypotheses.org/files/2025/03/cropped-Logo_High_Vision_4.jpg'></p> ")
