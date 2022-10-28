import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header( 'Breakfast Menu')
streamlit.text('🥣Onega 3 & Blueberry Ostneal')
streamlit.text('🥗Kale, Spinach & Rocket Smocthio')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

   
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
