import streamlit as st

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
DEFAULT_ENDPOINT = 'http://127.0.0.1:45678/search'
TOP_K = 10


# App declaration
def main():
    page_options = ["Movie Recommender System","Other RS"]
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    st.write('# Recommendation System')
    if page_selection == "Movie Recommender System":
        # Sider contents
        sys = st.sidebar.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))
        settings = st.sidebar.expander(label='Settings', expanded=False)
        with settings:
            endpoint = st.text_input(label='Endpoint', value=DEFAULT_ENDPOINT)
            top_k = st.number_input(label='Top K', value=TOP_K, step=1)

        # Header contents
        st.write('## Movie Recommender Engine')
        st.image('resources/imgs/Image_header.png',use_column_width=True)

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list)
        movie_2 = st.selectbox('Second Option',title_list)
        movie_3 = st.selectbox('Third Option',title_list)
        fav_movies = [movie_1,movie_2,movie_3]
        fav_movie = ['hippoman1', 'hippoman2', 'hippoman3']
        # Perform top-n movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=top_k)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

    if page_selection == "Other RS":
        st.title("Other RS")
        st.write("Wait to add.")


if __name__ == '__main__':
    main()
