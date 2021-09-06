def main():
    
    import streamlit as st
    
    st.title("LAYOUT COMPONENTS & CONFIGURATIONS")
    
    #%% INITIAL LAYOUT SETTINGS ---------------------------------------
    st.header("Initial Layout Settings - See the source code provided here")
    with st.echo():                                     
        
        import streamlit as st
    
        if False: # remove or set to "True"
            # Page Layout Initial Configuration
            # NOTE: set_page_config() can only be called once per app, 
            # and must be called as the FIRST command in your script.
            # The `import` commands are the only ones accepted before it.
            # NOTE: set_page_config() must be in the app main file (app.py)
            st.set_page_config(
                page_title='Streamlit Demonstration App', 
                # set Streamlit logotype as the favicon
                page_icon="Streamlit_Logo_1.jpg", # None, ":memo:...
                layout='wide', # centered, wide
                initial_sidebar_state='expanded' # auto, expanded, collapsed
            )
        
    
    #%% Control Visibility of the Hamburger Menu and 'Made with Streamlit' footer -----------------------------------------------------------
    st.header("Menu and Footer Visibility - See the source code provided here")
    with st.echo():
            
        # https://discuss.streamlit.io/t/remove-made-with-streamlit-from-bottom-of-app/1370/2
        
        if False: # remove or set to "True"
            # Hide Hamburger Menu and Streamlit footer 'Made with Streamlit'
            # NOTE: this hack must be inserted in the app main file (app.py)
            hide_menu_footer = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
            """
            st.markdown(hide_menu_footer, unsafe_allow_html=True) 
        
        
    #%% LAYOUT Divisions and Elements ------------------------------------
    st.header("LAYOUT Divisions and Elements")
    with st.echo():    
        
        st.write("<https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/>")
    
    
    # -----------------------------------------------------------------
    st.subheader("Columns")
    with st.echo():     
        st.write("Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)")
        col1 = st.sidebar
        # col2 will have width=2 and col1, width=1
        col2, col3 = st.columns((2,1))
        # Add some text to the columns
        col1.header("Column 1 (Sidebar)")
        col2.write("Column 2")
        col3.write("Column 3")
        
        # Syntatic sugar
        ''' This is equivalent to:
        col2.write("col2")
        col2.write(2+2)
        '''
        with col2:
            st.write("col2")
            st.write(2+2)
    
    # -----------------------------------------------------------------
    st.subheader("Trick to obtain Center Alignment")
    
    with st.echo():     
        
        st.write("Create 3 columns and just use column 2 (the middle one)")           
        
        col1, col2, col3 = st.columns([2, 2, 2])

        col2.title("Centered Text")     
        
         
    # -------------------------------------------------------------------
    st.subheader("Expander Bar")
    with st.echo(): 
        expander_bar = st.beta_expander("Click to expand")
        expander_bar.markdown("""
        - test
        - line 2
        - __bold line3__
        """)
        #
        expander_bar.line_chart({'x':range(10),
                                'y':range(11,21)})
        
        
    # ----------------------------------------------------------
    st.subheader("[Containers](https://docs.streamlit.io/en/stable/api.html?highlight=container#streamlit.beta_container)")
    #
    st.write('''
    - Containers are invisible untill you add content to them
    - Containers reserve a space and everything added to it will be placed in that space
        - This opens a great deal of flexibility and possibilities to your app
    - The difference between an __single-element container__ (`st.empty()`) and a __container__ (`st.beta_container()`) is that, in the former, each new call __replaces__ the previous contents inside it, while in the latter, subsequent calls __append__ to the existing contents
    ''')
    with st.echo():
    
        container1 = st.beta_container()
        
        st.write("This line will appear after the contents added to the container")
        
        import time
        with container1:
            for seconds in range(10):
                st.write(f"⏳ {seconds} seconds have passed")
                time.sleep(1)
            st.write("✔️ 10 seconds over!")
    
    
    # ------------------------------------------------------------
    st.subheader("[Single-Element Containers](https://docs.streamlit.io/en/stable/api.html?highlight=empty#streamlit.empty)")
    with st.echo():     
        placeholder = st.empty()
        
        st.markdown("This comment will appear after any of the content added to the container")
        
        placeholder.write("Fill container with content")
        placeholder.write("This content will replace the one added above")
        
    
if __name__ == "__main__":
    main()