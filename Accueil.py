import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.html("<p  style='text-align:center'>Bienvenue sur l'app de démo du travail du projet ANR <a href ='https://highvision.hypotheses.org/'> Highvision </a>. <br> Vous trouverez ci dessous des exemples d'images du projet, de journaux du projet, et les liens qui ont pu être réalisés entre ceux-ci.</p> ")
st.write("Sélectionnez une ligne du tableau pour avoir des détails sur les images.")
df=pd.read_csv("datas/liensghub_et_images.csv", sep=";")
df_pochettes = pd.read_csv("datas/donnees_boites2_260_def2.csv")
df_metadonnees = pd.merge(df, df_pochettes, left_on="Id_image", right_on="nom_image_normalise")
df_metadonnees= df_metadonnees[df_metadonnees['Face']=='verso'].reset_index()

col1, col2, col3 =st.columns((2,1,1))
tableau=col1.dataframe(df,
    column_config={
    "Page de journal correspondante":None,"Image recto":st.column_config.ImageColumn("Image recto", width="large"), "Image verso":st.column_config.ImageColumn("Image verso", width="large")},hide_index=True, on_select="rerun", selection_mode="single-row")

try :
    image_recto = col2.image(df.loc[(tableau.selection['rows'][0]), "Image recto"], caption ="Recto de l'image")
    image_verso = col2.image(df.loc[(tableau.selection['rows'][0]), "Image verso"], caption = "Verso de l'image")
    lien_image =df.loc[(tableau.selection['rows'][0]), "Page de journal correspondante"].replace(".item", "/full/full/0/native.jpg").replace("ark:","iiif/ark:")
    col1.write(f"Cote du contenant aux Service Historique de la défense : {df_metadonnees.loc[(tableau.selection['rows'][0]), "Dossier"]} ")
    col1.write(f"Titre de l'enveloppe contenant la pochette de l'image : {df_metadonnees.loc[(tableau.selection['rows'][0]), "Titre Enveloppe"]} ")
    col1.write(f"Titre de la pochette contenant l'image : {df_metadonnees.loc[(tableau.selection['rows'][0]), "Titre Pochette"]} ")
    image_gallica = col3.image(lien_image, caption ="Page de journal où l'image est reprise")
    avertissement_gallica = col3.write(f"La BNF ayant mis en place des restrictions liées à des récuperations en masse de leurs images, l'affichage peut prendre quelques temps. \n Alternativement vous pouvez accéder à l'image à l'adresse : {lien_image}")
except:
    pass


st.html("<p  style='text-align:center'>Application réalisée par Fantin Le Ber, données annotées par Marie-Louise Kitoko et Sihem Yousfi dans le cadre du projet ANR highvision <br><img src='https://highvision.hypotheses.org/files/2025/03/cropped-Logo_High_Vision_4.jpg'></p> ")
