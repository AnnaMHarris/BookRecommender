import streamlit as st
import pickle
import streamlit.components.v1 as components
from PIL import Image
import requests

books = pickle.load(open("books_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
books_list = books['title'].values

st.header("Book Recommender")
selectvalue=st.selectbox("Select movie from dropdown", books_list)

def fetch_cover(books_id):
    # Get the image URL for the book
    image_url = books.loc[books['book_id'] == books_id, 'image'].iloc[0]
    # Open the image from the URL
    open_image = Image.open(requests.get(image_url, stream=True).raw)
    return open_image

def recommend(book):
    index = books[books['title']==book].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda vector:vector[1])
    recommend_book = []
    recommend_cover =[]
    for i in distance[1:6]:
        books_id = books.iloc[i[0]]['book_id']
        recommend_cover.append(fetch_cover(books_id))
        recommend_book.append(books.iloc[i[0]].title)
    return recommend_book, recommend_cover

if st.button("show recommendations"):
    book_name, book_cover = recommend(selectvalue)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(book_name[0])
        st.image(book_cover[0])
    with col2:
        st.text(book_name[1])
        st.image(book_cover[1])
    with col3:
        st.text(book_name[2])
        st.image(book_cover[2])
    with col4:
        st.text(book_name[3])
        st.image(book_cover[3])
    with col5:
        st.text(book_name[4])
        st.image(book_cover[4])