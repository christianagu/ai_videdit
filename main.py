import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

import librosa
import librosa.display
import subprocess

def extract_frames(video_path, output_dir, fps=1):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if count % (frame_rate // fps) == 0:
            filename = os.path.join(output_dir, f"frame_{count}.jpg")
            cv2.imwrite(filename, frame)
        count += 1
    cap.release()

def extract_spectrogram(audio_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    count = 0

    for root, _, files in os.walk(audio_dir):
        for audio_file in files:
            full_path = os.path.join(root, audio_file)
            print(f"Loading: {full_path}")
            y, sr = librosa.load(full_path, sr=None)

            # Create mel-spectrogram
            S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
            S_db = librosa.power_to_db(S, ref=np.max)

            # Save as image
            plt.figure(figsize=(12, 6))
            librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel')
            plt.colorbar(format='%+2.0f dB')
            plt.title(f'Spectrogram: {audio_file}')
            plt.tight_layout()

            out_path = os.path.join(output_dir, f"spectrogram_{count:03d}.png")
            plt.savefig(out_path)
            plt.close()
            count += 1

def run_shell(audio_input_dir):
    for root, _, files in os.walk(audio_input_dir):
        return_code = 1
        if files == []:
            return_code = subprocess.call("extract_wav.sh", shell=True)
        
        if return_code != 0:
            print(f"Error running script, return code: {return_code}")
        else:
            print("Script executed successfully")

# === Main ===
video_path = "data/video.mp4"
frames_output_dir = "extracted_data/frames"
audio_input_dir = "C:/Users/xuts/Desktop/dev/ai_videdit/audio_wav"
spectrogram_output_dir = "extracted_data/spectrograms"

run_shell(audio_input_dir)
extract_spectrogram(audio_input_dir, spectrogram_output_dir)
extract_frames(video_path, frames_output_dir)