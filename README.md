# sapy5
Makes it easy to use sapi from Python.<br>
<br>
# Install
```sh
pip install git+https://github.com/Rilm2525/sapy5
```
# Features
・Support text2speech. (No disk access)<br>
・Support export wave.<br>
・Support get pcm bytestream. (No disk access)<br>
・Support get wave file stream. (No disk access)<br>
<br>
# How to (Speak)
```Python
import sapy5

sapi = sapy5.core()
sapi.speak("This is a test message")
```
# How to (Export wave file)
```Python
from sapy5 import core, audio_formats

sapi = core(audio_format=audio_formats.pcm_48kHz16BitStereo)
sapi.export_wave("This is a test message", "test_msg.wav", "wb")
```
