import streamlit
streamlit.title("new diner")
streamlit.header('breakfast menu')
streamlit.text('omega 3, blueberry oatmeal')
streamlit.text('kale, spinach')
streamlit.text('hard-boiled egg')
streamlit.text('avacado toast')


streamlit.title('Build your own smoothie')
import pandas as pd
my_fruit_list=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect('pick some fruits:',list(my_fruit_list.index),['Avocado','Apple'])
streamlit.dataframe(my_fruit_list)

