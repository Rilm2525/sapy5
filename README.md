# sapy5
Makes it easy to use sapi from Python.<br>
<br>
# Install
pip install git+https://github.com/Rilm2525/sapy5<br>
<br>
# Features
・Support text2speech.<br>
・Support export wave.<br>
・Support get pcm bytestream.<br>
・Support get wave file stream.<br>
<br>
# How to (Speak)
import sapy5<br>
<br>
sapi = sapy5.core()<br>
sapi.speak("This is a test message")<br>
<br>
# How to (Export wave file)
from sapy5 import core, audio_formats<br>
<br>
sapi = core(audio_format=audio_formats.pcm_48kHz16BitStereo)<br>
sapi.export_wave("This is a test message", "test_msg.wav", "wb")<br>
