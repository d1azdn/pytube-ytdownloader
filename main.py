import ytConnect
import convert
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import webbrowser
from pytube import YouTube as ytb
import pytube
import random

st.set_page_config(page_title="ytb-load", layout='wide')

greyBackground = "https://www.solidbackgrounds.com/images/1280x720/1280x720-light-gray-solid-color-background.jpg"

if "menu" not in st.session_state:
    st.session_state.menu = "Search by links"
    st.session_state.obj1 = {
        "image" : greyBackground,
        "title" : "",
        "view" : "",
        "author" : "",
        "link" : ""
    }
    st.session_state.obj2 = {
        "image" : greyBackground,
        "title" : "",
        "view" : "",
        "author" : "",
        "link" : ""
    }
    st.session_state.obj3 = {
        "image" : greyBackground,
        "title" : "",
        "view" : "",
        "author" : "",
        "link" : ""
    }

def on_change(key):
    selection = st.session_state[key]

def videoShow(var):
    session = ['obj1','obj2','obj3']
    if var == 3 : 
        ytList = ytConnect.ytConnecting()
        ytList = ytList.session(st.session_state.textInput)

        for loop in range(3):
            ytObj = ytb(ytList[loop])
            select = st.session_state[session[loop]]
            select['image'] = ytObj.thumbnail_url
            select['title'] = ytObj.title
            select['view'] = str(ytObj.views) + " Views."
            select['author'] = "Channel <-> " + ytObj.author
            select['link'] = ytList[loop]
    else :
        for loop in range(3):
            ytObj = ytb(st.session_state.textInput)
            select = st.session_state[session[loop]]
            select['image'] = ytObj.thumbnail_url
            select['title'] = ytObj.title
            select['view'] = str(ytObj.views) + " Views."
            select['author'] = "Channel <-> " + ytObj.author
            select['link'] = st.session_state.textInput

def downloadButton(var,input):
    if var == "Mp3":
        streamSound = ytb(input['link']).streams.get_by_itag(140)
        streamSound.download(filename=f"outputs/{input['title']}.mp3")
        return
    
    for loop in range(5):
        if var == list(choose.keys())[loop] and var != "Mp3":
            stream = ytb(input['link']).streams.get_by_itag(list(choose.values())[loop])
            streamSound = ytb(input['link']).streams.get_by_itag(140)

            print("Downloading the video...")
            stream.download(filename="Video.mp4",)

            print("Downloading the Audio...")
            streamSound.download(filename="Audio.mp3")

            print("Combining the pieces...")
            convert.combine_audio("Video.mp4", "Audio.mp3", f"outputs/{input['title']}.mp4")

class streamlitContainer :
    def container(self,input):
        with st.container():
            match input:
                case 1:
                    pass

                case 2:
                    self.left, self.right = st.columns(2)

                case 3:
                    self.left, self.middle, self.right = st.columns(3)

                case _: return
    
    def setMid(self,input):
        a,b,c = st.columns(3)
        with b :
            st.image(input, width=250)

    def setContent(self,input):
        st.image(input['image'])
        st.subheader(input['title'])
        st.text(input['view'])
        st.write(input['author'])
        if st.button("Link to the original video", key=random.randint(0,100)) :
            webbrowser.open(f"{input['link']}")

st.markdown("<h1 style='text-align: center;'>ytb-load</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Python web-apps for downloading video/audio from YouTube</p>", unsafe_allow_html=True)
select = option_menu(None, ["Search by links", "Search on youtube"], 
        icons=['link-45deg', 'search'], 
        default_index=0, orientation="horizontal", key="menu", on_change=on_change)
st.text_input(label=" ", placeholder=st.session_state.menu, label_visibility="collapsed", key="textInput")
if st.button("Submit", use_container_width=True) :
    if st.session_state.menu == "Search by links" :
        videoShow(1)
    elif st.session_state.menu == "Search on youtube" :
        videoShow(3)
st.markdown("#")
st.markdown("#")

st.write("---")

st.markdown("<h3 style='text-align: center;'>Your videos will show here.</h3>", unsafe_allow_html=True)

content = streamlitContainer()
content.container(3)
with content.left :
    content.setContent(st.session_state.obj1)
with content.middle :
    content.setContent(st.session_state.obj2)
with content.right :
    content.setContent(st.session_state.obj3)

st.markdown("#")
downloadContent = streamlitContainer()
downloadContent.container(3)
choose = {"1080p" : 137 , "720p": 22, "480p": 135, "360p": 18, "Mp3": 140}
with downloadContent.left :
    option = st.selectbox("Choose the media type here",("----- Video", "1080p", "720p", "480p", "360p", "----- Audio", "Mp3"),key="456")
    if st.button("Download!", key='654'):
        downloadButton(option, st.session_state.obj1)
with downloadContent.middle :
    option1 = st.selectbox("Choose the media type here",("----- Video", "1080p", "720p", "480p", "360p", "----- Audio", "Mp3"),key="457")
    if st.button("Download!", key='546'):
        downloadButton(option1, st.session_state.obj2)
with downloadContent.right :
    option2 = st.selectbox("Choose the media type here",("----- Video", "1080p", "720p", "480p", "360p", "----- Audio", "Mp3"),key="458")
    if st.button("Download!", key='465'):
        downloadButton(option2, st.session_state.obj3)


st.write("---")
st.markdown("#")
bottom = streamlitContainer()
bottom.container(2)
bottom.left.title("What is ytb-load ?")
bottom.left.write("Youtube downloader (ytb-load) is an application that uses to download youtube video/audio.")

with bottom.right:
    bottom.setMid("https://icons.iconarchive.com/icons/dtafalonso/android-l/256/Youtube-icon.png")

st.write("---")
st.markdown("#")
footer = streamlitContainer()
footer.container(2)
footer.right.title("About this Project")
footer.right.write("This is my first project for python language. I will happy to accept any suggestion you share with me ^^.")
footer.right.write("My Github page linked down below.")
if footer.right.button("See more on Github ->") :
    webbrowser.open("https://github.com/d1azdn")

with footer.left:
    footer.setMid("https://cdn-icons-png.flaticon.com/512/25/25231.png")