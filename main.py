#from turtle import color
import streamlit as st
from langchain_helper import get_few_shot_db_chain

#### Setting Page config and columns
st.set_page_config(
    page_title="SQLPaLM",
    #page_icon="favicon2.png",
    layout="wide",    
    #menu_items={'About': "# This App has been developed by Junaid"}
)

with st.container(border=False):
    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        with st.container(border=True):
            st.image("header_img.jpg", use_column_width='always',)
            st.markdown("""
                        <h1 style= 'text-align: center; font-family: Monotype Corsiva;
                        height: 80vh; font-style: italic; font-size: 54px;
                        background:black;
                        color:white'>
                        Echo & Eden</h1>                    
                        """, unsafe_allow_html=True)       


    with col2:        
        with st.container(border=True):
            st.header(':blue[*SQL*]:rainbow[PaLM]', divider='rainbow')
            st.write(':rainbow[**Powered BY Google PaLM To Talk To Your MySQL DB**]')   
            st.header('\n')
            
            question = st.text_area("Question: ")

            col_reponse_empty, col_sql_empty = st.columns([0.2,0.8])
            with col_reponse_empty:
                with st.container(border=True):
                    #st.subheader("Result", divider=True)
                    placeholder1= st.empty()
                    placeholder1.subheader(':grey[*Result*]')
                    
                    
            with col_sql_empty:
                with st.container(border=True):
                    #st.subheader("SQL Query Ran By PaLM", divider=True)
                    placeholder2= st.empty()
                    placeholder2.subheader(':grey[*Query Ran*]')


            if question:
                chain, return_sql_query_chain = get_few_shot_db_chain()
                response = chain.run(question)               
                sql_query_returned_palm = return_sql_query_chain(question)                

                #st.header("Answer")
                col_reponse, col_sql = st.columns([0.2,0.8])
                
                with col_reponse_empty:
                    placeholder1.empty()
                    with st.container(border=True):                    
                        st.subheader("Result", divider=True)
                        try:
                            st.write(response)
                        except Exception as e:
                            #response_ex = chain(question)
                            #st.write(f"{response_ex['result']}")
                            st.warning(f"Unexpected error occurred: {e}")
                            pass

                with col_sql_empty:
                    placeholder2.empty()
                    with st.container(border=True):                
                        
                        st.subheader("Query Ran", divider=True)

                        try:                    
                            st.code(f"{sql_query_returned_palm['result']}", language='sql')
                        except Exception as e:
                            response_ex = chain(question)
                            st.code(f"{response_ex['query']}", language='sql')
                            st.warning(f"Unexpected error occurred: {e}")
                            pass
                        

        
        