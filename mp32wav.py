from pydub import AudioSegment
sound = AudioSegment.from_mp3("mo.mp3")
sound.export("mo.wav",format="wav")
