# pytube-ytdownloader
Simple collaborative apps using pytube, streamlit, and beautifulSoup4. 
<br/>
This application mainly focuses on downloading file from YouTube, either just audio or video. This application can also be used as a search on YouTube, and can also be used as a learning medium about Python programming language.
<br/><br/>
*Aplikasi ini berfokus untuk mendownload file dari Youtube, baik itu hanya audio ataupun video. Aplikasi ini dapat digunakan sebagai pencarian di Youtube, dan dapat dijadikan sebagai bahan pembelajaran mengenai bahasa pemograman Python.*

## Project results
![App Screenshot]("./etc/full_image.png")

## Getting Started
There are several python libraries used in this project.
<br/><br/>
*Ada beberapa modul python yang digunakan dalam proyek ini.*
```bash
  streamlit >= 1.26.0
  streamlit_lottie = 0.0.5
  streamlit_option_menu = 0.1
  pytube >= 15.0.0
  beautifulsoup4 >= 4.12.0
  pillow >= 10.0.0
```

## Workflow
1. Navigation in one page
   * Header = Introduction about pytube-ytdownload
   * Body = Search by links or Search on Youtube <br/>
            $~~~~~~~~~~~~~$ Changing from square to picture from youtube <br/>
            $~~~~~~~~~~~~~$ Picking which videos, and choosing type data. Then download it.
   * Footer = Link to my github.
2. Downloaded file will appear on your file directory.
3. Audio and video are saved with .mp4 format
4. Some video are not having audio (YouTube's coding no longer includes links to such files)
<br/>
<= Indonesia => <br/>
1. Navigasi hanya di satu halaman <br/>
2. File yang telah di download akan tersimpan di directory file tersebut <br/>
3. Audio dan video tersimpan dalam format mp4 <br/>
4. Beberapa video tidak memiliki suara (Kodingan YouTube telah diubah) <br/>

## Clone
Clone this project :
```bash
git clone https://github.com/d1azdn/pytube-ytdownloader
```
