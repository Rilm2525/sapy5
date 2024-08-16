# sapy5
Easily use SAPI (Speech Application Programming Interface) from Python.<br>
<br>

# Features
・Speak the input text (without disk access)<br>
・Output PCM byte sequence from the input text (without disk access)<br>
・Output a WAV file stream in io.BytesIO from the input text (without disk access)<br>
・Output a WAV file from the input text<br>
<br>

# Installation (requires git)
```sh
pip install git+https://github.com/Rilm2525/sapy5
```
<br>

# Basic Text-to-Speech Usage
```Python
from sapy5 import Sapy5, AudioFormat

# Initialize the Sapy5 class (default audio_format is pcm_44khz_16bit_stereo if not specified)
sapi = Sapy5(audio_format=AudioFormat.pcm_48khz_16bit_stereo)

# Search for voices (returns all available voices if name is not specified)
voices = sapi.get_voices(name='Zira')

# Set the voice (if not specified, the default voice is used). In this example, we set the first element from the search result Dict.
sapi.set_voice(next(iter(voices.values())))

# Speak the text
sapi.speak('This is a sample text-to-speech output.')

# Output as PCM byte sequence
pcm_frames = sapi.get_audio_frames('This is a sample output as PCM byte sequence.')

# Output as io.BytesIO WAV file stream
wav_stream = sapi.get_audio_frames('This is a sample output as a WAV file stream in io.BytesIO.')

# Output as a WAV file
sapi.export_wave('This is a sample output as a WAV file.', './output.wav', 'wb')
```
