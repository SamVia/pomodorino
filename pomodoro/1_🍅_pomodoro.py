import streamlit as st
from datetime import timedelta
import time
st.set_page_config(
  page_title="Pomodoro",
  page_icon="https://static.vecteezy.com/system/resources/previews/019/527/038/original/an-8-bit-retro-styled-pixel-art-illustration-of-a-red-garden-tomato-free-png.png", 
)
#code to hide streamlit normal view
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </stile>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

#links
link_start="https://www.htmlcsscolor.com/preview/gallery/ECC75B.png"
link_work = "https://www.htmlcsscolor.com/preview/gallery/77C062.png"
link_pause = "https://www.htmlcsscolor.com/preview/gallery/898CE6.png"
link_finish ="https://www.icegif.com/wp-content/uploads/2022/09/icegif-386.gif"

# Check if the inputs have been submitted
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "selected_video" not in st.session_state:
    st.session_state.selected_video = ("None","")

if "image" not in st.session_state:
  st.session_state.image = "https://www.icegif.com/wp-content/uploads/2022/09/icegif-386.gif"
    
if "sel_sounds" not in st.session_state:
  st.session_state.sel_sounds={
    "work_s": "https://www.myinstants.com/media/sounds/boxing-bell-184.mp3",
    "pause_s": "https://www.myinstants.com/media/sounds/grandfather-clock-chime.mp3",
    "end_s": "https://www.myinstants.com/media/sounds/wonka_youdidit.mp3"
  }    
if "min_work" not in st.session_state:
    st.session_state.min_work = 25
if "min_pause" not in st.session_state:
    st.session_state.min_pause = 5
if "num_cycles" not in st.session_state:
    st.session_state.num_cycles=2   
if "show_animation" not in st.session_state:
    st.session_state.show_animation = True
if "show_timer" not in st.session_state:
    st.session_state.show_timer = True

def generate_rectangles(angle, color, width='8px', height='16px', left='146px', top='142px'):
    return f"""<div class="rectangle" style="
        width: {width};
        height: {height};
        background-color: {color};
        transform-origin: center;
        border: 3px solid rgba(0,0,0,0.07);
        position: absolute;
        left:{left};
        top:{top};
        border-radius:3px;
        transform: rotate({angle-90}deg) translate(150px) rotate(90deg);
    "></div>"""

def animated_timer(color_quarters="#10040E", link_colored = "#721D45", link_normal = "#FFFFFF", image_url = "https://static.vecteezy.com/system/resources/previews/019/527/038/original/an-8-bit-retro-styled-pixel-art-illustration-of-a-red-garden-tomato-free-png.png", total_seconds = 1, current_seconds=1, num_divisions = 24, text="", show_animation = True, show_timer = True, message=""):
    """
    function that generates the markdown text to create an istance of the timer\n
    USAGE: input all the optional attributes that you need these are the default values\n
    remember that the function must be called each time a frame needs to be updated (use the delay you need, ideally 1 sec)
    """
    html_code =""
    
    if show_animation:
        colored_zone = current_seconds*24//total_seconds
        degrees = current_seconds*360//total_seconds
        blank_zone = 24-colored_zone
        html_code += f'<div class="circle" style="position: fixed; width: 300px; height: 300px; border-radius: 50%; border: 1px transparent;top:50%;left:50%;transform: translate(-50%, -50%);">'
        
        for i in range(1, colored_zone+1):
            angle = (i) * (360 / num_divisions)
            html_code += generate_rectangles(angle, link_colored)
        for i in range(1, blank_zone):
            angle = (i+colored_zone) * (360 / num_divisions)
            html_code += generate_rectangles(angle, link_normal)
        
        # Define the positions and dimensions for the four rectangles
        rectangles = [
            {'angle': 0, 'color': color_quarters, 'width': '12px', 'height': '24px', 'left': '144px', 'top': '138px'},
            {'angle': 90, 'color': color_quarters, 'width': '12px', 'height': '24px', 'left': '144px', 'top': '138px'},
            {'angle': 180, 'color': color_quarters, 'width': '12px', 'height': '24px', 'left': '144px', 'top': '138px'},
            {'angle': 270, 'color': color_quarters, 'width': '12px', 'height': '24px', 'left': '144px', 'top': '138px'}
        ]
        
        for rectangle in rectangles:
            html_code += generate_rectangles(**rectangle)
        html_code += f'<div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 24px; z-index: 2; pointer-events: none;">{text}</div>'
        html_code += f'''
            <style>
            div.stButton > button:first-child {{
                height:220px;
                width:220px;
                background-color: transparent;
                background-image: url('{image_url}');
                background-size: cover;
                background-repeat: no-repeat;
                border-color: transparent;
                position: fixed; 
                top: 50%; 
                left: 50%; 
                transform: translate(-50%, -50%) rotate({degrees}deg); 
                border-radius:50%;
                z-index: 1;
            transition: transform 0.3s ease-in-out;
            }}
            div.stButton > button:first-child:hover {{
                transform: translate(-50%, -50%) scale(1.1);
            }}
            </style>
                '''
        html_code += '</div>'
    
    if show_timer:
        text_dim = 75 if show_animation else 100
        transform_values = "-50%, -13%" if show_animation else "-50%, 50%"
        html_code += f"""<div style="
        position: fixed; 
        top: 13%; 
        left: 50%;
        transform: translate({transform_values}); 
        color: white; 
        font-size: {text_dim}px; 
        font-weight:bold; 
        z-index: 2;
        text-shadow: -2px 0 rgba(0,0,0,0.09), 0 2px rgba(0,0,0,0.09), 2px 0 rgba(0,0,0,0.09), 0 -2px rgba(0,0,0,0.09);">
        {message}
        </div>"""
    
    return html_code
  
