def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        import pandas as pd
        import numpy as np
        
        st.title("MAPS")
        
        st.header('DISPLAY LATITUDE-LONGITUDE POINTS')
        
        np.random.seed(321)
        #
        latlon_points = pd.DataFrame(
            # np.random.randn(25, 2) / [50, 50] + [-3.7381, -38.5350], 
            np.random.randn(25, 2) / [50, 50] + [-25.54015, -54.58581], 
            columns=['latitude', 'longitude']
        )
        
        st.map(latlon_points)

        st.write('Points displayed: ', latlon_points)
        
        ''' '''
    
if __name__ == "__main__":
    main()