def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        import streamlit.components.v1 as components
        
        st.title('EMBED WEB APPS / SITES using Iframe')
        
        st.header("Embed Streamlit Website")
        components.iframe("https://docs.streamlit.io/en/latest", height=600, scrolling=True)
        
        st.header('Embed Moneytimes Website')
        components.iframe("https://www.moneytimes.com.br/tag/xp-investimentos/", height=700, scrolling=True)

        '''
        st.header('Embed Shiny Web App')
        components.iframe("https://<user-name>.shinyapps.io/<app-name>/", height=600)
        '''
        
        ''' '''
    
if __name__ == "__main__":
    main()