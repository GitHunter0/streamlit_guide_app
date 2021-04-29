def main():
   
    import streamlit as st
   
    with st.echo():                                     
   
        import streamlit as st
   
        st.title("SIDEBAR")

        st.write("To place an element in the sidebar just add the prefix `sidebar.` to it")

        st.header("Look at the bottom of the lateral left bar")
   
        st.sidebar.title("Sidebar Title")
        
        st.sidebar.info(
            """
            ## Sidebar Info BOX
            This app was built solely for educational purposes. In case of any doubt, 
            [contact me](https://wa.me/<insert-your-whatsapp-number-here>?text=How%20can%20I%20help?).
            """
        )
    
if __name__ == "__main__":
    main()