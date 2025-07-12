import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Spotify credentials
SPOTIFY_CLIENT_ID = "ff38566fa1334ff2b195af082fd80abe"
SPOTIFY_CLIENT_SECRET = "7f83c07e1a4e4e198fe2b1a8542001c2"

# Spotify vibe-playlist
vibe_playlists = {
    "Soft but strong": {
        "title": "Wild Roses",
        "artist": "Hope Sandoval & The Warm Inventions",
        "url": "https://open.spotify.com/track/3YCcGDqtN7aZhkTu3c2nEU?si=4db2932907d44aa6"
    },
    "Chaotic good": {
        "title": "Cool Cat",
        "artist": "Queen",
        "url": "https://open.spotify.com/track/7nhWtCc3v6Vem80gYPlppQ?si=406e907dadb84bad"
    },
    "Sad but pretty": {
        "title": "Thinking About You",
        "artist": "Radiohead",
        "url": "https://open.spotify.com/track/46tfxn5lP7Qsbz7NHsj9iu?si=89302054b51248c4"
    },
    "Main character in a rainy scene": {
        "title": "I Still Do",
        "artist": "The Cranberries",
        "url": "https://open.spotify.com/track/7EJvwHjf9NKCmYBBGOuwQS?si=4cabbfadfd1f4b25"
    },
    "Divine Chaos in Low Power Mode": {
        "title": "Instant Crush (feat. Julian Casablancas)",
        "artist": "Daft Punk, Julian Casablancas",
        "url": "https://open.spotify.com/track/2cGxRwrMyEAp8dEbuZaVv6?si=d87f4dc00a84432e"
    },
    "Gentle villain arc": {
        "title": "Champagne Supernova",
        "artist": "Oasis",
        "url": "https://open.spotify.com/track/2V5SGZFsF1yoDakHRwrmma?si=eb2a5b4d0d214ec1"
    },
    "Overthinker with nice hands": {
        "title": "Luna - 2011 Remaster",
        "artist": "The Smashing Pumpkins",
        "url": "https://open.spotify.com/track/5Q6Xzp25aXYxNJ4B6vBkcf?si=c243ad9542dd4e24"
    },
    "Flirty menace": {
        "title": "Everybody Here Wants You",
        "artist": "Jeff Buckley",
        "url": "https://open.spotify.com/track/2bcvooA6HEmVUneEGJnNZD?si=f1baec9e69594840"
    },
    "Ghosting with grace": {
        "title": "Is It Really You?",
        "artist": "Loathe",
        "url": "https://open.spotify.com/track/4OmlsAT8r4q9vPFBvfYgyZ?si=98e3bd60cce54884"
    },
    "Loyalty is my villain origin": {
        "title": "Telephones - Audiotree Live Version",
        "artist": "Vacations, Audiotree",
        "url": "https://open.spotify.com/track/36kemoDk9mPpgnYClja9hW?si=1b590463099840a6"
    },
    "Secret Vibe : Ro": {
        "title": "Mind Over Matter (Reprise)",
        "artist": "Young The Giant",
        "url": "https://open.spotify.com/track/77KnJc8o5G1eKVwX5ywMeZ?si=293bae97a22a476c"
    },
    "Secret Vibe: Salamuffin": {
        "title": "Nothing's Gonna Hurt You Baby",
        "artist": "Cigarretts After 6",
        "url": "https://open.spotify.com/track/3W7KHojYGgYaoX9ogKO9hU?si=8334e9b391b946f5"
    },
    "Secret Vibe: Alaa Cinnabon": {
        "title": "Rd Elzyara",
        "artist": "Abdul Kareem Abdul Qader",
        "url": "https://open.spotify.com/track/50tfYdcdadgLLgcF3WgmXY?si=9acf8450921845f1"
    }
}

# Secret triggers
SECRET_TRIGGERS = {
    "stranger things!": ("Secret Vibe : Ro", "🫂 *This part wasn’t supposed to be found. But I hoped you would. You’re my safe chaos. Thanks for letting me be me💓. ah btw u r stuck with me otherwise I'd have to lock u up fr u know waayy too much🙄*"),
    "smooth operator": ("Secret Vibe: Salamuffin", "🎷 *Yo Stiles! mom keeps asking me when u coming btw. I Love Yoouuu & ur family, and thanks for bringing out the best in me 💌 u literally adopted me since day one like ur cat even tho i was so mean😀 i just love how chaotic we are. u r the Carlos to my Charles🥰*"),
    "cr7": ("Secret Vibe: Alaa Cinnabon", "😎 *u were born a leader. u keep droping iconic lines casually then keep talking like nothing happenes, and i got 'em all written down. u look sharp but u r the softest soul ever💕. ever the cinnabon lover, our smartie💋. p.s. i added ur fav childhood song. 👀*")
}

secret_videos = {
    "Secret Vibe : Ro": "ro.mp4",
    "Secret Vibe: Salamuffin": "salamuffin.mp4",
    "Secret Vibe: Alaa Cinnabon": "alaa.mp4"
}


# Unsplash
UNSPLASH_ACCESS_KEY = "k0m0Vih89ebe8tHJphoaZrJZGWstGqH1B1TJMm_wHWo"

def get_f1_fact(vibe):
    try:
        with open("f1_quotes_updated.json", "r") as file:
            facts = json.load(file)
            return facts.get(vibe, "Max Verstappen did something insane. Again. 💨")
    except:
        return "F1 is chaos, and so are u.😍"

def get_unsplash_image(vibe):
    try:
        res = requests.get(f"https://api.unsplash.com/photos/random?query={vibe}%20aesthetic&client_id={UNSPLASH_ACCESS_KEY}&orientation=landscape")
        return res.json()["urls"]["regular"]
    except:
        return "https://images.unsplash.com/photo-1503264116251-35a269479413"

def media_block(vibe):
    if vibe in secret_videos:
        st.video(secret_videos[vibe])
    else:
        st.image(get_unsplash_image(vibe), use_column_width=True)

def get_spotify_song(vibe):
    song = vibe_playlists.get(vibe)
    if song:
        return song["title"], song["artist"], song["url"]
    return "Silence", "Unknown", "https://open.spotify.com"

# UI
st.set_page_config("VibeMatch", layout="centered")
st.title("🌌 VibeMatch: Your Mood, Curated")
st.markdown("_Made by Shudz – bringing in coded feels._")

regular_vibes = [v for v in vibe_playlists if not v.startswith("Secret")]  # hide secrets
vibe_choice = st.selectbox("Choose your vibe:", regular_vibes + ["✨ Type your own vibe"])

# Determine final vibe
if vibe_choice == "✨ Type your own vibe":
    user_input = st.text_input("Type what you're feeling…").strip().lower()
    final_vibe, secret_msg = SECRET_TRIGGERS.get(user_input, ("Soft but strong", ""))
    if secret_msg:
        st.success(secret_msg)
else:
    final_vibe = vibe_choice

with st.spinner("Summoning your vibe pack…"):
    song = vibe_playlists[final_vibe]
    fact = get_f1_fact(final_vibe)

st.subheader("🎵 Song Recommendation")
st.markdown(f"**{song['title']}** by *{song['artist']}*  \n👉 [Listen]({song['url']})")

st.subheader("🏎️ F1 Vibe Check")
st.markdown(f"_{fact}_")

st.subheader("🎬 Mood Visual")
media_block(final_vibe)

st.markdown("---")
st.markdown("✨ *Share the vibe. Save the mood.*")
