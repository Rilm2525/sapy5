# sapy5
Makes it easy to use sapi from Python.

# Features
・Support text2speech.
・Support export wave.
・Support get pcm bytestream.
・Support get wave file stream.

# How to (Speak)
import sapy5
<br>
sapi = sapy5.core()
sapi.speak("This is a test message")

# How to (export wave file)
from sapy5 import core, audio_formats
<br>
sapi = core(audio_format=audio_formats.pcm_48kHz16BitStereo)
sapi.export_wave("This is a test message", "test_msg.wav", "wb")
