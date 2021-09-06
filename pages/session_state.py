import streamlit as st
st.title("Session State")

#
def update_first():
    st.session_state.second = st.session_state.first
def update_second():
    st.session_state.first = st.session_state.second
    
st.title('🪞 Mirrored Widgets using Session State')
st.text_input(label='Textbox 1', key='first', on_change=update_first)
st.text_input(label='Textbox 2', key='second', on_change=update_second)

st.subheader("Application 2 - Restric access to a result by requiring a password")  

st.write("this part will run without alter the authentication part below")
st.selectbox("Choose a Word", options=['First', 'Second'])

with st.form(key='auth_form'):    
    password = st.text_input("Insert password 'pass_test'", 
                            type='password')
    submit = st.form_submit_button("Submit")

with st.form(key='auth_form2', ):    
    st.session_state.password = \
        st.text_input("Insert password 'pass_test'", type='password')
    st.session_state.submit = st.form_submit_button("Submit")    
    print(st.session_state.submit)    

def password_protected_part():
    # NOTE: Dynamic content does not work since it would ask for authentication every time    
    # https://github.com/streamlit/streamlit/issues/166
    st.subheader("This result is available only for registered users")
    st.write(f'2+2 = ', 2+2)    

if st.session_state.submit:
    if st.session_state.password!="pass-test":
        st.error("Wrong Password. Please, try again.")  
    else:
        st.success("The authetication was successful")
        password_protected_part() 
            
                
