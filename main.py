import os
import whisper                              ## Documentation https://github.com/openai/whisper            
from audio_extract import extract_audio     ## Documentation https://pypi.org/project/audio-extract/
from alive_progress import alive_bar        ## Documentation https://github.com/rsalmei/alive-progress
import time

MODEL = "large-v3"                          ## Possible Options https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages    
LANGUAGE = "pt"

def writeTimeStampFrom(start: str, end: str) -> list[str]:
    start: int = int(start)
    end  : int = int(end)
    
    hours  : list[int]  = [start // 3600, end // 3600] 
    minutes: list[int]  = [start % 3600 // 60, end % 3600 // 60]
    seconds: list[int]  = [start % 60, end % 60]

    return [
        f"{hours[0]:02}:{minutes[0]:02}:{seconds[0]:02}",
        f"{hours[1]:02}:{minutes[1]:02}:{seconds[1]:02}",
    ]

def main():

    ## Define input and output folders
    path_videos: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Video")
    path_audios: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Audio")
    path_text  : str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Text")

    print(f"Video folder: {path_videos}")
    print(f"Audio folder: {path_audios}")
    print(f"Text folder: {path_text}")
    print()

    ## Ensure the output folders exist
    if not os.path.exists(path_audios):
        os.makedirs(path_audios)

    if not os.path.exists(path_text):
        os.makedirs(path_text)

    ## Extract audio from video files
    list_of_videos: list[str] = os.listdir(path_videos)
    with alive_bar(len(list_of_videos)) as bar:
        for index, video_file in enumerate(list_of_videos):
            print(f"Extracting audios from {path_videos} to {path_audios}")
            if video_file.endswith(".mp4"):
                input_path: str = os.path.join(path_videos, video_file)
                output_path: str = os.path.join(path_audios, video_file.rsplit('.', 1)[0] + ".mp3")

                if not os.path.exists(output_path):
                    extract_audio(input_path=input_path, output_path=output_path)
                    print(f"Audio {video_file}: extracted")
            bar()

    print()

    ## Load model
    model: whisper = whisper.load_model(MODEL)
    
    print()
    
    ## Transcribe each mp3 file in the Audio folder
    list_of_audios: list[str] = os.listdir(path_audios)
    with alive_bar(len(list_of_videos)) as bar:
        for index, audio_file in enumerate(list_of_audios):
            print(f"Extracting text from {path_audios} to {path_text}")
            if audio_file.endswith(".mp3"):
                audio_path: str = os.path.join(path_audios, audio_file)
                print(f"Loading audio {audio_path}")
                
                ## Load audio and pad/trim it to fit 30 seconds
                audio = whisper.load_audio(audio_path)
                
                ## Decode the audio
                print(f"Decoding {audio_path}")
                
                options: dict = {
                    "language": LANGUAGE,
                    "task": "transcribe"
                }

                result: dict= whisper.transcribe(model, audio, **options)
                
                ## Write result to formatted txt
                text_path = os.path.join(path_text, audio_file).replace(".mp3", f"_{MODEL}.txt")
                print(f"Saving on {text_path}")
                with open(text_path, "w", encoding="utf-8") as file:
                    for segments in result['segments']:
                        timestamps: list[str] = writeTimeStampFrom(segments['start'], segments['end'])
                        file.write(f"{timestamps[0]} --> {timestamps[1]}\n{segments['text']}\n")
            os.remove(audio_path)
            bar()
                    
if __name__ == "__main__":
    main()