def play_sound(link):
    html_string = f"""
            <audio autoplay>
              <source src="{link}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)

def set_bg(link):
    command = f"""
            <style>
            [data-testid="stAppViewContainer"] > .main {{
            background-image: url({link});
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: local;
            }}
            [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
            }}
            </style>
            """
    return command

def music_player(id):
    return f"""<iframe style="display:none;" width="560" height="315" src="https://www.youtube.com/embed/{id}?autoplay=1&loop=1&playlist={id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""

st.markdown(music_player(st.session_state.selected_video[1]), unsafe_allow_html=True)
if not st.session_state.submitted:
    # Create an empty container for the input fields
    input_container = st.empty()
    #page_bg_img = f""" <style> [data-testid="stAppViewContainer"] > .main {{ background-image: url({link_start}); background-size: cover; background-position: center center; background-repeat: no-repeat; background-attachment: local; margin-top:-0; }} [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }} </style> """
    st.markdown(set_bg(link=link_start), unsafe_allow_html=True)
    
    st.markdown(animated_timer(message=f"{timedelta(seconds=st.session_state.min_work*60)}", text="Press", show_animation=st.session_state.show_animation, show_timer=st.session_state.show_timer), unsafe_allow_html=True)
    if input_container.button(" ", key = "start_pomodoro"):
        st.session_state.submitted = True
        input_container.empty()  # Empty the container
        time.sleep(0.2)
        st.rerun()
        
else:
    print_container = st.empty()
    for i in range(0,st.session_state.num_cycles):
        st.markdown(set_bg(link_work), unsafe_allow_html=True)  
        play_sound(st.session_state.sel_sounds["work_s"])
        
        #count down timer
        if st.button(" ", key = i):
            st.session_state.submitted = False
            st.empty()  # Empty the container
            st.rerun()
        seconds = st.session_state.min_work * 60
        for s in range(seconds, 0, -1):
            print_container.markdown(animated_timer(message=f"{timedelta(seconds=s)}", text="Press", total_seconds=seconds, current_seconds=seconds-s, show_animation=st.session_state.show_animation, show_timer=st.session_state.show_timer), unsafe_allow_html=True)
            time.sleep(1)
            print_container.empty()
            
            
        #check if there are more than 1 cycle otherwise the pause is meaningless    
        if st.session_state.num_cycles > 1:   
            play_sound(st.session_state.sel_sounds["pause_s"])
            st.markdown(set_bg(link_pause), unsafe_allow_html=True)
            seconds = st.session_state.min_pause * 60
            for s in range(seconds, 0, -1):
                print_container.markdown(animated_timer(message=f"{timedelta(seconds=s)}", text="Press", total_seconds=seconds, current_seconds=seconds-s, show_animation=st.session_state.show_animation, show_timer=st.session_state.show_timer), unsafe_allow_html=True)
                time.sleep(1)
                print_container.empty()
        print_container.empty()
        
    #make button invisible and unclickable (can be found with TAB)    
    print_container.markdown("""<style>
            div.stButton > button:first-child {
                height:2px;
                width:2px;
                background-color: transparent;
                background-size: cover;
                background-repeat: no-repeat;
                border-color: transparent;
                position: fixed; 
                top: 50%; 
                left: 50%; 
                z-index: -1;
            }
            </style>""", unsafe_allow_html=True)
    #finished work screen
    play_sound(st.session_state.sel_sounds["end_s"])
    
    st.markdown(set_bg(st.session_state.image), unsafe_allow_html=True)
    time.sleep(15)

    st.session_state.submitted = False
    st.rerun()