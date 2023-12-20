import streamlit as st
import base64

st.set_page_config(
  page_title="Pomodoro",
  page_icon="🍅", 
  initial_sidebar_state="collapsed"
)
st.title("Settings:")

hide_st_style = """<style> header {visibility: hidden;} footer {visibility: hidden;} </stile>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# if "color" not in st.session_state:
#   st.session_state.color = "#ffffff"

if "sounds" not in st.session_state:
    st.session_state.sounds = {
     #create different options: "sound name":"link_to_sound"   
        "Announcement Tone":"https://orangefreesounds.com/wp-content/uploads/2023/07/Announcement-tone.mp3?_=1",
        "Marimba":"https://orangefreesounds.com/wp-content/uploads/2023/04/Marimba-notification-tone.mp3?_=1",
        "Soft Bell":"https://orangefreesounds.com/wp-content/uploads/2023/04/Soft-bell-notification-tone.mp3?_=1",
        "Ding Dong":"https://orangefreesounds.com/wp-content/uploads/2022/12/Notification-ding-dong-sound-low-tone.mp3?_=1",
        "Simple Notification":"https://orangefreesounds.com/wp-content/uploads/2022/06/Simple-notification-sound.mp3?_=1",
        "Flute":"https://www.orangefreesounds.com/wp-content/uploads/2022/04/Flute-notification-ringtone.mp3?_=1",
        "Chime":"https://www.orangefreesounds.com/wp-content/uploads/2021/11/Simple-sms-tone.mp3?_=1",
        "Boxe": "https://www.myinstants.com/media/sounds/boxing-bell-184.mp3",
        "Old Clock": "https://www.myinstants.com/media/sounds/grandfather-clock-chime.mp3",
        "You Did IT!": "https://www.myinstants.com/media/sounds/wonka_youdidit.mp3"
    }
if "sel_sounds" not in st.session_state:
  st.session_state.sel_sounds={
    "work_s": "https://www.myinstants.com/media/sounds/boxing-bell-184.mp3",
    "pause_s": "https://www.myinstants.com/media/sounds/grandfather-clock-chime.mp3",
    "end_s": "https://www.myinstants.com/media/sounds/wonka_youdidit.mp3"
  }
if "image" not in st.session_state:
  st.session_state.image = "https://www.icegif.com/wp-content/uploads/2022/09/icegif-386.gif"
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "min_work" not in st.session_state:
    st.session_state.min_work = 25
if "min_pause" not in st.session_state:
    st.session_state.min_pause = 5
if "num_cycles" not in st.session_state:
    st.session_state.num_cycles=2
    
if "selected_video" not in st.session_state:
    st.session_state.selected_video = ("None","")

if "show_animation" not in st.session_state:
    st.session_state.show_animation = True
if "show_timer" not in st.session_state:
    st.session_state.show_timer = True

#FUNCTIONS:

def get_image_data_url(img_bytes):
    encoded = base64.b64encode(img_bytes).decode()
    return f"data:image/png;base64,{encoded}"

def extract_youtube_id(url):
    start = url.find("?v=") + 3
    end = url.find("&", start)
    if end == -1:
        end = len(url)
    return url[start:end]

#in case of switching to other pages
st.session_state.submitted = False


col1, col2, col3 = st.columns(3)
with col1:
  st.session_state.min_work = st.number_input("select minutes of work", min_value=1, value = st.session_state.min_work)
with col2:
  st.session_state.min_pause = st.number_input("select minutes of pause", min_value=1, value = st.session_state.min_pause)
with col3:
  st.session_state.num_cycles = st.number_input("select number of cycles", min_value=1, value = st.session_state.num_cycles)
#list of all values and all keys, look up if need to change to just two lists
list_keys = list(st.session_state.sounds.keys())
list_dvals = list(st.session_state.sounds.values())
"-------"
list_vals = list(st.session_state.sel_sounds.values())
# st.session_state.color = st.color_picker("select a color", st.session_state.color)
with col1:
  key = st.selectbox("Work sound", list_keys, key="work", index=list_dvals.index(list_vals[0]))
  st.session_state.sel_sounds["work_s"] = st.session_state.sounds[key]
  if st.button("test"):
    html_string = f"""
            <audio autoplay>
              <source src="{st.session_state.sel_sounds["work_s"]}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)

with col2:
  key = st.selectbox("Pause sound", list_keys,key="pause", index=list_dvals.index(list_vals[1]))
  st.session_state.sel_sounds["pause_s"] = st.session_state.sounds[key]
  if st.button("test",key=4):
    html_string = f"""
            <audio autoplay>
              <source src="{st.session_state.sel_sounds["pause_s"]}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)


with col3:
  key = st.selectbox("Finish sound", list_keys, key= "finish", index=list_dvals.index(list_vals[2]))
  st.session_state.sel_sounds["end_s"] = st.session_state.sounds[key]
  if st.button("test",key=1):
    html_string = f"""
            <audio autoplay>
              <source src="{st.session_state.sel_sounds["end_s"]}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)
with col1:
  uploaded_file = st.file_uploader("Choose an for background image...", type=["png", "jpg", "jpeg", "gif"])
  if uploaded_file is not None:
    st.session_state.image = get_image_data_url(uploaded_file.read())
with col2:
  st.session_state.show_timer = st.checkbox("Show Timer", value=st.session_state.show_timer, key="timer")

with col3:
  st.session_state.show_animation = st.checkbox("Show Animation", value=st.session_state.show_animation, key="animation")
if "videos" not in st.session_state:
    st.session_state.videos = {
        "None":"",
        "Pokemon": "YMEblRM4pGc",
        "Minecraft": "0KvlwMd3C4Y",
        "Lofi Girl": "BTYAsjAVa3I",
        "Upbeat Classical": "mv5SZ7i6QLI",
        "Classical Music":"jgpJVI3tDbY",
        "Upbeat Study":"xcwA5h85AvA",
        "Soft Techno":"7j0yL8A-k4E",
        "8D Binaural":"n0SpKMnkPec",
        "Input youtube link":"" 
    }
    
list_keys = list(st.session_state.videos.keys())#easy way to get all names of choices
sel_obj = st.session_state.selected_video[0]#extract the current name
col1, col2 = st.columns(2)
with col1:
  st.markdown("""<div style="display:flex; font-size: 30px; justify-content:center; align-items:center; font-weight: bold; color: "white";">
                          Beats🎶
                      </div>""",unsafe_allow_html=True)
  key = st.selectbox("select ambient music", list_keys, index = list_keys.index(sel_obj), label_visibility="collapsed")
  
  if key == "Input youtube link":
    text = st.text_input("input link:", placeholder="https://www.youtube.com/watch?v=xxxxxxxxxxx")  
    text = extract_youtube_id(text)
    if len(text) != 11:
      st.toast("Please input a valid youtube link")
    else:
      st.session_state.videos[key]=text
      st.toast("Youtube link accepted!")



st.session_state.selected_video = (key,st.session_state.videos[key])
#in case of switching to other pages
st.session_state.submitted = False
