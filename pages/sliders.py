def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        import pandas as pd
        
        st.title("SLIDER WIDGETS (User Input)")

        # https://docs.streamlit.io/en/stable/api.html?highlight=slider#streamlit.slider

        # BUG: add float() to slider() arguments if KeyError: <class 'numpy.float64'> 
        # - https://discuss.streamlit.io/t/keyerror-class-numpy-float64/5147/2

    with st.echo():                                     
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
        # Convert into specified str format
        # df["date_str2"] = df["date"].dt.strftime("%d-%m-%Y")     

    with st.echo():                                     
        # - # Numeric/Float Slider -------------------------------------------
        st.header("Numeric/Float Slider")
        #
        gdp_growth_min = df["gdp_growth"].min()
        gdp_growth_max = df["gdp_growth"].max()
        #
        gdp_slider = st.slider(label = 'GDP GROWTH', 
                               min_value = float(gdp_growth_min), 
                               max_value = float(gdp_growth_max))
        #
        df_selec = df[ df["gdp_growth"] <= gdp_slider ]
        #
        st.write(df_selec)

    with st.echo():                                     
        # - # Datetime Slider -------------------------------------------
        st.subheader("Datetime Slider")
        #
        from datetime import datetime
        start_time = st.slider("When do you start?",
                               value=datetime(2020, 1, 1, 9, 30),
                               format="DD/MM/YYYY - hh:mm")
        st.write("Start time:", start_time)        
        
    with st.echo():                                     
        # - # Range Sliders: ------------------------------------------------
        st.header("Range Sliders")
        st.write("To convert a slider in a 'range slider', pass in a tuple/list of int/float for the value")
        
    with st.echo():                                     
        # ---------------------------------------------------------------
        st.subheader("Datetime Range Slider")
        #
        date_min = df["date"].min().to_pydatetime()
        date_max = df["date"].max().to_pydatetime()
        #        
        date_slider = st.slider(label="Select Period",
                                min_value = date_min,
                                max_value = date_max,
                                value = (date_min, date_max))
        df_selec = df[ (df["date"] >= date_slider[0]) & \
                       (df["date"] <= date_slider[1]) ]
        st.write(df_selec)   

    with st.echo():                                     
        # -----------------------------------------------------------------
        st.subheader("Range Slider - Display min and max points of the interval")
        values = st.slider(label = 'Select a range of values',
                            min_value=0.0, 
                            max_value=100.0, 
                            value = (25.0, 75.0),
                            step = 0.5)
        st.write('Values:', [values[0], values[1]])

    with st.echo():                                     
        # -------------------------------------------------------------------
        st.subheader("Time Range Slider")
        from datetime import time
        appointment = st.slider("Schedule your appointment:",
                                value = (time(11, 30), time(12, 45)))
        st.write("You're scheduled for:", appointment)

    with st.echo():                                     
        # SELECT SLIDERS ----------------------------------------------------
        st.header("SELECT SLIDERS")
        st.subheader("String Date Range Slider")
        st.write("select_slider() selects values from iterables (list, ...)")
        # 
        date_str_list = df["date_str"].sort_values().unique().tolist()
        date_str_min = df["date_str"].min()
        date_str_max = df["date_str"].max() 
        #
        date_str_slider = st.select_slider(label="Select Period",
                                           options = date_str_list,
                                           value = (date_str_min, date_str_max))
        df_selec = df[ (df["date"] >= date_str_slider[0]) & \
                       (df["date"] <= date_str_slider[1]) ]
        st.write(df_selec)     

    
if __name__ == "__main__":
    main()