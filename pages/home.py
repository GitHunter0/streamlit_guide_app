def main():
   
    import streamlit as st
    
    # with st.echo():                                     
        
    import streamlit as st
    import PIL
    
    # Trick to get CENTERED ALIGNMENT 
    col1, col2, col3 = st.columns([0.5,6,0.5])
    col2.title("STREAMLIT DEMONSTRATION WEB APP")

    image = PIL.Image.open("Streamlit_Logo_1.jpg")
    st.image(image, use_column_width=True, caption=None)
    
    col1, col2, col3 = st.columns([0.5,6,0.5])
    col2.write(""" 
    # Reference Guide to Build a Streamlit App
    """)
    
    # st.sidebar.title("Home Sidebar Title")
    
if __name__ == "__main__":
    main()