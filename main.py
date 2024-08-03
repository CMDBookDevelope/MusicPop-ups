import librosa
import json
import os
import random

def analyze_beats(audio_path):
    y, sr = librosa.load(audio_path)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beats, sr=sr)
    
    # Using onset detection to find the accents (emphasis points) in the music
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onsets = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr, units='time')
    
    return onsets

def generate_script(audio_path, output_script_path):
    onsets = analyze_beats(audio_path)
    
    # Convert onsets to a JSON-compatible string
    onsets_str = json.dumps(onsets.tolist())
    audio_file = os.path.basename(audio_path)

    # List of messages for popups
    messages = [
        "小心女人", "小心台阶", "久~住~", "您", "你线黄了",
        "你线蓝了", "你线白了", "你死了", "菜", "多练", "咕咕咕！"
    ]

    script_content = f"""
import sounddevice as sd
import librosa
import tkinter as tk
import time
import json
import os
import random

class AudioPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.windows = []

    def show_error_popup(self):
        top = tk.Toplevel(self.root)
        top.title("Warning")

        # Randomly select a message from the list
        messages = [
            "小心女人", "小心台阶", "久~住~", "您", "你线黄了",
            "你线蓝了", "你线白了", "你死了", "菜", "多练", "咕咕咕！"
        ]
        message = random.choice(messages)
        
        # 20% chance to add an image
        if random.random() < 0.2:
            try:
                img = tk.PhotoImage(file="image.png")
                img_label = tk.Label(top, image=img)
                img_label.image = img  # Keep a reference to prevent garbage collection
                img_label.pack()
            except Exception as e:
                print("Error loading image:", e)
        
        msg = tk.Label(top, text=message, font=('Helvetica', 16))
        msg.pack(padx=50, pady=50)  # Increase padding for better visibility
        self.windows.append(top)
        
        # Set random position within the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 300
        window_height = 200
        x = random.randint(0, screen_width - window_width)
        y = random.randint(0, screen_height - window_height)
        top.geometry(f"{{window_width}}x{{window_height}}+{{x}}+{{y}}")
        
        self.root.update()  # Ensure the window is shown and updated

    def close_all_popups(self):
        for win in self.windows:
            win.destroy()
        self.windows.clear()

    def play_audio_with_popups(self, audio_path, onsets):
        print("Loading audio file from:", audio_path)
        try:
            y, sr = librosa.load(audio_path)
        except Exception as e:
            print("Error loading audio file:", e)
            return

        start_time = time.time()
        print("Playing audio...")
        sd.play(y, sr)
        
        onset_index = 0
        while onset_index < len(onsets):
            current_time = time.time() - start_time
            if current_time >= onsets[onset_index]:
                self.show_error_popup()
                onset_index += 1
            time.sleep(0.01)
        
        sd.wait()
        print("Audio playback finished.")
        self.close_all_popups()

def play_audio_with_popups():
    audio_path = os.path.join(os.path.dirname(__file__), "{audio_file}")
    onsets = json.loads('{onsets_str}')
    
    player = AudioPlayer()
    player.play_audio_with_popups(audio_path, onsets)

play_audio_with_popups()
"""
    # Save the script with UTF-8 encoding
    with open(output_script_path, 'w', encoding='utf-8') as file:
        file.write(script_content)

def main(audio_path):
    script_path = 'generated_script.py'
    generate_script(audio_path, script_path)

audio_path = 'audio.mp3'  # 替换为你的 MP3 文件路径
main(audio_path)
