import time
import pygame
from datetime import datetime
import os

# Initialize pygame mixer
pygame.mixer.init()

# Function to play audio
def play_audio(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Function to log activity
def log_activity(activity):
    with open(f"{activity}.txt", "a") as file:
        file.write(f"{activity} at {datetime.now()}\n")

# Function to handle reminders
def handle_reminder(activity, audio_file, stop_word, next_time, interval):
    current_time = time.time()
    if current_time >= next_time:
        play_audio(audio_file)
        user_input = input(f"Enter '{stop_word}' after completing {activity}: ")
        if user_input == stop_word:
            log_activity(activity)
            next_time = current_time + interval
        else:
            print(f"Invalid input. Please enter '{stop_word}'.")
    return next_time

# Set intervals for each activity in seconds (for quick testing, set to 6 seconds)
water_interval = 6
eye_interval = 6
exercise_interval = 6

# Absolute paths to the audio files
water_audio = os.path.abspath("Python_Codes\\Intermediate\\healthy_programmer\\Please-drink-water.mp3")
eye_audio = os.path.abspath("Python_Codes\\Intermediate\\healthy_programmer\\Please-do-eye-exerci.mp3")
exercise_audio = os.path.abspath("Python_Codes\\Intermediate\\healthy_programmer\\Please-do-some-physi.mp3")

# Check if the files exist
if not all(os.path.exists(path) for path in [water_audio, eye_audio, exercise_audio]):
    print("One or more audio files could not be found. Please check the paths.")
    exit(1)

try:
    start_time = time.time()
    water_next = start_time + water_interval
    eye_next = start_time + eye_interval
    exercise_next = start_time + exercise_interval

    while True:
        water_next = handle_reminder("Drank", water_audio, "Drank", water_next, water_interval)
        eye_next = handle_reminder("EyDone", eye_audio, "EyDone", eye_next, eye_interval)
        exercise_next = handle_reminder("ExDone", exercise_audio, "ExDone", exercise_next, exercise_interval)

        time.sleep(1)
except KeyboardInterrupt:
    print("Program stopped.")
