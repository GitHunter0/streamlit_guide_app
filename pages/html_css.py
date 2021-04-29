def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        import streamlit.components.v1 as components
        
        st.title('INSERT HTML / CSS COMPONENTS')
        
        st.markdown("<font color='red'>THIS TEXT WILL BE RED</font>",
                    unsafe_allow_html=True)
        
        st.markdown('''<p><font color="purple" face="Verdana, Geneva, sans-serif" size="+1">Your formatted text goes here</font></p>''',
        unsafe_allow_html=True)

        ''' '''
    
if __name__ == "__main__":
    main()