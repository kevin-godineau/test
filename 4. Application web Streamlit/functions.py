### Import
import streamlit as st
import pandas as pd

# Cach data @st.cache_data
df = pd.read_csv('data.csv')

def page_1():

    ### Title et markdown : st.title et st.markdown
    st.title("Bonjour tout le monde")

    st.subheader("Hello World !")

    st.write("Je suis une zone de texte")

    st.markdown("""
                # Titre

                ## Sous-titre

                texte
                """)

    st.write(df.head(10))




    ### Checkbox st.checkbox
    if st.checkbox("Click on bouton"):
        st.image('https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg', width=200)



    ### Selectbox st.selectbox
    select_user = st.selectbox('Sélect a number : ', range(5))
    st.write(f"Your choice : {select_user}")


    ### Forms st.form, st.form_submit_button et st.select_slider
    with st.form('Formulaire 1'):
        name = st.text_input('Tape your Name')

        if st.form_submit_button('Send'):
            st.write(name)
        
        
        
        
### autre methode pour crer des pages  tout indenter
def page_2():
    st.title("autre bonjour le monde")


def page_formulaire():
    st.title("Formulaire")

