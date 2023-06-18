import json
import sounddevice as sd
import soundfile as sf
import numpy as np
import openai
import time
from flask import Flask, request, jsonify, session

app = Flask(__name__)

openai.api_key = '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'

# Initialize an empty array to store the recorded audio
recording = np.array([])

def audio_callback(indata, frames, time, status):
    global recording
    recording = np.append(recording, indata)

def record_audio():
    sample_rate = 16000
    recording_duration = 15
    silence_threshold = 3

    stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate)
    print('talk now!')
    stream.start()

    start_time = time.time()
    while True:
        if input("Press any key to stop recording: , and say 'quit' to quit"):
            break
        if len(recording) >= sample_rate * recording_duration:
            break

    end_time = time.time()
    print(end_time - start_time)

    stream.stop()
    stream.close()

    sf.write("user_recording.wav", recording, sample_rate)

def convert_speech_to_text(audio_file):
    with open(audio_file, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)

    return transcript

language = ["English", "Russian", "Spanish", "Italian", "Africaans", "Albanian"]
topic = ["ordering at a restaurant", "ordering at a supermarket", "doctor's appointment"]
conversation = [
    {"role": "system", "content": f"You are a helpful assistant that speaks {language[0]}. "
                                 f"You will be roleplaying the topic of {topic[0]} for the user's learning purposes. "
                                 "Play along."},
]
i = 0
while True:
    if i != 0:
        record_audio()
        user_input = convert_speech_to_text("user_recording.wav").text
    else:
        user_input = '\n'
        i += 1
    if user_input.strip().lower() == 'quit.':
        break
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation,
    )
    assistant_reply = response["choices"][0]["message"]["content"]
    print("Assistant:", assistant_reply)
    conversation.append({"role": "assistant", "content": assistant_reply})
    time.sleep(5)  # Delay for 5 seconds

app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/process', methods=['POST'])
def process_data():
    # Retrieve data from the front-end
    data = request.json

    # Get the previous data from the session, or an empty list if it doesn't exist
    previous_data = session.get('previous_data', [])

    # Perform logic using both current and previous data
    processed_data = perform_logic(data, previous_data)

    # Update the previous data with the current data
    previous_data.append(data)

    # Store the updated previous data in the session
    session['previous_data'] = previous_data

    # Prepare the response
    response = {'result': processed_data}

    # Send the response back to the front-end
    return jsonify(response)

def perform_logic(current_data, previous_data):
    # Perform your logic using both current and previous data here
    
    result = previous_data + [current_data]
    return result

# if __name__ == '__main__':
#     app.run()

