# WALES.PY 🐳

Wales.py is a no-nonsense, cold-blooded YouTube butcher bot.  
Give it a 3hr video and it’ll chop it into 24 shorts like a sushi chef.

## 🤖 What It Does
- Reads YouTube links from `youtubelinks.txt`
- Downloads each video
- Splits each into 8-min chunks
- Adds suspense captions + music + background
- Drops all videos into `shorts/` for your channel

## 🧠 Requirements
- Python 3.8+
- Kali or any Linux
- Virtualenv activated
- CPU with 8GB RAM (runs on low juice)

# System dependencies (Kali-friendly)
sudo apt update && sudo apt install -y \
  ffmpeg libavcodec-dev libavformat-dev libswscale-dev \
  libavdevice-dev libavutil-dev libavfilter-dev libopenblas-dev \
  libsndfile1 gfortran cmake pkg-config

# Virtual environment setup(assumming you name it idris)
cd ~/Desktop/scripts/youtube
virtualenv idris
source idris/bin/activate

# Python dependencies
pip3 install -r requirements.txt

# 3. Run the bot
python3 wales.py -l youtubelinks.txt
