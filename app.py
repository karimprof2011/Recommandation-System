!pip install streamlit
import streamlit as st

st.set_page_config(page_title="Maturité Digitale des Enseignants", layout="centered")

st.title("📊 Évaluation de la maturité digitale des enseignants")

st.subheader("Sélectionnez les outils TICE que vous utilisez régulièrement")

tice_tools = [
    "Tableau Numérique Interactif (TNI)",
    "Plateforme d'apprentissage en ligne (Moodle, Google Classroom)",
    "Logiciels de présentation (PowerPoint, Google Slides)",
    "Outils de collaboration en ligne (Google Docs, Microsoft 365)",
    "Applications éducatives (Kahoot!, Quizlet)",
    "Ressources pédagogiques numériques (sites web, vidéos éducatives)",
    "Logiciels de gestion de classe (Pronote, Vie Scolaire)",
    "Réseaux sociaux professionnels (LinkedIn Education, Eduscol)"
]

selected_tools = st.multiselect(
    "Outils TICE",
    tice_tools
)

score = len(selected_tools)

st.write(f"Votre score de maturité digitale est de : {score}/{len(tice_tools)}")

if score == 0:
    st.warning("Vous n'avez sélectionné aucun outil. Votre maturité digitale semble faible.")
elif score < len(tice_tools) / 2:
    st.info("Vous utilisez quelques outils TICE. Il y a une bonne marge de progression !")
elif score < len(tice_tools):
    st.success("Vous utilisez régulièrement des outils TICE. C'est excellent !")
else:
    st.balloons()
    st.success("Félicitations ! Vous maîtrisez parfaitement les outils TICE !")
