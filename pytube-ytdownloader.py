# MADE AND CREATE BY D1AZDN #
# github/d1azdn #

import streamlit as st
import requests
from bs4 import BeautifulSoup as bs
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from pytube import YouTube as ytb
import pytube
from PIL import Image
import webbrowser

#<=Page Config=>
st.set_page_config(page_title="pytube-ytdownloader", layout='wide')

#<=Load from lottie web=>
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottiecoding = load_lottie("https://lottie.host/53b76bcf-f7ea-404a-9e9d-7ea5261547f1/DUDOI6hD7U.json")

#<=I don't know why i needed this=>
grey = "https://www.solidbackgrounds.com/images/1280x720/1280x720-light-gray-solid-color-background.jpg"

def on_change(key):
    selection = st.session_state[key]

def gantivideo():
    try :
        a = ytb(st.session_state.tinput1)
    except pytube.exceptions.RegexMatchError or pytube.exceptions.VideoUnavailable:
        st.error("Error while checking video. Did you put the right one?")
    else : 
        st.success("Video found! (Scroll down to see.)")
        selection = st.session_state.leftb
        selection['image'] = a.thumbnail_url
        selection['video'] = a.title
        selection['view'] = str(a.views) + " Views."
        selection['author'] = "Channel <-> " + a.author
        selection['link'] = st.session_state.tinput1

def ganti3video():
    with requests.Session() as s :
        sess = ['leftb','midb','rightb']
        pertama = s.get("https://www.youtube.com/results?search_query="+st.session_state.tinput1)
        kedua = bs(pertama.text, 'html.parser')
        ketiga = kedua.find_all('script')
        keempat = ketiga[-6].text.replace("var ytInitialData = ","").replace(";","")
        tes = keempat.split(r'{"videoId":')
        tampung = ["http://youtube.com/watch?v=","http://youtube.com/watch?v=","http://youtube.com/watch?v="]; tampungan = 0
        for a in range(8):
            if a == 1 or a == 4 or a == 7:
                for b in range(12):
                    if b!=0:
                        tampung[tampungan] += tes[a][b]        
                tampungan += 1
        for x in range(3):
            a = ytb(tampung[x])
            selection = st.session_state[sess[x]]
            selection['image'] = a.thumbnail_url
            selection['video'] = a.title
            selection['view'] = str(a.views) + " Views."
            selection['author'] = "Channel <-> " + a.author
            selection['link'] = tampung[x]
        st.success("Video found! (Scroll down to see.)")

#<=First row, the top field=>
### This is for not restarting the browser.
if "menu" not in st.session_state:
    st.session_state.menu = "Search by links"
    st.session_state.leftb = {
        "image" : grey,
        "video" : "",
        "view" : "",
        "author" : "",
        "link" : ""
    }
    st.session_state.midb = {
        "image" : grey,
        "video" : "",
        "view" : "",
        "author" : "",
        "link" : ""
    }
    st.session_state.rightb = {
        "image" : grey,
        "video" : "",
        "view" : "",
        "author" : "",
        "link" : ""
    }
    st.session_state.imagedone = st.session_state.leftb['image']

st.markdown("#")
with st.container():
    lefta, righta = st.columns(2)
    with lefta:
        st.header("Youtube Downloader")
        st.write(
            """Youtube Downloader (pytube-ytdownloader) is a fanmade application that uses python as main language.
            This website was built using the Streamlit library, and with the help of the pytube library 
            to download videos from the YouTube page.
            """
            )
        selected2 = option_menu(None, ["Search by links", "Search on youtube"], 
        icons=['link-45deg', 'search'], 
        default_index=0, orientation="horizontal", key="menu", on_change=on_change)

        st.text_input("", placeholder=st.session_state.menu, label_visibility="collapsed", key="tinput1")
        submit = st.button("Submit")
        if submit :
            if st.session_state.menu == "Search by links" :
                gantivideo()
            if st.session_state.menu == "Search on youtube" :
                ganti3video()
    with righta:
        st_lottie(lottiecoding, height = 300, key ="youtube")

st.write("---")

#<=Second row=>
with st.container():
    st.markdown("<h3 style='text-align: center; color: black;'>Your videos will show here.</h3>", unsafe_allow_html=True)

    leftb,midb,rightb = st.columns(3)
    with leftb:
        st.image(st.session_state.leftb['image'])
        st.subheader(st.session_state.leftb['video'])
        st.text(st.session_state.leftb['view'])
        st.write(st.session_state.leftb['author'])
        if st.button("Link to the original video.", key="1234") :
            webbrowser.open(st.session_state.leftb['link'])
    with midb:
        st.image(st.session_state.midb['image'])
        st.subheader(st.session_state.midb['video'])
        st.text(st.session_state.midb['view'])
        st.write(st.session_state.midb['author'])
        if st.button("Link to the original video.", key="2234") :
            webbrowser.open(st.session_state.midb['link'])
    with rightb:
        st.image(st.session_state.rightb['image'])
        st.subheader(st.session_state.rightb['video'])
        st.text(st.session_state.rightb['view'])
        st.write(st.session_state.rightb['author'])
        if st.button("Link to the original video.", key="3243") :
            webbrowser.open(st.session_state.rightb['link'])

st.write("---")

#<=Third row=>
with st.container():
    leftc,rightc = st.columns(2)
    with leftc:
        st.markdown("<h3 color: black;'>Select your video and type of media</h3>", unsafe_allow_html=True)
        st.write("Choose the video and the type of media you want to download. There are many types you can download here. Unfortunately, there are limitations on downloading video that includes audio. So, find one that suits you better!")
        option1 = st.selectbox("Choose the video here",(f"{st.session_state.leftb['video']}",f"{st.session_state.midb['video']}", f"{st.session_state.rightb['video']}"),key="123")
        sess = ['leftb','midb','rightb']
        for i in range(3) :
            if option1 == st.session_state[sess[i]]['video'] :
                st.session_state.imagedone = st.session_state[sess[i]]['image']
                st.session_state.tinput2 = st.session_state[sess[i]]['link']
                break       
        option2 = st.selectbox("Choose the media type here",("----- Video", "1080p (Video Only)", "720p", "480p (Video Only)", "360p", "----- Audio", "Mp3"),key="456")
        chooseing = {"1080p (Video Only)" : 137 , "720p": 22, "480p (Video Only)": 135, "360p": 18, "Mp3": 140}
        
        option3 = st.button("Download!")
        if option3 :
            st.success("Downloading... (might take a while.)")
            st.text("If the page is running, then it is downloading. \nWait until page is done, then check your file folder :)")
            z = None
            for i in range(5):
                if option2 == list(chooseing.keys())[i] :
                    z = ytb(st.session_state.tinput2)
                    stream = z.streams.get_by_itag(list(chooseing.values())[i])
                    break
            stream.download()

    with rightc:
        st.image(st.session_state.imagedone)
        st.text_input("Link of your url", value = st.session_state.tinput2, key="tinput2")

st.write("---")

#<=Last row=>
with st.container():
    leftd,rightd = st.columns(2)
    with leftd:
        st.header("This Project")
        st.write(
            """This project is my first project using Python programming language. 
            I'm new to coding, so i will improve more on the future. To see my other project, please visit d1azdn's github site.
            """
            )
        if st.button("See more on Github ->") :
            webbrowser.open("https://github.com/d1azdn")
    with rightd:
        l1,l2,l3 = st.columns(3)
        with l2:
            st.image("https://cdn-icons-png.flaticon.com/512/25/25231.png", width=250)