def main():

    import streamlit as st

    with st.echo():
        "Switch to True to enable the code"
        if False:
            '''
            "home.py", "dashboard.py", "page3.py", "page4.py", etc. are streamlit python files inside the folder "pages"
            '''
            import streamlit as st
            import pages.home
            import pages.dashboard
            import pages.page3
            import pages.page4
            # and so on ...

            PAGES = {
                "Home": pages.home,
                "Dashboard": pages.dashboard,
                "Menu title of page 3": pages.page3,
                "Menu title of page 4": pages.page4
                # ...
            }

            st.sidebar.title("Menu - App Pages")
            
            # RADIO BUTTON - Each one renders a new Web Page
            choice = st.sidebar.radio("Choose Page", list(PAGES.keys()))
            
            PAGES[choice].main()
        
        
if __name__ == "__main__": 
     main()

