def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
    
        st.title("PLOTS & COLOR PICKER")

    with st.echo():                                     
        # Plotnine -------------------------------------------------------
        st.header("Plotnine Graph")
        # https://github.com/streamlit/streamlit/issues/1581
        from plotnine import ggplot, aes, geom_point, theme
        from plotnine.data import mtcars
        
        p = (
            ggplot(mtcars, aes("wt", "mpg", fill = "vs")) + 
            geom_point() +
            theme(subplots_adjust={'right': 0.85})
        )
            
        st.pyplot(ggplot.draw(p))

    with st.echo():                                     
        # Plotly ---------------------------------------------
        st.header("Plotly Graph")
        import plotly.express as px
        long_df = px.data.medals_long()
        fig = px.bar(long_df, 
                     x="nation", y="count", color="medal", 
                     title="Long-Form Input",
                     width=900, height=600)
        # fig.show()
        st.write(fig)

    with st.echo():                                     
        # Color Picker --------------------------------------
        st.header("Color Picker")
        color_selec = st.color_picker('Pick A Color', '#00f900')
        st.write('The current color is', color_selec)
        #
        df = px.data.tips()
        #
        import plotly.express as px
        fig = px.histogram(df, 
                           x = "total_bill", 
                           # NOTE: do not forget the brackets [ ]
                           color_discrete_sequence = [color_selec],
                           title="Plot with the Selected Color",
                           width=700, height=500)
        # fig.show() 
        st.write(fig)  
    
if __name__ == "__main__":
    main()