import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="GODKING MUSIC", page_icon="🎵")

# CSS ស្អាតបែប Apple Music
st.markdown("""
    <style>
    .main { background-color: #000000; }
    h1 { color: #FA243C; text-align: center; }
    .stAudio { background-color: #1C1C1E; border-radius: 30px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🎵 GODKING MUSIC</h1>", unsafe_allow_html=True)

url = st.text_input("", placeholder="បិទភ្ជាប់ Link ចម្រៀងនៅទីនេះ...")

if url:
    try:
        with st.spinner("⏳ កំពុងស្វែងរក..."):
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'song.mp3',
                'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                st.image(info.get('thumbnail', ''), use_container_width=True)
                st.subheader(info.get('title', 'Music'))
            
            with open("song.mp3", "rb") as f:
                st.audio(f.read(), format="audio/mp3")
                st.download_button("📥 ទាញយកទុកស្ដាប់ Offline", f, "music.mp3", "audio/mpeg")
            os.remove("song.mp3")
    except:
        st.error("រកមិនឃើញចម្រៀងនេះទេ!")
