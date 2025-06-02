import librosa
import numpy as np
import speech_recognition as sr
from typing import Tuple, Dict

class AudioAnalyzer:
    """
    音频分析模块
    功能：
    1. 语音转文字
    2. 语调分析
    3. 情感分析
    """
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def speech_to_text(self, audio_path: str) -> str:
        """
        将语音转换为文字
        :param audio_path: 音频文件路径
        :return: 转换后的文本
        """
        with sr.AudioFile(audio_path) as source:
            audio_data = self.recognizer.record(source)
            try:
                text = self.recognizer.recognize_google(audio_data, language='zh-CN')
                return text
            except Exception as e:
                print(f"语音识别错误: {e}")
                return ""
    
    def analyze_intonation(self, audio_path: str) -> Dict[str, float]:
        """
        分析语调特征
        :param audio_path: 音频文件路径
        :return: 包含语调特征的字典
        """
        y, sr = librosa.load(audio_path)
        
        # 提取MFCC特征
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        
        # 提取音高特征
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        pitch_mean = np.mean(pitches[pitches > 0])
        
        return {
            "mfcc_mean": float(np.mean(mfcc)),
            "pitch_mean": float(pitch_mean),
            "speech_rate": len(self.speech_to_text(audio_path).split()) / (len(y) / sr)
        }