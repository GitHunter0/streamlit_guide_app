def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
        import PIL
       
        st.title("MEDIA INPUTS: IMAGE & VIDEO & AUDIO")
        
        st.write("URL IMAGE")
        image_url = "https://images.unsplash.com/photo-1501250523374-8f78abda6b86?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1482&q=80"
        st.image(image_url, use_column_width=True)
        
        st.write("LOCAL IMAGE")
        image = PIL.Image.open("ryan-loughlin--a8Cewc-qGQ-unsplash.jpg")
        st.image(image, use_column_width=True, caption="Insert a caption here")
        
        st.write("LOCAL AUDIO")
        audio_file = open('audio_sample_guitar.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        
        st.write("VIDEO FROM URL")        
        st.video("https://www.youtube.com/watch?v=kWZmpZTDtkU")
    
if __name__ == "__main__":
    main()