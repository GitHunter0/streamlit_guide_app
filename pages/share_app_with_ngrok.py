def main():
    
    import streamlit as st

    st.title("Share your App with ngrok")

    st.write("_ngrok generates a public URL to access your app from anywhere_")
    
    st.write('''
                
    - [ngrok tutorial](https://dashboard.ngrok.com/get-started/tutorials)
    
    - [ngrok and other similar services](https://www.sitepoint.com/accessing-localhost-from-anywhere)

    STEPS: (For WINDOWS operational system)
    - Register in <https://ngrok.com/>
    - Download ngrok app
    - Unzip it (there is only one file inside: `ngrok.exe`)
    - Run `ngrok.exe`, it will open a Terminal window
    - In that window, type: `ngrok authtoken <your-token>`
        - The token can be found at your ngrok.com account
    - Type: `ngrok http 8501`
        - It will show an alternative URL to access your Streamlit app from anywhere, not just in your local machine
        - 8501 was choosen because it is the default port of Streamlit, but any port number can be used, provided that it is the same you are running locally
    
    ''')
    
    
if __name__ == "__main__":
    main()