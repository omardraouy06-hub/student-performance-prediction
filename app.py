
import streamlit as st
import pandas as pd
import joblib

# ETAPE 1 : Charger le modele entraine
model = joblib.load('model.pkl')

# ETAPE 2 : Configuration de la page
st.set_page_config(
    page_title="Prediction Etudiant",
    page_icon="🎓"
)

# ETAPE 3 : Titre
st.title("🎓 Prediction de la note finale")
st.write("Entrez les notes de l'etudiant pour estimer sa note finale.")

# ETAPE 4 : Saisie des notes
note_math = st.number_input(
    "Note de Math",
    min_value=0.0,
    max_value=20.0,
    value=10.0
)

note_physique = st.number_input(
    "Note de Physique",
    min_value=0.0,
    max_value=20.0,
    value=10.0
)

note_francais = st.number_input(
    "Note de Français",
    min_value=0.0,
    max_value=20.0,
    value=10.0
)

# ETAPE 5 : Bouton de prediction
if st.button("Predire la note finale"):

    # Preparer les donnees
    nouvel_etudiant = pd.DataFrame({
        'note math': [note_math],
        'note physique': [note_physique],
        'note français': [note_francais]
    })

    # Effectuer la prediction
    prediction = model.predict(nouvel_etudiant)

    # Afficher le resultat
    st.success(f"Note finale predite : {prediction[0]:.2f} / 20")
