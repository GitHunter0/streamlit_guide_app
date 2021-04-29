def main():
    
    import streamlit as st
                                           
    st.title("BASIC INFORMATION & TRICKS")
    
    # --------------------------------------
    st.header("Streamlit installation")
    
    st.write("""
        - Conda: `conda install --channel=conda-forge streamlit`
        - Pip: `pip install --upgrade streamlit`
    """)        
    
    st.error('''
        - In Conda environments, install from conda-forge. Pip installation may cause a lot of errors
        - Check Python version compatibility, currently only [versions](https://docs.streamlit.io/en/stable/) from 3.6 to 3.8 are accepted
    ''')
    
    # -----------------------------------------
    st.header("How to run your Streamlit app")
    
    st.write("""
        - Go to the Terminal
        - Activate the conda environment it is installed on 
        - Go to the directory of the streamlit app you want to run
        - Type: `streamlit run your_app_file_name.py`
    """) 
    
    st.subheader("See your running app")
    st.write("""    
        - The default Streamlit port is __8501__
        - Therefore, you can see the app running by going to your browser at the address <http://localhost:8501/>
    """)
    
    st.subheader("How to run in another port")
    st.write("""
        - Let's say you want to run at port 8579, type:
        `streamlit run your_app_file_name.py --server.port 8579`  
    """)     
    
    # -------------------------------------------------------
    st.header("Record a screencast")
    st.info("""    
    To record your app screen while you use it, go to:  
    __Menu -> 'Record a screencast'__
    """)
    st.warning("The record will only work if you give ALL the permissions that are asked")   
            
    # --------------------------------------------------------      
    st.write('''
             
             
             ''')        
    st.write("""     
        - Modules required to run this demonstration app: ` streamlit, streamlit-ace, streamlit_tags, numpy, pandas, scipy, openpyxl, plotnine, plotly, kaleido`, 
    """)
    
    # This last line "" is needed to prevent a BUG that precludes the display of
    # all the content of st.write() when st.echo() is.
    ""    
    
if __name__ == "__main__":
    main()