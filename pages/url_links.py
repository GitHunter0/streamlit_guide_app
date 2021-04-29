def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
    
        st.title("URL LINKS") 
            
        link_in_markdown_format = '''    
        [Click to open the link in a new tab](https://streamlit.io/)   
        '''
        st.markdown(link_in_markdown_format, unsafe_allow_html=True)   
    
if __name__ == "__main__":
    main()