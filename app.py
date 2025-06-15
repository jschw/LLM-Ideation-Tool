import streamlit as st
import time
import os, signal
from utils.llm import LLMHandler
from utils.workflows import LinearWorkflow
from dotenv import dotenv_values

def main():
  

  try:
    if 'initialized' not in st.session_state or not st.session_state.initialized:
      if 'config' not in st.session_state:
        st.session_state['config'] = dotenv_values(".env")
        
      if 'workflow' not in st.session_state:
        st.session_state['workflow'] = LinearWorkflow()
        
      if 'persistent_text' not in st.session_state:
        st.session_state['persistent_text'] = ""

    st.title("Markdown Live viewer")

    widget = st.empty()

    while True:

      new_txt = input("-> ")

      if new_txt == "/quit":
        os.kill(os.getpid(), signal.SIGKILL)
      
      elif new_txt == "/clear":
        st.session_state['persistent_text'] = ""
        new_txt = ""
        st.rerun()

      st.session_state['persistent_text'] += f"{new_txt}\n\n"

      widget.markdown(st.session_state['persistent_text'])

    
  except Exception:
    print("Error")
    pass

if __name__ == '__main__':
  main()
