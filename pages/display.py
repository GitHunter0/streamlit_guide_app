def main():
    
    import streamlit as st
    
    st.title("DISPLAY OBJECTS / TEXT / CODE / Other inputs")
    
    #%% st.write(): FLEXIBLE DISPLAY ---------------------------
    st.header("[write() function](https://docs.streamlit.io/en/stable/api.html?highlight=streamlit.write#streamlit.write)")

    st.subheader("st.write() displays appropriate output based on the input type")
    
    st.info('''
    Arguments are handled as follows:

    - write(string): Prints the formatted Markdown string, with
        support for LaTeX expression and emoji shortcodes. See docs for st.markdown for more.

    - write(data_frame) : Displays the DataFrame as a table.

    - write(error) : Prints an exception specially.

    - write(func) : Displays information about a function.

    - write(module) : Displays information about the module.

    - write(dict) : Displays dict in an interactive widget.

    - write(obj) : The default is to print str(obj).

    - write(mpl_fig) : Displays a Matplotlib figure.

    - write(altair) : Displays an Altair chart.

    - write(keras) : Displays a Keras model.

    - write(graphviz) : Displays a Graphviz graph.

    - write(plotly_fig) : Displays a Plotly figure.

    - write(bokeh_fig) : Displays a Bokeh figure.

    - write(sympy_expr) : Prints SymPy expression using LaTeX.

    ''')    
    
    
    #%% MARKDOWN -----------------------------------------
    st.header("MARDKOWN")
    with st.echo():
        st.markdown("## Subheader created with Markdown")
    
    
    #%% CODE -----------------------------------------------------
    st.header("CODE")
    with st.echo():
        code = '''
        def hello():
        print("Hello, Streamlit!")
        '''
        st.code(code, language='python')
    
    
    #%% DATAFRAME -------------------------------------------------
    st.header("DATAFRAME")
    with st.echo():                                     
    
        import streamlit as st
        import pandas as pd
        from datetime import datetime 
    
        
        df = pd.DataFrame({
            'country': ['Brazil']*3 + ['Ireland']*3,
            'date':['2020-01-01','2020-02-01','2020-03-01'] + 
                ['2020-01-01','2020-01-02','2021-01-03'],
            'population': [200*10**6]*3 + [6*10**6]*3,
            'gdp_growth': [4.2,5,-1,8,7,6.9]
        })
        #  Convert into date type
        df["date2"] = pd.to_datetime(df["date"]) 
        # Convert into specified str format
        df["date3"] = df["date2"].dt.strftime("%d-%m-%Y")
         
        st.write("Method 1 - st.dataframe() - Interactive Table")
        st.dataframe(df)
        
        st.write("Method 2 - st.write() - same result as above")
        st.write(df)
        
        st.write("Method 3 - Static Table")
        st.table(df)
        
        
    #%% DOCSTRING -------------------------------------------------
    st.header("DOCSTRING")
    with st.echo():   
        import pandas as pd
        st.help(pd.DataFrame)                                  
            
    
if __name__ == "__main__":
    main()