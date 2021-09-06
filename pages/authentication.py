def main():
    
    import streamlit as st
    
    with st.echo():    
        
        st.title("Streamlit User Authentication & Authorization")                                 
        
        '''Better Alternatives: 
        https://discuss.streamlit.io/t/multi-page-app-with-session-state/3074/10
        https://discuss.streamlit.io/t/multi-page-app-with-session-state/3074/41
        '''
        
        # First load code from gist
        # You need the SessionState gist. I.e. put the file SessionState.py from <https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92> in your project.  
        '''It will not work for more than 1 concurrent users
        https://discuss.streamlit.io/t/two-people-on-same-session-state/3211/13
        '''
        from SessionState import get

        session_state = get(password='')

        if session_state.password != 'pwd123':
            pwd_placeholder = st.sidebar.empty()
            pwd = pwd_placeholder.text_input("Password:", value="", type="password")
            session_state.password = pwd
            if session_state.password == 'pwd123':
                pwd_placeholder.empty()
                main()
                
            # elif session_state.password != '',     
            else:
                st.error("the password you entered is incorrect")
        else:
            main()
            
        ""
    
if __name__ == "__main__":
    main()