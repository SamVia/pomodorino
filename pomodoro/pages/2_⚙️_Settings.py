import streamlit as st
from zoneinfo import available_timezones
import base64


st.set_page_config(
  page_title="Pomodoro",
  page_icon="🍅"
)
st.title("Settings:")

hide_st_style = """<style> header {visibility: hidden;} footer {visibility: hidden;} </stile>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

if "color" not in st.session_state:
  st.session_state.color = "#ffffff"

if "sounds" not in st.session_state:
    st.session_state.sounds = {
     #create different options: "sound_name":"link_to_sound"   
        "Announcement Tone":"https://orangefreesounds.com/wp-content/uploads/2023/07/Announcement-tone.mp3?_=1",
        "Marimba":"https://orangefreesounds.com/wp-content/uploads/2023/04/Marimba-notification-tone.mp3?_=1",
        "Soft Bell":"https://orangefreesounds.com/wp-content/uploads/2023/04/Soft-bell-notification-tone.mp3?_=1",
        "Ding Dong":"https://orangefreesounds.com/wp-content/uploads/2022/12/Notification-ding-dong-sound-low-tone.mp3?_=1",
        "Simple Notification":"https://orangefreesounds.com/wp-content/uploads/2022/06/Simple-notification-sound.mp3?_=1",
        "Flute":"https://www.orangefreesounds.com/wp-content/uploads/2022/04/Flute-notification-ringtone.mp3?_=1",
        "Chime":"https://www.orangefreesounds.com/wp-content/uploads/2021/11/Simple-sms-tone.mp3?_=1",
    }
if "sel_sounds" not in st.session_state:
  st.session_state.sel_sounds={
    "work_s": 1,
    "pause_s": 1,
    "end_s":1
  }

if "min_work" not in st.session_state:
    st.session_state.min_work = 25
if "min_pause" not in st.session_state:
    st.session_state.min_pause = 5

if "selected_video" not in st.session_state:
    st.session_state.selected_video = ("None","")

#function to change format from printable to executable


#function to extract the index of the current timezone:
def get_index(val):
  return st.session_state.timezones.index(val)
def get_image_data_url(img_bytes):
    encoded = base64.b64encode(img_bytes).decode()
    return f"data:image/png;base64,{encoded}"
#save timezone value:

st.session_state.color = st.color_picker("select a color", st.session_state.color)

st.session_state.min_work = st.number_input("select minutes of work", min_value=1, value = st.session_state.min_work)
st.session_state.min_pause = st.number_input("select minutes of pause", min_value=1, value = st.session_state.min_pause)


col1, col2, col3 = st.columns(3)

with col1:
  key = st.selectbox("select", list(st.session_state.sounds.keys()), key="work")
  st.session_state.sel_sounds["work_s"] = st.session_state.sounds[key]
  if st.button("test"):
    html_string = f"""
            <audio autoplay>
              <source src="{st.session_state.sel_sounds["work_s"]}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)

with col2:
  key = st.selectbox("select", list(st.session_state.sounds.keys()),key="pause")
  st.session_state.sel_sounds["pause_s"] = st.session_state.sounds[key]
  if st.button("test",key=4):
    html_string = f"""
            <audio autoplay>
              <source src="{st.session_state.sel_sounds["pause_s"]}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)


with col3:
  key = st.selectbox("select", list(st.session_state.sounds.keys()),key= "finish")
  st.session_state.sel_sounds["end_s"] = st.session_state.sounds[key]
  if st.button("test",key=1):
    html_string = f"""
            <audio autoplay>
              <source src="{st.session_state.sel_sounds["end_s"]}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "gif"])
if uploaded_file is not None:
  st.session_state.image = get_image_data_url(uploaded_file.read())
  
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
        "8D Binaural":"n0SpKMnkPec"  
    }
    
list_keys = list(st.session_state.videos.keys())#easy way to get all names of choices
sel_obj = st.session_state.selected_video[0]#extract the current name
col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div style="display:flex; font-size: 30px; justify-content:center; align-items:center; font-weight: bold; color: "white";">
                            Beats🎶
                        </div>""",unsafe_allow_html=True)
    key = st.selectbox("select ambient music", list_keys, index = list_keys.index(sel_obj), label_visibility="collapsed")

st.session_state.selected_video = (key,st.session_state.videos[key])


  