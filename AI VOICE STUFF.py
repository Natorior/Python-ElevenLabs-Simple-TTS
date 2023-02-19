from elevenlabslib import *
import pydub
import pydub.playback
import io
def play(bytesData):
    sound = pydub.AudioSegment.from_file_using_temporary_files(io.BytesIO(bytesData))
    pydub.playback.play(sound)
    return
      
user = ElevenLabsUser(API_KEY) #fill in your api key as a string
voice = user.get_voices_by_name(VOICE_NAME)[0]  #fill in the name of the voice you want to use. ex: "Rachel"
play(voice.generate_audio_bytes(WORDS)) #fill in what you want the ai to say as a string