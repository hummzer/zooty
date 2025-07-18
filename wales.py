import os
import argparse
import subprocess
import random
import moviepy.editor as mp
import whisper
from tqdm import tqdm
import time

def download_video(urls, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    print("[1/5] Downloading videos:")
    for url in tqdm(urls, desc="Downloading", unit="video"):
        cmd = [
                "yt-dlp",
                "-f", "best[ext=mp4]",
                "-o", f"{output_dir}/%(title).40s.%(ext)s",
                url
                ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("[1/5] Done.")

def is_video_duration_valid(video_path):
    clip = mp.VideoFileClip(video_path)
    duration = clip.duration  # in seconds
    return 1800 <= duration <= 3600  # 30 min to 1 hour

def transcribe_audio(video_path):
    print(f"[2/5] Transcribing audio from: {video_path}")
    model = whisper.load_model("tiny")
    audio_path = video_path.replace(".mp4", ".mp3")
    mp.VideoFileClip(video_path).audio.write_audiofile(audio_path, logger=None)

    result = model.transcribe(audio_path)

    # Simulate progress bar for transcription segments
    segments = result["segments"]
    print("[2/5] Building transcription progress...")
    for _ in tqdm(range(len(segments)), desc="Transcribing", unit="segment"):
        time.sleep(0.01)  # simulate processing
    return segments

def create_shorts(video_path, segments, output_dir="shorts", max_count=10):
    print(f"[3/5] Creating shorts from: {video_path}")
    os.makedirs(output_dir, exist_ok=True)
    video = mp.VideoFileClip(video_path)
    shorts_created = 0
    segment_pool = [seg for seg in segments if seg['end'] - seg['start'] >= 10]
    random.shuffle(segment_pool)

    total = min(max_count, len(segment_pool))
    with tqdm(total=total, desc="Creating Shorts", unit="clip") as pbar:
        for seg in segment_pool:
            if shorts_created >= max_count:
                break
            start = seg["start"]
            duration = min(seg["end"] - start, random.randint(30, 60))
            end = start + duration

            try:
                clip = video.subclip(start, end).resize(height=720)
                out_path = f"{output_dir}/short_{shorts_created+1}.mp4"
                clip.write_videofile(out_path, codec="libx264", audio_codec="aac", threads=1, logger=None)
                shorts_created += 1
                pbar.update(1)
            except Exception as e:
                print(f"Skipping segment due to error: {e}")
    print(f"[4/5] Done. Created {shorts_created} shorts.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--list", required=True, help="Text file with YouTube links (one per line)")
    args = parser.parse_args()

    with open(args.list, "r") as f:
        links = [line.strip() for line in f if line.strip()]

    download_video(links)

    files = [file for file in os.listdir("downloads") if file.endswith(".mp4")]

    for i, file in enumerate(files, start=1):
        path = os.path.join("downloads", file)
        print(f"\nProcessing video {i}/{len(files)}: {file}")
        if is_video_duration_valid(path):
            segments = transcribe_audio(path)
            create_shorts(path, segments)
            print(f"[5/5] Processing completed for: {file}\n")
        else:
            print(f"Skipping '{file}' — Not between 30min and 1hr.")

if __name__ == "__main__":
    main()

