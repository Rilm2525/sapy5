import win32com.client
from io import BytesIO
import wave

class AudioFormat:
    pcm_8khz_8bit_mono = {'sapi_format_type': 4, 'sampling_rate': 8000, 'sample_width_bit': 8, 'channels': 1}
    pcm_8khz_8bit_stereo = {'sapi_format_type': 5, 'sampling_rate': 8000, 'sample_width_bit': 8, 'channels': 2}
    pcm_8khz_16bit_mono = {'sapi_format_type': 6, 'sampling_rate': 8000, 'sample_width_bit': 16, 'channels': 1}
    pcm_8khz_16bit_stereo = {'sapi_format_type': 7, 'sampling_rate': 8000, 'sample_width_bit': 16, 'channels': 2}
    pcm_11khz_8bit_mono = {'sapi_format_type': 8, 'sampling_rate': 11000, 'sample_width_bit': 8, 'channels': 1}
    pcm_11khz_8bit_stereo = {'sapi_format_type': 9, 'sampling_rate': 11000, 'sample_width_bit': 8, 'channels': 2}
    pcm_11khz_16bit_mono = {'sapi_format_type': 10, 'sampling_rate': 11000, 'sample_width_bit': 16, 'channels': 1}
    pcm_11khz_16bit_stereo = {'sapi_format_type': 11, 'sampling_rate': 11000, 'sample_width_bit': 16, 'channels': 2}
    pcm_12khz_8bit_mono = {'sapi_format_type': 12, 'sampling_rate': 12000, 'sample_width_bit': 8, 'channels': 1}
    pcm_12khz_8bit_stereo = {'sapi_format_type': 13, 'sampling_rate': 12000, 'sample_width_bit': 8, 'channels': 2}
    pcm_12khz_16bit_mono = {'sapi_format_type': 14, 'sampling_rate': 12000, 'sample_width_bit': 16, 'channels': 1}
    pcm_12khz_16bit_stereo = {'sapi_format_type': 15, 'sampling_rate': 12000, 'sample_width_bit': 16, 'channels': 2}
    pcm_16khz_8bit_mono = {'sapi_format_type': 16, 'sampling_rate': 16000, 'sample_width_bit': 8, 'channels': 1}
    pcm_16khz_8bit_stereo = {'sapi_format_type': 17, 'sampling_rate': 16000, 'sample_width_bit': 8, 'channels': 2}
    pcm_16khz_16bit_mono = {'sapi_format_type': 18, 'sampling_rate': 16000, 'sample_width_bit': 16, 'channels': 1}
    pcm_16khz_16bit_stereo = {'sapi_format_type': 19, 'sampling_rate': 16000, 'sample_width_bit': 16, 'channels': 2}
    pcm_22khz_8bit_mono = {'sapi_format_type': 20, 'sampling_rate': 22000, 'sample_width_bit': 8, 'channels': 1}
    pcm_22khz_8bit_stereo = {'sapi_format_type': 21, 'sampling_rate': 22000, 'sample_width_bit': 8, 'channels': 2}
    pcm_22khz_16bit_mono = {'sapi_format_type': 22, 'sampling_rate': 22000, 'sample_width_bit': 16, 'channels': 1}
    pcm_22khz_16bit_stereo = {'sapi_format_type': 23, 'sampling_rate': 22000, 'sample_width_bit': 16, 'channels': 2}
    pcm_24khz_8bit_mono = {'sapi_format_type': 24, 'sampling_rate': 24000, 'sample_width_bit': 8, 'channels': 1}
    pcm_24khz_8bit_stereo = {'sapi_format_type': 25, 'sampling_rate': 24000, 'sample_width_bit': 8, 'channels': 2}
    pcm_24khz_16bit_mono = {'sapi_format_type': 26, 'sampling_rate': 24000, 'sample_width_bit': 16, 'channels': 1}
    pcm_24khz_16bit_stereo = {'sapi_format_type': 27, 'sampling_rate': 24000, 'sample_width_bit': 16, 'channels': 2}
    pcm_32khz_8bit_mono = {'sapi_format_type': 28, 'sampling_rate': 32000, 'sample_width_bit': 8, 'channels': 1}
    pcm_32khz_8bit_stereo = {'sapi_format_type': 29, 'sampling_rate': 32000, 'sample_width_bit': 8, 'channels': 2}
    pcm_32khz_16bit_mono = {'sapi_format_type': 30, 'sampling_rate': 32000, 'sample_width_bit': 16, 'channels': 1}
    pcm_32khz_16bit_stereo = {'sapi_format_type': 31, 'sampling_rate': 32000, 'sample_width_bit': 16, 'channels': 2}
    pcm_44khz_8bit_mono = {'sapi_format_type': 32, 'sampling_rate': 44000, 'sample_width_bit': 8, 'channels': 1}
    pcm_44khz_8bit_stereo = {'sapi_format_type': 33, 'sampling_rate': 44000, 'sample_width_bit': 8, 'channels': 2}
    pcm_44khz_16bit_mono = {'sapi_format_type': 34, 'sampling_rate': 44000, 'sample_width_bit': 16, 'channels': 1}
    pcm_44khz_16bit_stereo = {'sapi_format_type': 35, 'sampling_rate': 44000, 'sample_width_bit': 16, 'channels': 2}
    pcm_48khz_8bit_mono = {'sapi_format_type': 36, 'sampling_rate': 48000, 'sample_width_bit': 8, 'channels': 1}
    pcm_48khz_8bit_stereo = {'sapi_format_type': 37, 'sampling_rate': 48000, 'sample_width_bit': 8, 'channels': 2}
    pcm_48khz_16bit_mono = {'sapi_format_type': 38, 'sampling_rate': 48000, 'sample_width_bit': 16, 'channels': 1}
    pcm_48khz_16bit_stereo = {'sapi_format_type': 39, 'sampling_rate': 48000, 'sample_width_bit': 16, 'channels': 2}

    ''' Idk how to add support for these formats. sry :(
    #TrueSpeech format
    SAFTTrueSpeech_8kHz1BitMono = 40

    #A-Law formats
    SAFTCCITT_ALaw_8kHzMono = 41
    SAFTCCITT_ALaw_8kHzStereo = 42
    SAFTCCITT_ALaw_11kHzMono = 43
    SAFTCCITT_ALaw_11kHzStereo = 4
    SAFTCCITT_ALaw_22kHzMono = 44
    SAFTCCITT_ALaw_22kHzStereo = 45
    SAFTCCITT_ALaw_44kHzMono = 46
    SAFTCCITT_ALaw_44kHzStereo = 47

    #u-Law formats
    SAFTCCITT_uLaw_8kHzMono = 48
    SAFTCCITT_uLaw_8kHzStereo = 49
    SAFTCCITT_uLaw_11kHzMono = 50
    SAFTCCITT_uLaw_11kHzStereo = 51
    SAFTCCITT_uLaw_22kHzMono = 52
    SAFTCCITT_uLaw_22kHzStereo = 53
    SAFTCCITT_uLaw_44kHzMono = 54
    SAFTCCITT_uLaw_44kHzStereo = 55
    SAFTADPCM_8kHzMono = 56
    SAFTADPCM_8kHzStereo = 57
    SAFTADPCM_11kHzMono = 58
    SAFTADPCM_11kHzStereo = 59
    SAFTADPCM_22kHzMono = 60
    SAFTADPCM_22kHzStereo = 61
    SAFTADPCM_44kHzMono = 62
    SAFTADPCM_44kHzStereo = 63

    #GSM 6.10 formats
    SAFTGSM610_8kHzMono = 64
    SAFTGSM610_11kHzMono = 65
    SAFTGSM610_22kHzMono = 66
    SAFTGSM610_44kHzMono = 67

    #Other formats
    SAFTNUM_FORMATS = 68
    '''
    
