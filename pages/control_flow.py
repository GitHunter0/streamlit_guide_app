def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
    
        st.title("CONTROL FLOW")
        
        # name will be '' (empty) if the user does not type a name
        name = st.text_input('Name (insert your name here)  ') 
        # display inserted name
        st.write(name) 
        
        st.write("No subsequent code will be run until some name is inserted (any name different from empty '') ")
        if name=='':
            st.warning('Please input a name.')
            # Make any subsequent code not to run (which includes st.success)
            st.stop() 
            
        st.success('Thank you for inputting a name')
        
        st.write(f"Your name has {len(name)} letters")
        
        
    
if __name__ == "__main__":
    main()