def main():
   
    import streamlit as st
   
    with st.echo():                                     
      
        import streamlit as st
      
        st.title("IMPORT and USE YOUR CUSTOM FUNCTIONS")
        
        st.write(
        """ 
        IMPORT CUSTOM FUNCTIONS from .py files
        
        - The default working directory path will be always the same of the file run by `streamlit run app.py`, i.e., the one used to run the app (`app.py`, in this case). 
        
        - The paths of the files containing the functions to be imported __must be in the same directory tree__ of the default working directory
        
        - Also the paths will be __relative paths__ to the default working directory. 
        
        - Hence, for example, to import function `function1` from
          `custom_functions.py` in the folder `functions_folder` the command would
          be: 
        `from functions_folder.custom_functions import function1`
        
        
        - So, keep in mind that when pages of a multipage app are run separately, their default working directory will change (it will be their own folder directory), so that the functions files will not be able to be imported. There are 3 solutions to that:
        
            - __Method 1:__ Move the functions files to the same folder tree of your new default working directory.
            
            - __Method 2:__ Insert the functions files paths to your `sys.path` list:  
            `current_path = os.path.abspath('.')`  
            `parent_path = os.path.dirname(current_path)`  
            `sys.path.append(parent_path)`  
            `import os, sys`  
            `dir_path = os.path.dirname(os.path.realpath(__file__))` 
            `parent_dir_path=os.path.abspath(os.path.join(dir_path, os.pardir))`  
            `sys.path.insert(0, parent_dir_path)`  
            `for p in sys.path: print(p)`  
        
        - __Method 3:__ Use specialized functions to accomplish this task (i.e., import as a module a .py script from another directory). Example:  
        
        `import importlib.machinery`  
        `filepath = 'D:/.../functions_folder/custom_functions.py'`  
        `custom_functions = importlib.machinery.SourceFileLoader('', filepath).load_module('')`  
        `function1 = custom_functions.function1`  
        
        NOTE: those commands are deprecated but so far are still working. See
        the new method in the last block of
        <https://stackoverflow.com/a/19011259/13684783>
        
        - To update imported functions, you have to reload the IDE / kernel.
        """
        )   
        
    st.header("EXAMPLE")
    st.write('''Import and use functions `custom_sum` and `custom_mean` 
                from `arithmetic_functions.py` file, which is inside `myfunctions` folder''')
    with st.echo():
        from myfunctions.arithmetic_functions import custom_sum
        from myfunctions.arithmetic_functions import custom_mean
        st.write( custom_sum([2,4]) )
        st.write( custom_mean([2,4]) )
        

if __name__ == "__main__":
    main()