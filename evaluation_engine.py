from typing import Dict
from .audio_analysis import AudioAnalyzer
from .video_analysis import VideoAnalyzer
from .text_analysis import TextAnalyzer

class EvaluationEngine:
    """
    评测引擎
    功能：
    1. 整合多模态分析结果
    2. 计算综合评分
    3. 生成反馈建议
    """
    
    def __init__(self):
        self.audio_analyzer = AudioAnalyzer()
        self.video_analyzer = VideoAnalyzer()
        self.text_analyzer = TextAnalyzer()
    
    def evaluate(self, audio_path: str, video_path: str, resume_text: str, position: str) -> Dict:
        """
        执行多模态评测
        :param audio_path: 音频文件路径
        :param video_path: 视频文件路径
        :param resume_text: 简历文本
        :param position: 岗位类型
        :return: 评测结果
        """
        # 音频分析
        audio_result = self.audio_analyzer.analyze_intonation(audio_path)
        speech_text = self.audio_analyzer.speech_to_text(audio_path)
        
        # 视频分析
        video_result = self.video_analyzer.analyze_facial_expressions(video_path)
        
        # 文本分析
        resume_result = self.text_analyzer.analyze_resume(resume_text, position)
        answer_result = self.text_analyzer.analyze_answer_quality(speech_text)
        
        # 计算综合评分
        scores = self._calculate_scores(
            audio_result, 
            video_result, 
            resume_result, 
            answer_result
        )
        
        # 生成反馈建议
        feedback = self._generate_feedback(
            scores, 
            speech_text, 
            resume_result, 
            answer_result
        )
        
        return {
            "scores": scores,
            "feedback": feedback,
            "audio_analysis": audio_result,
            "video_analysis": video_result,
            "text_analysis": {"resume": resume_result, "answer": answer_result}
        }
    
    def _calculate_scores(self, audio_result, video_result, resume_result, answer_result) -> Dict[str, float]:
        """计算5个核心能力指标评分"""
        return {
            "专业知识": resume_result["match_score"],
            "技能匹配度": resume_result["technical_term_count"] / 10,
            "语言表达": (audio_result["speech_rate"] * 0.3 + answer_result["clarity_score"] * 0.7),
            "逻辑思维": answer_result["logical_score"],
            "应变能力": (video_result["neutral"] * 0.5 + (1 - video_result["angry"]) * 0.5)
        }
    
    def _generate_feedback(self, scores, speech_text, resume_result, answer_result) -> List[str]:
        """生成反馈建议"""
        feedback = []
        
        # 专业知识反馈
        if scores["专业知识"] < 0.6:
            feedback.append(f"专业知识匹配度较低({scores['专业知识']:.2f})，建议加强{resume_result['keywords'][0]}相关知识学习")
        
        # 语言表达反馈
        if not answer_result["star_structure"]:
            feedback.append("回答缺乏STAR结构(情境-任务-行动-结果)，建议使用此结构组织回答")
            
        # 应变能力反馈
        if scores["应变能力"] < 0.5:
            feedback.append("面试中表现出紧张情绪，建议多做模拟面试练习")
            
        return feedback