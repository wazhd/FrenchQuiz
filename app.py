import streamlit as st

st.set_page_config(page_title="Quiz : La Francophonie à Toronto", page_icon="🇨🇦")

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

st.title("🧩 Quiz interactif : Toronto et sa culture")
st.write("Testez vos connaissances sur la francophonie et la culture torontoise après notre présentation !")


with st.form("quiz_form"):
    q1 = st.radio(
        "1. En quelle année Samuel de Champlain est-il arrivé pour explorer la région ?",
        ["1534", "1615", "1790", "1803"]
    )

    q2 = st.radio(
        "2. Quel pourcentage de la population de Toronto avait le français comme langue maternelle en 2021 ?",
        ["1,5 %", "3,7 %", "10 %", "12,4 %"]
    )

    q3 = st.radio(
        "3. Quel est l'ingrédient principal qui compose la base de la 'Sushi Pizza' à Toronto ?",
        ["Pâte à pizza classique", "Pain pita", "Riz frit", "Feuille d'algue séchée"]
    )

    q4 = st.radio(
        "4. Quel quartier est connu pour être le premier projet de logement social au Canada ?",
        ["Corktown", "Little Italy", "Old Town", "Regent Park"]
    )

    q5 = st.radio(
        "5. Pendant combien de temps la Tour CN a-t-elle été la plus haute tour du monde ?",
        ["10 ans", "20 ans", "Plus de 30 ans", "Elle l'est toujours"]
    )

    submit_button = st.form_submit_button("Soumettre mes réponses")


if submit_button:
    st.session_state.score = 0
    st.session_state.submitted = True

    if q1 == "1615": st.session_state.score += 1
    if q2 == "3,7 %": st.session_state.score += 1
    if q3 == "Riz frit": st.session_state.score += 1
    if q4 == "Regent Park": st.session_state.score += 1
    if q5 == "Plus de 30 ans": st.session_state.score += 1

    st.divider()
    if st.session_state.score == 5:
        st.balloons()
        st.success(f"Félicitations ! Score parfait : {st.session_state.score}/5 🏆")
    elif st.session_state.score >= 3:
        st.info(f"Pas mal ! Ton score est de : {st.session_state.score}/5 👍")
    else:
        st.warning(f"Tu peux faire mieux ! Score : {st.session_state.score}/5.")

st.sidebar.info("Projet présenté par Ryan, Dravya, Joel et Carson.")
