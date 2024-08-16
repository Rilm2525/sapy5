# sapy5
Easily use SAPI (Speech Application Programming Interface) from Python.<br>
<br>

# 機能
・入力されたテキストを読み上げる (ディスクアクセス無し)<br>
・入力されたテキストを元にPCMバイト列に出力 (ディスクアクセス無し)<br>
・入力されたテキストを元にio.BytesIOのWAVファイルストリームに出力 (ディスクアクセス無し)<br>
・入力されたテキストを元にWAVファイルに出力<br>
<br>

# インストール方法 (gitのインストールが必要)
```sh
pip install git+https://github.com/Rilm2525/sapy5
```
<br>

# Text2Speechの基本
```Python
from sapy5 import Sapy5, AudioFormat

# Sapy5クラスを初期化 (audio_formatを指定しなかった場合はデフォルト値のpcm_44khz_16bit_stereoになります)
sapi = Sapy5(audio_format=AudioFormat.pcm_48khz_16bit_stereo)

# ボイスの検索(nameを指定しなかった場合は存在するすべてのボイスを返します)
voices = sapi.get_voices(name='Haruka')

# ボイスの指定 (指定しなかった場合はデフォルトのボイスが使用されます) 以下の例では検索結果のDictから一番目の要素をセットしています
sapi.set_voice(next(iter(voices.values())))

# 読み上げる
sapi.speak('これはテキストを読み上げるサンプルです')

# PCMバイト列に出力
pcm_frames = sapi.get_audio_frames('これはPCMバイト列に出力するサンプルです')

# io.BytesIOのWAVファイルストリームに出力
wav_stream = sapi.get_audio_frames('これはio.BytesIOのWAVファイルストリームに出力するサンプルです')

# WAVファイルに出力
sapi.export_wave('これはWAVファイルに出力するサンプルです', './output.wav', 'wb')
```
