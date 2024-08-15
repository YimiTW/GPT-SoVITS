import requests
from pydub import AudioSegment
from pydub.playback import play
import io

llm_response = '誰是他媽的tales'

r = requests.get(f'http://127.0.0.1:9880?refer_wav_path=/home/yimi/Downloads/test sovit 1-2 使用無參考文本時建議使用微調的GPT.m4a&prompt_text=使用無參考文本時建議使用微調的GPTNone&prompt_language=zh&text={llm_response}&text_language=zh')
audio = AudioSegment.from_file(io.BytesIO(r.content), format="wav")
play(audio)