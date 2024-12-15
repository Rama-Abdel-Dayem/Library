import streamlit as sl
from Library_Script import * 



sl.title("Welcome to the Library System")


while(True):
    option= sl.selectbox('What would you like to look at?', ['All Books', 'Available Books', 'Authors',
                                                            'Members','Staff','Issue History'])
    if option =='Members':
        sl.header('Our Valued Members')
        



