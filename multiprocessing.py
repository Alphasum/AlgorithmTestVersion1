import streamlit as st
import multiprocessing
import os

# Define a function to run your Streamlit app
def run_streamlit_app():
    os.system('streamlit run 0_🛖_Home.py')

# Define a function to start a new process and run the Streamlit app
def start_new_process():
    p = multiprocessing.Process(target=run_streamlit_app)
    p.start()
    return p

# Check if the app is running in the main process
if __name__ == "__main__":
    # Get the current process ID
    current_pid = os.getpid()

    # Try to find an existing process that is running the same app
    found_existing_process = False
    for pid in multiprocessing.active_children():
        if pid != current_pid:
            found_existing_process = True
            break

    # If an existing process is found, show a message and exit
    if found_existing_process:
        st.write("Another instance of this app is already running. Starting new instance")
        start_new_process()
    # If no existing process is found, start a new process and run the app
    else:
        st.write("Starting a new instance of the app...")
        start_new_process()

