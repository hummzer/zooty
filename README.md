# WALES 🐳


`WALES` is a no-nonsense, cold-blooded YouTube butcher bot.  
Give it 30 minute to 1 hour video and it’ll chop it into several shorts like a sushi chef.


### 🤖 What It Does
- Reads YouTube links from `youtubelinks.txt`
- Downloads each video
- Splits each into 10-30 seconds chunks


### 🧠 Requirements
- Python 3.8+
- Kali or any Linux
    - `Virtualenv` activated
- CPU with 8GB RAM (runs on low juice)


### System dependencies (Kali-friendly)
    `Bash `
    ```
    sudo apt update && sudo apt install -y \
        ffmpeg libavcodec-dev libavformat-dev libswscale-dev \
        libavdevice-dev libavutil-dev libavfilter-dev libopenblas-dev \
        libsndfile1 gfortran cmake pkg-config
        ```


### Virtual environment setup(assumming you name it idris)
        `Bash`
        ```
        virtualenv idris

        source idris/bin/activate
        ```

### Python dependencies
        ```
        pip3 install -r requirements.txt
        ```

### Run the bot
        ```
        python3 wales.py -l youtubelinks.txt
        ```
