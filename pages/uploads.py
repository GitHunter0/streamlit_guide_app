def main():
   
    import streamlit as st
   
    with st.echo():                                     
   
        import streamlit as st
   
        st.title("UPLOAD FILES")
        
        import pandas as pd

        uploaded_file = \
            st.file_uploader("Choose a file (.xlsx) to upload and display",
                             accept_multiple_files = False)
        
        if uploaded_file is not None:
            
            df = pd.read_excel(uploaded_file)
            
            st.write(df)  
    
if __name__ == "__main__":
    main()