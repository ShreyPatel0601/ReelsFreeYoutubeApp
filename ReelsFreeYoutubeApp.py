import requests
import streamlit as st

# 🔑 Insert your YouTube API key here
API_KEY = "AIzaSyAgJ24uDnRzFmmBIl7nhJZnPmZYQKubqEo"
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

# 📽️ Function to get videos from YouTube API
def get_videos(query, max_results=5):
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': max_results,
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        return []

# 🎨 Streamlit App UI
st.title("YouTube Informative Video Search")
query = st.text_input("Enter a topic (e.g. Tech News, Science, AI)")

if query:
    videos = get_videos(query)
    if videos:
        for video in videos:
            video_id = video['id']['videoId']
            title = video['snippet']['title']
            channel = video['snippet']['channelTitle']
            thumbnail = video['snippet']['thumbnails']['medium']['url']
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            st.image(thumbnail, width=320)
            st.markdown(f"### [{title}]({video_url})")
            st.write(f"Channel: {channel}")
            st.markdown("---")
    else:
        st.warning("No videos found. Try a different keyword.")
