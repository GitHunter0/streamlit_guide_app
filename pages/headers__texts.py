def main():
    import streamlit as st
    with st.echo():                                     
        
        import streamlit as st
        
        st.title("Title")

        st.write(""" 
        # Markdown Section Header
        """)

        st.header("Header 1")
        st.write("Text1")
        st.write(""" 
        # Text 2 
        """)
        st.subheader("Subheader1")
        st.write("## Text subheader")
        st.text("# This is pure text, no Markdown")
        
        txt = st.text_area(label='Text to analyze', value='''
        I feel that there is much to be said for the Celtic belief that the souls of those whom we have lost are held captive in some inferior being, in an animal, in a plant, in some inanimate object, and so effectively lost to us until the day (which to many never comes) when we happen to pass by the tree or to obtain possession of the object which forms their prison. Then they start and tremble, they call us by our name, and as soon as we have recognised their voice the spell is broken. We have delivered them: they have overcome death and return to share our life., (...)
        ''', height=80)
        # st.write('Sentiment:', run_sentiment_analysis(txt))

        st.sidebar.title("About")
        st.sidebar.info("Information about the organization ..."
 
        )
        
        

    
if __name__ == "__main__":
    main()