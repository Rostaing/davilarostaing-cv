import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime
import streamlit.components.v1 as components

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_English_and_French_version_Diavila_Rostaing_Engandzi.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
info_pic = current_dir / "assets" / "info.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Davila Rostaing | Digital CV "
PAGE_ICON = "assets/logo.jpg"
NAME = "Davila Rostaing ENGANDZI"
DESCRIPTION = """
Data Scientist & Informaticien, aider les entreprises en soutenant la prise de décision basée sur les données avec l'intelligence artificielle.
"""
EMAIL = "rostaingdavila@gmail.com"
SOCIAL_MEDIA = {
    "         ": "https://youtube.com/c/codingisfun",
    "": "",
    "LinkedIn": "linkedin.com/in/davila-rostaing-3b25a51bb/",
    "GitHub": "https://github.com/Rostaing",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
st.markdown(""" <br>""", unsafe_allow_html=True)
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

annee = datetime.today().year
annnee_experience = annee - 2019

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.markdown(f"<b><p class='nom'>{NAME}</p></b>", unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger mon CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.image("assets/info.png", width=100)
    #st.write("📫", info_pic)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
 
st.markdown(""" <hr>""", unsafe_allow_html=True)   

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    f"""
- ✔️ {annnee_experience} ans d'expérience dans l'extraction d'informations exploitables à partir de données
- ✔️ Solide expérience pratique et connaissances en Python et R
- ✔️ Bonne compréhension des principes statistiques et de leurs applications respectives
- ✔️ Excellent esprit d'équipe et faisant preuve d'un fort sens de l'initiative sur les tâches
"""
)

with st.expander("Formations et Certifications"):
  st.markdown("""
              - ✔️ 2021 : Data Analytics Professional Certificate (équivalent BAC +4); Google
              - ✔️ 2021 : Data Analyst Professional Certificate; IBM
              - ✔️ 2020 : Deep Learning Specialization Certificate; DeepLearning.AI
              - ✔️ 2020 : Mathematics for Machine Learning Specialization Certificate; Imperial College London
              - ✔️ 2020 : AI Engineering Professional Certificate; IBM
              - ✔️ 2020 : Data Science Professional Certificate (équivalent aux crédits Universitaires); IBM
              - ✔️ 2020 : Machine Learning Specialization Certificate; University of Washington
              - ✔️ 2020 : Big Data Specialization Certificate; UCSanDiego
              - ✔️ 2020 : Leadership Development for Engineers Specialization Certificate, Rice University
              - ✔️ 2020 : Diplôme d’ingénieur des Travaux Informatiques; Institut Africain d’Informatique (Gabon)
              - ✔️ 2019 : Diplôme de Programmeur ; Institut Africain d’Informatique (Libreville, Gabon)
              
              """)


  
with st.expander("Expériences Professionelles"):
  st.markdown("""
              16/02/2022 — 22/02/2022 :
              
            - Participant au Forum Numérique Congo 3ème Edition. Thème : L’Innovation Technologique et la Donnée au coeur des Transformations Digitales : Enjeux & Défis (Pointe-Noire, Congo).
            <br>
            
            - Fonction : Consultant informaticien et Data Scientist
            
            - Tâches réalisées :
            
            - ✔️ Parlé des services qu’offre le cabinet <<Grinso & Associés>> devant le Premier Ministre, Chef du
              Gouvernement et d’autres membres du Gouvernement ;
            
            - ✔️ Service Conseil : droit numérique, management des systèmes d’informations, l’ingénierie
              informatique, gestion de projets, MOA-MOE, stratégie, légistique, marketing technologique, l’intelligence
              artificielle, big data ;
            
            - ✔️ Service Etude : prospective du marché, audit informatique, élaboration des cahiers des charges informatiques...
          
            <hr>
              05/2022 — 09/2022 :
              
            - Projet : Enquêtes sociodémographiques complémentaires auprès des ménages dans le cadre du Projet Lisungi de Réponse d’Urgence à la Convid-19 (PLRUC).
                                             LOT 5: Loango, Djambala, Dolisie, Nkayi et Ouesso
                                             
            - Fonction : Consultant Data Manager
            
            Tâches réalisées :
              - ✔️Préparer la pré-liste;
              - ✔️Réviser et piloter les questionnaires;
              - ✔️Lister les répondants;
              - ✔️Suivre, apurer les données et assister dans l’analyse préliminaire de celles-ci;
              - ✔️Soutenir l’élaboration des rapports de projets;
              - ✔️Superviser la synchronisation des données effectuées par les enquêteurs;
              - ✔️Soumettre les rapports réguliers à la Division RSU.
              
              <br>
              
            Environnement technique :
              - ✔️OS : Windows 11
              - ✔️Langages : Python, DAX, SQL
              - ✔️SGBD : Oracle…
              - ✔️Bibliothèques : Numpy, Pandas, Seaborn, Matplotlib
              - ✔️Méthode : Agile (SCRUM)
              - ✔️Outils : Microsoft Power BI, Jupyter lab, Talend, Git
              <hr>
              
              2021 à ce jour :
              
              Ecole Supérieure de Gestion et d’Administration des Entreprises (ESGAE).
                                 BP: 2339 - BRAZZAVILLE
                
            - Fonction : Enseignant (Prestataire)
            
            Matières enseignées :
              - ✔️Algorithme et Structure de données;
              - ✔️Data Science avec Python;
              - ✔️Administration MongoDB;
              - ✔️Microsoft Power BI;
              - ✔️Administration Oracle;
              - ✔️Fondamentaux JavaScript.
              
              <hr>
              10/2020 — 05/2022 :
              
            - Projet : Mise en place de smart data et des cubes olap selon les indicateurs de l’application <<Gestion hospitalière et dossier médical unique>> à l’Agence Congolaise des Systèmes d’Information (ACSI) à Brazzaville (Congo).
              
            - Fonction : Data Analyst
              
            Tâches réalisées :
              - ✔️Collecte et traitement de données manquantes;
              - ✔️Création du dataset;
              - ✔️Analyse exploratoire de données;
              - ✔️Modélisation (régression linéaire multiple…);
              - ✔️Analyse des besoins en indicateurs;
              - ✔️Création des indicateurs sous Microsoft Power BI;
              - ✔️Cartographie de données;
              - ✔️Développement et amélioration des tableaux de bord;
              - ✔️Maintenance corrective et évolutive des tableaux de bord…
            <br>
            
            Environnement technique :
              - ✔️OS : Windows 10
              - ✔️Langages : Python, DAX, SQL
              - ✔️SGBD : MySQL
              - ✔️Bibliothèques : Numpy, Pandas, Seaborn, Matplotlib, Scikit-learn
              - ✔️Méthode : Agile (SCRUM)
              - ✔️Outils : Microsoft Power BI, Jupyter lab, Talend, Git
              - ✔️Serveur : Wamp
              
            <hr>
            3/2019 — 6/2019 :
              <br>
            
              - Projet du dataset de covid-19 de kaggle.com
              - Fonction : Data Scientist (Freelance)
           
            Tâches réalisées :
           
            - ✔️Analyse exploratoire de données du dataset (EDA); 
            - ✔️Prétraitement de données ; 
            - ✔️Développement et mise en place d’un système d’aide à la décision à base d’intelligence artificielle des patients atteints de SARS-CoV2 (Covid-19).
              
            <hr>
            2017 — 2018 :
            
            - Fonction: Développeur web, et formateur à Libreville (Gabon)
            
          
              
            Tâches réalisées :
            - ✔️Formateur en programmation informatique, au développement web et Microsoft Office; 
            - ✔️Encadreur en mathématiques (collège, lycée) et l’anglais ;  
            - ✔️Installation des systèmes d’exploitation et installation des logiciels ; 
            - ✔️Activation des systèmes d’exploitation et de Microsoft office.
            
            <hr>
            2016 :
            
            - Fonction : Agent Airtel
             
             <br>
            Tâches réalisées :
            
            - ✔️Marketing, enroulement et activation des comptes Airtel Money à Airtel Congo (Brazzaville).   
          
            
              """, unsafe_allow_html=True)
  
with st.expander("Compétences Techniques"):
  st.markdown("""
           - ✔️ Langages de programmation : Python, R, Ruby, DAX…
           - ✔️ Frameworks: Ruby on Rails, Streamlit, Tensorflow…
           - ✔️ Technologies web : HTML, CSS, Bootstrap, Hotwire…
           - ✔️ Content Management System (CMS) : WordPress…
           - ✔️ Gestion de projet : Agile (Kanban, Scrum)
           - ✔️ Système de Gestion des Bases de Données : MongoDB, Oracle, MySQL, PostgreSQL, SQLite, SQL Server…
           - ✔️ Méthodes de Conception des Systèmes d’Information : Agile (SCRUM), UML + 2TUP, MERISE
           - ✔️ Bibliothèques : Numpy, Pandas, Scipy, Seaborn, Matplotlib, Plotly, Scikit-learn, BeautifulSoup, Statsmodels, Keras…
           - ✔️ Data Science : Analyse de données, Machine Learning, Deep Learning, Intelligence Artificielle…
           - ✔️ Systèmes d’exploitation : Linux, Windows, MacOS
           - ✔️ Logiciels : Microsoft Power BI, RStudio, Jupyter notebook, Spyder, Jupyter Lab, Colab, Tableau, Git, Microsoft Office, Spreadsheets, Spark…
           - ✔️ Autres : Big Data, API, Github, SQL, NoSQL, ETL, Business Intelligence (BI), Business Analyse, Cloud…
           
           """)

with st.expander("Compétences Métiers"):
  st.markdown("""
              - ✔️ Banque
              - ✔️ Assurance
              - ✔️ Finance
              - ✔️ Marketing
              - ✔️ Education
              - ✔️ Médecine
              - ✔️ Sport
              """)
  
with st.expander("Langues"):
  st.markdown(""" 
              - ✔️ Français (Langue maternelle)
              - ✔️ Anglais (certifié TESOL, Arizona State University, USA)
              """)

with st.expander("Centres d’intérêt"):
  st.markdown(""" 
              - ✔️ Data Science & recherches
              - ✔️ Lecture
              - ✔️ Musique
              - ✔️ Sport
              - ✔️ Voyage
              """)
st.markdown("Je certifie sur l’honneur l’exactitude des renseignements fournis.")
st.markdown(""" <hr>""", unsafe_allow_html=True) 
st.markdown(f"<p class='pa'>© {annee} Davila Rostaing. Tous les droits réservés.</p>", unsafe_allow_html=True)