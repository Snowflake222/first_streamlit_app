
import streamlit

streamlit.title('Cali famous Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥤 Orange and Rocket Smoothie')
streamlit.text('🥣 Acai Bowl')
streamlit.text('🥦 Kale,spinach and blueberry smoothie')
streamlit.text('🥑 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

