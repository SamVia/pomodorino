import streamlit as st
from datetime import timedelta
import time
import winsound

pixel_adj = 6

#code to hide streamlit normal view
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </stile>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

#sounds
work_sound = r"pomodorino\pomodoro\work.wav"
pause_sound = r"pomodorino\sounds\pause.wav"
finish_sound = r"pomodorino\sounds\finishs.wav"

#links
link_start="https://www.htmlcsscolor.com/preview/gallery/F4CE5B.png"
link_work = "https://www.htmlcsscolor.com/preview/gallery/76E794.png"
link_pause = "https://www.htmlcsscolor.com/preview/gallery/E68585.png"
link_finish ="https://www.icegif.com/wp-content/uploads/2022/09/icegif-386.gif"

# Check if the inputs have been initialized in this session
if "inputs" not in st.session_state:
    # Initialize the inputs with some default values
    st.session_state.inputs = [1, 1, 1]

# Check if the inputs have been submitted
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Create an empty container for the input fields
input_container = st.empty()

if not st.session_state.submitted:
    page_bg_img = f""" <style> [data-testid="stAppViewContainer"] > .main {{ background-image: url({link_start}); background-size: cover; background-position: center center; background-repeat: no-repeat; background-attachment: local; margin-top:-0; }} [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }} </style> """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    # Create the input fields inside the container and store their values in session_state
    col1, col2, col3 = input_container.columns(3)
    with col1: st.session_state.inputs[0] = st.number_input(f'Input {0+1}', value=st.session_state.inputs[0], min_value=1, key=f'Input {0+1}')
    with col2: st.session_state.inputs[1] = st.number_input(f'Input {1+1}', value=st.session_state.inputs[1], min_value=1, key=f'Input {1+1}')
    with col3: st.session_state.inputs[2] = st.number_input(f'Input {2+1}', value=st.session_state.inputs[2], min_value=1,key=f'Input {2+1}')
    
    # Create a button to submit the inputs
    if st.button('Submit Inputs', key='Submit Button'):
        st.session_state.submitted = True
        input_container.empty()  # Empty the container
        time.sleep(0.2)
        st.rerun()
        
else:
    print_container = st.empty()
    for i in range(0,st.session_state.inputs[2]):
        
        page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url({link_work});
background-size: 100% auto;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;

}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""


        st.markdown(f"<style>{page_bg_img}</style>", unsafe_allow_html=True)
        
        #plays sound to start working
        winsound.PlaySound(work_sound, winsound.SND_FILENAME)
        
        #count down timer
        seconds = st.session_state.inputs[0] * 60
        for s in range(seconds, 0, -1):
            
            print_m = f"""
                <div style="display: grid; place-items: center; height: center; padding-top: 7%;">
                    <div style="font-size: 100px; font-weight: bold; color: "white";">
                        {timedelta(seconds=s)}
                    </div>
                </div>
                """

            print_container.markdown(print_m, unsafe_allow_html=True)
            time.sleep(1)
        
        print_container.empty()
        
        page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url({link_pause});
background-size: 100% auto;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;

}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
""" 
       
        st.markdown(page_bg_img, unsafe_allow_html=True)
        
        #plays sound to start the pause
        winsound.PlaySound(pause_sound, winsound.SND_FILENAME)
        
        #count down timer
        seconds = st.session_state.inputs[1] * 60
        for s in range(seconds, 0, -1):
            print_m = f"""
                <div style="display: grid; place-items: center; height: center; padding-top: 7%;">
                    <div style="font-size: 100px; font-weight: bold; color: "white";">
                        {timedelta(seconds=s)}
                    </div>
                </div>
                """
            print_container.markdown(print_m, unsafe_allow_html=True)
            time.sleep(1)
        print_container.empty()
    
    #finished work screen
    
    page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url({link_finish});
background-size: 100% auto;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;

}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    time.sleep(3)
    st.balloons()
    #play sound of finished working
    winsound.PlaySound(finish_sound, winsound.SND_FILENAME)
    st.balloons()

    st.session_state.submitted = False
    st.rerun()