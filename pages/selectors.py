def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        import pandas as pd
        
        st.title("SELECTOR WIDGETS (User Input)")
        
    with st.echo():                                             
        # - # Data -------------------------------------------------------
        df = pd.DataFrame({
            'country': ['Brazil']*3 + ['Ireland']*3,
            'date':['2020-01-01','2020-02-01','2020-03-01'] + 
                   ['2020-01-01','2020-01-02','2021-01-03'],
            'population': [200*10**6]*3 + [6*10**6]*3,
            'gdp_growth': [4.2,5,-1,8,7,6.9]
        })
        # 
        # df["date"] = pd.to_datetime(df["date"]) 
        # df
        
        # List of countries
        countries = df["country"].sort_values().unique().tolist()
        # or
        if False:
            countries = df["country"].unique().astype(str).tolist()
            countries.sort()

    with st.echo():                                     
        # - # SELECTBOX ---------------------------------------------------
        st.header("SELECTOX")
        st.subheader("selectbox() selects one and just one item at a time")
        st.title('SELECTBOX')
        
        # Create a selector of countries at the sidebar
        selec_countries = st.selectbox(\
            label = 'Country', 
            options = countries,
            # index (int) – The index of the preselected option on first render.
            index = 0
        )
        
        # Filter dataframe for the contries selected by the user
        """
        NOTE: Do not forget to add [] inside isin(). It solely accepts list type
        while selectbox() returns a string, since it returns only an item at a
        time.
        """
        df_selec_countries = df[ df["country"].isin([selec_countries]) ] 
        
        st.write(df_selec_countries)
        

    with st.echo():                                     
        # - # MULTISELECT --------------------------------------------------
        st.header("MULTISELECT")
        st.subheader("multiselect() selects starts empty and multiple items can be selected at a time")
        st.title('MULTISELECT')
        
        # Create a selector of countries at the sidebar
        selec_columns = st.multiselect(\
            label = 'Columns of the dataframe', 
            options = list(df),
            default = "country"
        )
        df_selec_columns = df[ selec_columns ] 

        st.write(df_selec_columns)

    
    # This line "" was added just to prevent a BUG that precludes the
    # display of all the content of st.write() via st.echo().
    ""        
    
if __name__ == "__main__":
    main()