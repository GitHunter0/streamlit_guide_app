from numpy import where


def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        import pandas as pd
        import datetime
        
        st.title("OTHER INPUTS: Date, Number, ...")
        
    with st.echo():   
        # --------------------------------------------------
        st.header("Checkbox Input")
        checkbox = st.checkbox("Check this box: Returns 'True' if checked")
        st.write(checkbox)

        # --------------------------------------------------
    with st.echo():  
        st.header("Date Input")
        d = st.date_input(label="When is your birthday?",
                          value=datetime.date(2019, 7, 6))
        st.write('Your birthday is:', d)
        
        # --------------------------------------------------
    with st.echo():      
        st.header("Number Input")
        number = st.number_input(label='Insert a number')
        st.write('The current number is ', number)
        
        # -------------------------------------------------
    with st.echo():  
        st.header("Text Input")
        title = st.text_input(label='Insert a movie title', 
                              value='Gladiator')
        st.write('The current movie title is', title)
        
        # --------------------------------------------------
    with st.echo():  
        st.header("Text Input - Password type")
        title = st.text_input(label='Insert your password', 
                              value='mypass', 
                              type="password")
        st.write('Your password is', title)
        
        # --------------------------------------------------

    
if __name__ == "__main__":
    main()