def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        from streamlit_tags import (st_tags, st_tags_sidebar)
        
        st.title("TEXT & TAG INPUTS")
        
    with st.echo():
        # TEXT INPUT -----------------------------------------------------
        st.header("TEXT INPUT")
        search_phrases_selec = [st.text_input(label="Select up to 2 keywords", 
                                              value="First keyword")]
        #
        search_phrases_selec.append(st.text_input(label='Second keyword'))
        #
        st.write('First keyword :', search_phrases_selec[0])
        st.write('Second keyword :', search_phrases_selec[1])

    with st.echo():        
        # TEXT INPUT - side-by-side Layout -------------------------------
        st.header("TEXT INPUT: Side by Side Layout")
        col2, col3 = st.beta_columns([1,1])
        keyword1_selec = col2.text_input(label="Keyword 1")
        keyword2_selec = col3.text_input(label="Keyword 2")
        st.write(keyword1_selec) 
        st.write(keyword2_selec)  
        
    with st.echo():    
        # TAGS INPUT ---------------------------------------------------
        st.header("TAGS INPUT")
        '''      
        - https://discuss.streamlit.io/t/new-component-streamlit-tags-a-new-way-to-do-add-tags-and-enter-keywords/10810
        
        - https://github.com/gagan3012/streamlit-tags
        
        python -m pip install streamlit-tags
        
        conda install --channel=gagan3012 streamlit-tags -y
        '''
        keywords = st_tags(label='Enter Keyword:', 
                           text='Press enter to add up to 3 keywords', 
                           value= ['First entry'],
                           maxtags=3)

        st.write(keywords)
        st.write('first keyword :', keywords[0])
        
    ""        
    
if __name__ == "__main__":
    main()