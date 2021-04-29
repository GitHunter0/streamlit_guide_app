def main():
    
    import streamlit as st
    import time
    
    with st.echo():                                     
    
        import streamlit as st
    
        st.title("SPINNER")
        
        st.header("It shows a message while performing a computation")
        #
        with st.spinner("Waiting..."):
            computation = 10**5/7**6
            time.sleep(5) # here just to simulate a long computation time
        st.success("Finished!")
        
        st.write(computation)
    
if __name__ == "__main__":
    main()