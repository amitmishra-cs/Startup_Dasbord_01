import  streamlit as st

import streamlit as st
from PIL.ImImagePlugin import number
from streamlit import subheader
import pandas as pd
import time


st.title('Startup Dashboard')
st.header('I am Learning Streamlit')
st.subheader('And I am Loving it')

st.write('Happy Birth day king')
st.markdown("""
### My favorite movies 
- Race -3
- Humerals
- Houseful
""""")

st.code("""
def foo(input):
   return foo**2

x =foo(2)
""")

st.latex('x^2 + y^2 + 2 = 0')

df =pd.DataFrame({
    'name':['Mishra', 'Amit', 'Anupam'],
    'Marks':[50, 60 ,70],
    'package':[10, 12, 15]
})
st.dataframe(df)

st.metric('Revenue', 'Rs =3L', '3%')
st.metric('Revenue', 'Rs =3L', '-3%')

st.json({
    'name':['Mishra', 'Amit', 'Anupam'],
    'Marks':[50, 60 ,70],
    'package':[10, 12, 15]
})

st.image('Screenshot 2024-11-05 225717.png')
st.video('video.m4V.mp4')

st.sidebar.title('Sidebar ka Title')
col1, col2 , col3 =st.columns(3)

with col1:
    st.image('Screenshot 2024-11-05 225717.png')

with col2:
    st.image('Screenshot 2024-11-05 225717.png')

with col3:
    st.image('Screenshot 2024-11-05 225717.png')


st.error('Login Failed')
st.success('Login success')

st.warning('Login success')

bar =st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)



number = st.number_input('Enter Age')
st.date_input('enter date ')

email = st.text_input('Enter Email')
password = st.text_input('Enter Password')
st.button('Login Karo')









# email = st.text_input('Enter Email')
# password = st.text_input('Enter Password')
gender =st.selectbox('Select gender', ['male', 'female', 'others'])

btn =st.button('Login Karo')

if btn:
    if  email == 'mishra@gmail.com' and password == '1234':
        st.success('Login sauces full')
        st.balloons()
        st.write(gender)

    else:
        st.error('Login Failed')
uploaded_file = st.file_uploader('Upload a CSV file')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.describe())