class Sapy5:
    def __init__(self, audio_format:AudioFormat=AudioFormat.pcm_44khz_16bit_stereo) -> None:
        self.__audio_format = audio_format
        self.__voice = None
    
    def set_audio_format(self, audio_format:AudioFormat) -> None:
        self.__audio_format = audio_format
    
    def get_voices(self, name:str=None) -> dict:
        sapi = win32com.client.Dispatch('SAPI.SpVoice')
        voices = {voice.GetDescription(): voice for voice in sapi.GetVoices()}
        if name:
            voices = {v_name: voice for v_name, voice in voices.items() if name.lower() in v_name.lower()}
        del sapi
        return voices
    
    def set_voice(self, voice) -> None:
        self.__voice = voice

    def speak(self, text:str) -> bytes:
        sapi = win32com.client.Dispatch('SAPI.SpVoice')
        if self.__voice:
            sapi.Voice = self.__voice
        sapi.Speak(text)
        del sapi

    def get_audio_frames(self, text:str) -> bytes:
        sapi = win32com.client.Dispatch('SAPI.SpVoice')
        mem_stream = win32com.client.Dispatch('SAPI.SpMemoryStream')
        mem_stream.Format.Type = self.__audio_format['sapi_format_type']
        sapi.AudioOutputStream = mem_stream
        if self.__voice:
            sapi.Voice = self.__voice
        sapi.Speak(text)
        data = mem_stream.GetData().tobytes()
        del sapi, mem_stream
        return data

    def get_wave_filestream(self, text:str) -> BytesIO:
        data = self.get_audio_frames(text)
        fs = BytesIO()
        file = wave.open(fs, 'wb')
        file.setnchannels(self.__audio_format['channels'])
        file.setsampwidth(self.__audio_format['sample_width_bit'] // 8)
        file.setframerate(self.__audio_format['sampling_rate'])
        file.writeframes(data)
        file.close()
        del data, file
        fs.seek(0)
        return fs

    def export_wave(self, text:str, wave_path:str, wave_mode:str='wb') -> None:
        data = self.get_audio_frames(text)
        file = wave.open(wave_path, wave_mode)
        file.setnchannels(self.__audio_format['channels'])
        file.setsampwidth(self.__audio_format['sample_width_bit'] // 8)
        file.setframerate(self.__audio_format['sampling_rate'])
        file.writeframes(data)
        file.close()
        del data, file
