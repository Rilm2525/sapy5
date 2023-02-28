# sapy5
It makes it easy to use sapi from Python.


# How to (Speak)
import sapy5

sapi = sapy5.core()
sapi.speak("This is a test message")


# How to (export wave file)
from sapy5 import core, audio_formats

sapi = core(audio_format=audio_formats.pcm_48kHz16BitStereo)
sapi.export_wave("This is a test message", "test_msg.wav", "wb")