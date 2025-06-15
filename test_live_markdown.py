import streamlit as st
import time
import os, signal

def main():
  try:
    st.title("Markdown Live viewer")

    widget = st.empty()

    persistent_text = ""

    while True:

      new_txt = input("-> ")

      if new_txt == "/quit":
        os.kill(os.getpid(), signal.SIGKILL)
      
      elif new_txt == "/clear":
        persistent_text = ""
        new_txt = ""
        st.rerun()

      persistent_text += f"{new_txt}\n\n"

      widget.markdown(persistent_text)

    
  except Exception:
    print("Error")
    pass

if __name__ == '__main__':
  main()
