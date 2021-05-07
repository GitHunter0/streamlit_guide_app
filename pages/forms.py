#%%

def main():
        
    import streamlit as st

    st.title("FORMS")

    # https://blog.streamlit.io/introducing-submit-button-and-forms/

    # -----------------------------------------------------
    with st.echo():
        st.subheader("Example 1")
        form = st.form(key='my-form')
        name = form.text_input('Enter your name')
        submit1 = form.form_submit_button('Submit')
        #
        st.write('Press submit to have your name printed below')
        #
        if submit1:                           
            st.write(f'hello {name}')

    # -----------------------------------------------
    with st.echo():
        st.subheader("Example 2: Restric access to a result by requiring a password")  

        with st.form(key='auth_form'):    
            password = st.text_input("Insert password 'pass_test'", 
                                    type='password')
            submit2 = st.form_submit_button("Submit")

        def password_protected_part():
            # NOTE: Dynamic content does not work since it would ask for authentication every time    
            # https://github.com/streamlit/streamlit/issues/166
            st.subheader("This result is available only for registered users")
            st.write(f'2+2 = ', 2+2)    
        
        if submit2:
            if password!="pass_test":
                st.error("Wrong Password. Please, try again.")  
            else:
                st.success("The authetication was successful")
                password_protected_part() 
            
    # -----------------------------------------------
    with st.echo():
        st.subheader("Example 3: Forms inside columns")
        col1, col2 = st.beta_columns(2)

        with col1:
            with st.form('Form3a'):
                flavor_selec = st.selectbox('Select flavor', ['Vanilla', 'Chocolate'])
                submit3a = st.form_submit_button('Submit')
            if submit3a:
                st.write(flavor_selec, 'flavor')       

        with col2:
            with st.form('Form3b'):
                intensity_selec = st.slider(label='Select Intensity', 
                                            min_value=0, max_value=100, key=3)
                submit3b = st.form_submit_button('Submit') 
            if submit3b:
                st.write('intensity of', intensity_selec)         
                
    # -----------------------------------------------
    with st.echo():
        
        st.subheader("Example 4: Columns inside forms")

        with st.form('form4'):
            col1, col2 = st.beta_columns(2)
            flavor_selec = col1.selectbox('Select flavor', 
                                          ['Vanilla', 'Chocolate'])
            intensity_selec = col2.slider(label='Select Intensity', 
                                        min_value=0, max_value=100, key=3) 
            submit4 = st.form_submit_button('Submit') 
            
        if submit4:
            st.write(flavor_selec, 'flavor with intensity', intensity_selec)
    
if __name__ == "__main__":
    main()  


