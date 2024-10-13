

# Download and extract transcript 

YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=cdiD-9MMpb0"

import os
import tempfile
import whisper
# from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Let's do this only if we haven't created the transcription file yet.
if not os.path.exists("transcription.txt"):
    youtube = YouTube(YOUTUBE_VIDEO, on_progress_callback = on_progress)
    audio = youtube.streams.filter(only_audio=True).first()

    # Let's load the base model. This is not the most accurate
    # model but it's fast.
    whisper_model = whisper.load_model("base")

    with tempfile.TemporaryDirectory() as tmpdir:
        # tmpdir="c:"
        # print(tmpdir)
        
        file = audio.download(output_path=tmpdir)
        
        print('here********************************************', file)
        result = whisper_model.transcribe(file)
        print(result)
        transcription = whisper_model.transcribe(file, fp16=False, verbose=True)["text"].strip()

        print('here2********************************************')
        with open("transcription.txt", "w") as file:
            file.write(transcription)
        print('here3********************************************')








print("done")