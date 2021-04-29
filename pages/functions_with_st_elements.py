def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
    
        st.header("FUNCTIONS with Streamlit (st) Elements")

        st.write('''
            - You can write functions with st elements (sliders, selectors, etc)
            - The elements will be created each time the function is called
        ''')
        
        st.subheader("Create Function to Display in a dataframe the parameters selected interactively by the user")
        # 
        import pandas as pd
        def user_input_features():
            sepal_length = st.slider('Sepal length', 4.3, 7.9, 5.4)
            sepal_width = st.slider('Sepal width', 2.0, 4.4, 3.4)
            petal_length = st.slider('Petal length', 1.0, 6.9, 1.3)
            petal_width = st.slider('Petal width', 0.1, 2.5, 0.2)
            data = {'sepal_length': sepal_length,
                    'sepal_width': sepal_width,
                    'petal_length': petal_length,
                    'petal_width': petal_width}
            features = pd.DataFrame(data, index=[0])
            return features
        # 
        df_input = user_input_features()
        #
        st.subheader('User Input parameters')
        #
        st.write(df_input)
    
if __name__ == "__main__":
    main()