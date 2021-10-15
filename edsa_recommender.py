import streamlit as st

# Custom Libraries
from utils.data_loader import load_movie_titles,load_movie_genres
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')
genre = load_movie_genres('resources/data/movies.csv')
DEFAULT_ENDPOINT = 'http://127.0.0.1:45678/search'
TOP_K = 10


# App declaration
def main():
    recommend_options = ["Movie Recommender System","Other RS"]
    page_selection = st.sidebar.selectbox("Choose Option", recommend_options)
    type_choice = st.sidebar.selectbox(
        'Please choose the type of your input:',
        [{'name': 'search_by_genre', 'display': 'Recommend from favored genres.'},
         {'name': 'search_by_object', 'display': 'Recommend from favored objects.'}],
        format_func=lambda x: x['display']
    )['name']
    st.write('# Recommendation System')
    # Sider contents
    sys = st.sidebar.radio("Select an algorithm",
                           ('Content Based Filtering',
                            'Collaborative Based Filtering'))
    settings = st.sidebar.expander(label='Settings', expanded=False)
    with settings:
        endpoint = st.text_input(label='Endpoint', value=DEFAULT_ENDPOINT)
        top_k = st.number_input(label='Top K', value=TOP_K, step=1)

    if page_selection == "Movie Recommender System":

        # Header contents
        st.write('## Movie Recommender Engine')
        st.image('resources/imgs/Image_header.png',use_column_width=True)

        if type_choice == "search_by_object":
            # User-based preferences
            st.write('### Enter Your Three Favorite Movies')
            movie_1 = st.selectbox('First Option',title_list)
            movie_2 = st.selectbox('Second Option',title_list)
            movie_3 = st.selectbox('Third Option',title_list)
            fav_movies = [movie_1, movie_2, movie_3]
        else:
            st.write('### Choose genres you prefer:')
            container1 = st.container()
            sectors = container1.multiselect(" ",genre,
                                             help="You can directly type words to search and choose genres.")

        # Perform top-n movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
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
