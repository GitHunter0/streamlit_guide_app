def main():
    
    import streamlit as st
    
    with st.echo():                                     
    
        import streamlit as st
    
        st.title("CACHE")
        
        st.info("Use st.cache() to speed up loading time of functions with expensive computation")
        
        import time
        @st.cache(suppress_st_warning=True)  # 👈 Changed this
        def expensive_computation(a, b):
            # 👇 Added this
            st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
            time.sleep(2)  # This makes the function take 2s to run
            return a * b
        
        a = 2
        b = 21
        res = expensive_computation(a, b)

        st.write("Result:", res)
        
        """
            NOTE: You may have noticed that we’ve added the suppress_st_warning
            keyword to the @st.cache decorators. That’s because the cached
            function above uses a Streamlit command itself (st.write in this
            case), and when Streamlit sees that, it shows a warning that your
            command will only execute when you get a cache miss. More often than
            not, when you see that warning it’s because there’s a bug in your
            code. However, in our case we’re using the st.write command to
            demonstrate when the cache is being missed, so the behavior
            Streamlit is warning us about is exactly what we want. As a result,
            we are passing in suppress_st_warning=True to turn that warning off.
        """
    
if __name__ == "__main__":
    main()