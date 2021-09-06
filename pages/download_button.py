def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
        
#%% -------------------------------------------------
        st.header("Download Button (Streamlit >= 0.88.0)")
        file_name = "table_test.xlsx"
        file_path = f"./{file_name}"
        file_bytes = open(file_path, 'rb')
        st.download_button(label="Click to download the file 1",
                            data=file_bytes, 
                            file_name=file_name,
                            key='download1')
        file_bytes.close()
        # or
        file_name = "table_test.xlsx"
        file_path = f"./{file_name}"
        with open(file_path, 'rb') as file_bytes:
            st.download_button(label="Click to download the file 2",
                               data=file_bytes, 
                               file_name=file_name,
                               key='download2')
        
#%% --------------------------------------------------
        st.header("Create Download Link Button (Streamlit <=0.88.0")

        import pandas as pd
        import numpy as np
        import os
        import base64
        
        def get_binary_file_downloader_html(file_name, 
                                            file_label='Download File'):
            """[Create link to download any file by the user using the browser]
            Args:
                file_name (str): [file path]
                file_label (str): [label to display]. Defaults to 'File'.
            Returns:
                [str]: [html element]    
            Details: See the discussion here <https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806>   
            """ 
            import os
            import base64
            #
            with open(file_name, 'rb') as f:
                data = f.read()
            #
            bin_str = base64.b64encode(data).decode()
            #
            href = f'''
                <a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(file_name)}"> {file_label}</a>
            '''
            return href

        # Create dataframe to be exported as Excel file (.xlsx)
        np.random.seed(1)
        df = pd.DataFrame(np.random.randn(5, 3),
                          columns=[f'col {i}' for i in range(3)])
        df["spècíal_chárâctérs"] = ["ÉeÕ~p+!#$%¨&%\'","fénâ","a","b","c"] 
        
        # Display dataframe
        st.dataframe(df)

        # Generate Link to Download the Excel file
        if st.button('Download as Excel Table'):

            # Save dataframe as a .xlsx file
            file_name = "table_test.xlsx"
            df.to_excel(file_name)  
            
            # HTML Link element
            html_link = get_binary_file_downloader_html(
                file_name = file_name,
                file_label = 'Download .xlsx file'
            )
            
            # Display Link            
            st.markdown(html_link, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
    