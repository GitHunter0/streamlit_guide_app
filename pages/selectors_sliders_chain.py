def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        import pandas as pd
        
        st.header("Chaining Selectors and Sliders to Filter a Dataframe")
        
        # - # Data -------------------------------------------------------
        df = pd.DataFrame({
            'country': ['Brazil']*3 + ['Ireland']*3,
            'date_str':['2020-01-01','2020-02-01','2020-03-01'] + 
                       ['2020-01-01','2020-01-02','2021-01-03'],
            'population': [200*10**6]*3 + [6*10**6]*3,
            'gdp_growth': [4.2,5,-1,8,7,6.9]
        })
        # 
        df["date"] = pd.to_datetime(df["date_str"])  
        
        # - # Filter Countries (dataframe rows) using a Selector --------------
        country_list = df["country"].sort_values().unique().tolist()
        
        country_selec = \
            st.selectbox(label = "Select Country",
                                 options = country_list,
                                 index = 0)
            
        # - # Filter Dates (dataframe rows) using a Slider -------------------
        date_min = df["date"].min().to_pydatetime()
        date_max = df["date"].max().to_pydatetime()
        date_selec = st.slider(label = "Select Date Interval",
                                       min_value = date_min,
                                       max_value = date_max,
                                       value = (date_min, date_max))
        
        # - # Filter Dataframe Columns using a Multi-Selector --------------
        column_list = list(df)
        column_selec = st.multiselect(label="Select Columns",
                                              options = column_list,
                                              default = column_list[0:2])
        
        # - # Display Filtered Dataframe -----------------------------------
        df_selec = df[ ( df["country"].isin([country_selec]) ) & \
                       ( df["date"] >= date_selec[0] ) & \
                       ( df["date"] <= date_selec[1] ) 
                     ][column_selec]
        
        st.subheader("Filtered Dataframe (adjust selections in the sidebar)")   
        
        st.write(df_selec)   
         
        ''' '''
    
if __name__ == "__main__":
    main()
    