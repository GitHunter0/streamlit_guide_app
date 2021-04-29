def main():
   
    import streamlit as st
    
    st.title("CUSTOM THEMES")
    
    st.markdown("""
    STEPS TO CUSTOMIZE APP THEME (Colors and Font):    
    
    - Create a folder named '.streamlit' inside your app directory    
    - Create file 'config.toml' inside that folder    
    - Go to your App -> Menu (top right corner button) -> Theme ->
        Custom Theme -> Edit active theme -> customize colors and font
        family -> Copy theme to clipboard -> paste inside
        'config.toml' -> Save file    
    - Reload app to see the new theme    
        
    - To assign a theme color to a variable, do this for example:    
    `variable_to_store_a_color = st.get_option("theme.primaryColor")`    
    
    References:    
        - <https://blog.streamlit.io/introducing-theming/>    
        - <https://www.youtube.com/watch?v=Mz12mlwzbVU>    
        - <https://github.com/streamlit/theming-showcase-blue>    
    """)
      
if __name__ == "__main__":
    main()