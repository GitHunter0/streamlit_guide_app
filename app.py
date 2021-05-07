
#%% _______________________________________________________________


#%% INSTALL MODULES

if False:
    '''
    !pip install --upgrade streamlit # For conda envs, use conda-forge instead
    !conda install --channel=conda-forge streamlit
    !python -m pip install --upgrade streamlit-ace streamlit-tags
    !python -m pip install --upgrade numpy pandas scipy openpyxl
    !python -m pip install --upgrade plotnine plotly kaleido
    '''


#%% IMPORT MODULES

# NOTE: if an error occurs, it means a module is missing and must be installed
import streamlit as st
import pandas as pd
import numpy as np
#
import scipy, statsmodels, openpyxl # accessories
import datetime, re # deal with date/time and regex
import plotnine, plotly, kaleido # plotting modules
#
import base64
import PIL
import requests


#%% INITIAL LAYOUT SETTINGS

import streamlit as st

st.set_page_config(page_title='Streamlit Demonstration App', 
                   # set Streamlit logotype as the favicon
                   page_icon="Streamlit_Logo_1.jpg", # None, ":memo:", ...
                   layout='wide', # centered, wide
                   initial_sidebar_state='expanded' # auto, expanded, collapsed
                   )

if False:
    # Hide Hamburger Menu and Streamlit logo 'Made with Streamlit'
    hide_menu_footer = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_footer, unsafe_allow_html=True)


#%% IMPORT AND LOAD PAGES VIA RADIO BUTTON

# Import pages .py files as modules
import pages.home
import pages.references
import pages.import_custom_functions
import pages.headers__texts
import pages.media_inputs
import pages.information
import pages.latex_math
import pages.functions_with_st_elements
import pages.display
import pages.mutate_data
import pages.download_button
import pages.uploads
import pages.url_links
import pages.multipage_app_with_radio_button
import pages.sidebar
import pages.control_flow
import pages.spinner
import pages.share_app_with_ngrok
import pages.themes
import pages.sandbox
import pages.page_config
import pages.selectors
import pages.sliders
import pages.maps
import pages.html_css
import pages.other_inputs
import pages.embed_web_apps_sites
import pages.cache
import pages.selectors_sliders_chain
import pages.plots_color_picker
import pages.layout
import pages.text_tag_inputs
import pages.forms


# Create dictionary with the imported pages
PAGES = {
    "Home": pages.home,
    "Basic Information & Tricks": pages.information,
    "References": pages.references,
    "Display": pages.display,
    "Headers & Text": pages.headers__texts,
    "Sidebar": pages.sidebar,
    "Selectors": pages.selectors,
    "Sliders": pages.sliders,
    "Chain of Selectors and Sliders": pages.selectors_sliders_chain,
    "Text & Tag Inputs": pages.text_tag_inputs,
    "Forms": pages.forms,
    "Other Input Types": pages.other_inputs,
    "Plots & Color Picker": pages.plots_color_picker,
    "Maps": pages.maps,
    "Image & Audio & Video": pages.media_inputs,
    "Latex & Math Formulas": pages.latex_math,
    "URL Links": pages.url_links,
    "Download Button": pages.download_button,
    "Upload Files": pages.uploads,
    "Control Flow": pages.control_flow,
    "Spinner": pages.spinner,
    "Multipage App via Radio Button": pages.multipage_app_with_radio_button,
    "Custom Functions": pages.import_custom_functions,
    "Functions with Streamlit Elements": pages.functions_with_st_elements,
    "Cache": pages.cache,
    "Page Configuration": pages.page_config,
    "Customized Themes": pages.themes,
    "Layout": pages.layout,    
    "Embed Websites and Web Apps": pages.embed_web_apps_sites,
    "HTML/CSS": pages.html_css,
    "Mutate Data": pages.mutate_data,
    "Share App with ngrok": pages.share_app_with_ngrok,
    "Streamlit Sandbox": pages.sandbox,
}

st.sidebar.title("Menu")

# Radio Button - Select page to be displayed
choice = st.sidebar.radio("Navigate", list(PAGES.keys()))

# Call main() function from the selected page
PAGES[choice].main()


#%% SIDEBAR TEXT

st.sidebar.title("About")
st.sidebar.info(
    """
    This app was built solely for educational purposes. In case of any doubt, 
    [contact me](https://wa.me/<insert-your-number-here>?text=How%20can%20I%20help?).
    """
)

#%% _________________________________________________________

