def main():
    
    import streamlit as st
    
    with st.echo():                                     
        
        import streamlit as st
        
        st.title("LATEX INPUT / MATH FORMULAS")
        
        st.latex(r'''
            a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
            \sum_{k=0}^{n-1} ar^k =
            a \left(\frac{1-r^{n}}{1-r}\right)
        ''')
        
        ''' '''
    
if __name__ == "__main__":
    main()