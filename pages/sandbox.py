def main():
    
    import streamlit as st
    
    # set_page_config() can only be called once per app, and must be called as
    # the first Streamlit command in your script.
    # st.write("It is important to set layout='wide' in set_page_config()")
    ''' 
    st.set_page_config(
        page_title='Streamlit Sandbox',    
        page_icon=':memo:',    
        layout='wide', 
        initial_sidebar_state='collapsed'
    )
    '''
    
    # with st.echo():                                     
    
    import streamlit as st
    from streamlit_ace import st_ace
    import pandas as pd
    import numpy as np
    
    st.title("Streamlit SANDBOX")

    st.sidebar.title(":memo: Editor settings")

    THEMES = [
        "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
        "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
        "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
        "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
        "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
        "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
    ]

    KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]

    display, editor = st.columns((2, 2))

    INITIAL_CODE = """
st.subheader("**_A quick and easy way to test your code_**")    
st.write("Play with Streamlit live in the browser!")
table_data = {'Column 1': [1, 2], 'Column 2': [3, 4]}
st.write(pd.DataFrame(data=table_data))
st.write("For a better display of Sandbox, use this option: `set_page_config(layout='wide')`")
"""

    with editor:
        st.write('### Code editor')
        code = st_ace(
            value=INITIAL_CODE,
            language="python",
            placeholder="st.header('Hello world!')",
            theme=st.sidebar.selectbox("Theme", options=THEMES, index=26),
            keybinding=st.sidebar.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
            font_size=st.sidebar.slider("Font size", 5, 24, 14),
            tab_size=st.sidebar.slider("Tab size", 1, 8, 4),
            wrap=st.sidebar.checkbox("Wrap lines", value=False),
            show_gutter=True,
            show_print_margin=True,
            auto_update=False,
            readonly=False,
            key="ace-editor"
        )
        st.write('Hit `CTRL+ENTER` to refresh the page')
        st.write('*Remember to save your code separately!*')

    with display:
        exec(code)

    with st.sidebar:
        libraries_available = st.beta_expander('Available Libraries')
        with libraries_available:
            st.write("""
            * Pandas (pd)
            * Numpy (np)
            [Need something else?](https://github.com/samdobson/streamlit-sandbox/issues/new)
            """)
    
if __name__ == "__main__":
    main()