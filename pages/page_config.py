def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
    
        st.title("SET PAGE CONFIGURATION")
    
        st.write('''
                 
        - set_page_config() can only be called once per app, and must be called as the first Streamlit command in your script.    
        
        st.set_page_config(    
            page_title = 'Streamlit Demonstration App',    
            page_icon = ':memo:', # None, ":memo:", ...    
            layout = 'wide', # centered, wide    
            initial_sidebar_state = 'expanded' # auto, expanded, collapsed    
        )  
             
        ''')
        
        ''' '''
    
if __name__ == "__main__":
    main()