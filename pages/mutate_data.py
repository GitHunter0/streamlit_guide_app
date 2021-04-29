
def main():
        
    import streamlit as st
    import pandas as pd
    import numpy as np
    
    with st.echo():  
        
        import streamlit as st
        import pandas as pd
        import numpy as np
        
        df1 = pd.DataFrame({'x': [float(x) for x in range(1,11)] ,
                            'y': [float(x) for x in range(11,21)] })
        
        my_table = st.table(df1) 
        
        np.random.seed(1)
        df2 = pd.DataFrame(np.random.randn(5, 2),
                           columns=[f'col {i}' for i in range(2)])
        
        # Add rows to the previous table
        my_table.add_rows(df2)
        
        my_chart = st.line_chart(df1)
        # Add data to the chart
        my_chart.add_rows(df2)


if __name__ == "__main__":
    main()