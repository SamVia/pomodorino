import streamlit as st

st.set_page_config(
  page_title="Pomodoro",
  page_icon="🍅"
)

def button_logo(site, logo, circle):
    if circle: circle = "border-radius:50%;"
    else: circle = ""
    return f"""
<style>
    .myButton {{
        background-color: transparent;
        color: white;
        padding: 10px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 0px;
        cursor: pointer;
        border: none;
        border-radius: 50%;
        transition: transform .2s;
        outline: none;
        position:relative;
        left:-20px
    }}

    .myButton:hover {{
        transform: scale(1.1);
    }}
</style>

<a href="{site}" class="myButton" target="_blank">
    <button class="myButton">
        <img src="{logo}" alt="Image description" style="width:50px;height:50px;{circle}">
    </button>
</a>
"""

st.title("Credits")

col1, col2,col3 = st.columns(3)
with col1:
    st.markdown("""
                <div class="image-container">
    <img src="https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg" alt="Description of the image" 
    style="
    height: auto; 
    width: 400px;
    border-radius: 5px;
    padding:20px;
    position:relative;
    left:-160px;
    box-shadow: 0 0 10px rgba(100, 100, 100, 0.1);">
</div>
                
                
            """,unsafe_allow_html=True)
    st.markdown("""<!DOCTYPE html>
<html>
<head>
    <style>
        .myDiv {
            width: 400px; /* Width of the div */
            height: auto; /* Height of the div */
            padding: 20px; /* Inner space of the div */
            margin: 10px; /* Outer space of the div */
            background-color: transparent; /* Background color of the div */
            border: transparent; /* Border around the div */
            font-size: 16px; /* Text size in the div */
            color: #f0f0f0; /* Text color in the div */
            text-align: justify; /* Text alignment in the div */
            position:relative;
            left:-170px;
        }
        .myDiv img {
            display: inline-block;
            width: auto;
            height: 40px;
            position: relative;
            top:5px;
        }
    </style>
</head>
<body>
<div class="myDiv">
    Tools used:
    <br>
    <img src="https://global.discourse-cdn.com/business7/uploads/streamlit/original/2X/f/f0d0d26db1f2d99da8472951c60e5a1b782eb6fe.png" alt="">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/935px-Python-logo-notext.svg.png" alt="" style="position:relative; top:7px; left: 5px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/CSS3_and_HTML5_logos_and_wordmarks.svg/1280px-CSS3_and_HTML5_logos_and_wordmarks.svg.png" alt="" style="position:relative; right:-10px;">
</div>
</body>
</html>
       """
                
                
                , unsafe_allow_html=True)


with col3:
    pres_text="""
    <head>
    <style>
    .custom-text {
      /* Dimension Properties */
      width: 400px;
      height: auto;

      /* Padding and Margin Properties */
      padding: 20px;
      margin: 10px;

      /* Border Properties */
      border-width: 2px;
      border-style: solid;
      border-color: black;
      border-radius: 10px;

      /* Background Properties */
      background-color: #000000;

      /* Text Properties */
      color: white;
      text-align: center;
      font-size: 16px;

      /* Display Properties */
      display: block;

      /* Positioning Properties */
      position: relative;
      left:-160px;

      /* Transition Properties */
      transition: all 0.5s ease;
    }
  </style>
  </head>
  <body>
    <div class="custom-text">
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras quis sagittis ipsum. Ut eget sagittis purus. Etiam lacus elit, aliquet nec feugiat non, venenatis id est. Sed id laoreet purus, vel consequat arcu. Pellentesque mollis, quam sit amet imperdiet tempus, lorem neque finibus leo, commodo iaculis lacus lorem sit amet lorem. Vivamus maximus justo diam, a pharetra lacus lobortis at. Nunc viverra lacus enim, vel finibus libero elementum tempor. Curabitur sagittis pretium augue. Praesent luctus ullamcorper tortor ut consequat. Morbi semper neque id molestie euismod. Maecenas ornare leo at risus venenatis, in molestie metus tempor. Nam id odio sem. Fusce in diam viverra, vestibulum libero at, facilisis dolor. Mauris erat dolor, imperdiet in eros eget, iaculis laoreet tellus. Suspendisse potenti. Vivamus consectetur ullamcorper libero, ac interdum lorem auctor et.
</div>
</body>  
    
    
    """
    
    st.markdown(pres_text, unsafe_allow_html=True)


    columns = col3.columns(4)
    
    with columns[1]:
        st.markdown(button_logo("","https://miro.medium.com/v2/resize:fit:400/1*MgGIm08OdUTUvgNyaUl0hw.jpeg",True), unsafe_allow_html=True)
    with columns[2]:
        st.markdown(button_logo("","https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",False), unsafe_allow_html=True)
    with columns[3]:
        st.markdown(button_logo("","https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png",True), unsafe_allow_html=True)





