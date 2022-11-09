import pandas as pd
import streamlit
import pandas
import numpy
import re

s = r',| '

def txt2flt(txt):
    #txt = re.sub(' +', ' ', txt)
    t2fl = re.split(s, str(txt))
    t2fl = [l for l in t2fl if l != '']
    return t2fl

def getsum(a):
    return sum([float(i) for i in a])  

def calcres(a,b):
    return [float(a[i])*float(b[i]) for i in range(len(a))]

def main():
    choice = streamlit.sidebar.selectbox("Menu", ['Home', 'About', 'Bayes Calculator', 'Contact Us'])
    if choice == "About":
        streamlit.title("About the page")
    if choice == "Contact Us":
        streamlit.title("Contact Us")
    if choice == "Home":
        streamlit.title("Home")
    if choice == "Bayes Calculator":
        streamlit.title('Bayes Calculator')
        data = pandas.DataFrame(columns=[])
        streamlit.markdown(""" <style> .font {font-size:50px;} </style> """, unsafe_allow_html=True)

        if 'df' not in streamlit.session_state:
            streamlit.session_state.df1 = data
        streamlit.session_state.df = data

        with streamlit.form(key='myform', ):
            A = streamlit.text_input("\u03B8", )
            B = streamlit.text_input("f(x|\u03B8)", )
            C = streamlit.text_input("p(\u03B8)f(x|\u03B8)", )
            streamlit.button = streamlit.form_submit_button("Get Result")

            if streamlit.button:
                A = txt2flt(A)
                B = txt2flt(B)
                C = txt2flt(C)
                Result = calcres(B,C)
                sumpt = getsum(B)
                summult = getsum(C)
                sumres = getsum(Result)
                Result1 = [str(l/sumres) for l in Result]
                Result = [str(l) for l in Result]

                df = pandas.DataFrame({"\u03B8": A, 'prior p(\u03B8)': B, "f(x|\u03B8)": C, "p(\u03B8)f(x|\u03B8)": Result, "p(\u03B8)f(x|\u03B8)/\u2211 p(\u03B8)f(x|\u03B8)":Result1})
                #blankIndex=[''] * len(df)
                #df.index = blankIndex
                #df.style.hide_index()    
                #df.to_string(index=False)
                streamlit.session_state.df = streamlit.session_state.df.append(df)


                streamlit.text("")
                streamlit.dataframe(streamlit.session_state.df)
                sumpt = getsum(B)
                summult = getsum(C)
                sumres = getsum(Result)
                sumres1 = getsum(Result1)
                
                
                streamlit.latex(r'''\sum p(\theta) = ''' + rf'''{sumpt}''')
                streamlit.latex(r'''\sum f(x|\theta) = ''' + rf'''{summult}''')
                streamlit.latex(r'''\sum p(\theta)f(x|\theta) = ''' + rf'''{sumres}''')
                streamlit.latex(r'''\frac {p(\theta)f(x|\theta)}{\sum p(\theta)f(x|\theta)} = ''' + rf'''{sumres1}''')
                

if __name__ == '__main__':
    main()