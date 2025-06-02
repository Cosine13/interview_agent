import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from typing import Dict

class ReportGenerator:
    """
    报告生成模块
    功能：
    1. 生成能力雷达图
    2. 生成文本反馈报告
    """
    
    def generate_radar_chart(self, scores: Dict[str, float]) -> BytesIO:
        """
        生成能力雷达图
        :param scores: 各维度评分
        :return: 图片二进制数据
        """
        categories = list(scores.keys())
        values = list(scores.values())
        
        N = len(categories)
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]
        
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, values, color='skyblue', alpha=0.25)
        ax.plot(angles, values, color='blue', linewidth=2)
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_title("面试能力评估", size=16, y=1.1)
        
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        plt.close()
        
        return img_buffer
    
    def generate_text_report(self, feedback: list, analysis_results: dict) -> str:
        """
        生成文本反馈报告
        :param feedback: 反馈建议列表
        :param analysis_results: 各模块分析结果
        :return: 格式化文本报告
        """
        report = "# 面试评估报告\n\n"
        
        # 添加关键问题
        report += "## 关键问题\n"
        for i, item in enumerate(feedback, 1):
            report += f"{i}. {item}\n"
        
        # 添加详细分析
        report += "\n## 详细分析\n"
        report += f"- **语言表达**: 清晰度得分 {analysis_results['text_analysis']['answer']['clarity_score']:.2f}\n"
        report += f"- **逻辑思维**: 逻辑性得分 {analysis_results['text_analysis']['answer']['logical_score']:.2f}\n"
        report += f"- **情绪表现**: 中性表情占比 {analysis_results['video_analysis']['neutral']:.2f}\n"
        
        # 添加改进建议
        report += "\n## 改进建议\n"
        report += "1. 针对薄弱知识点进行专项学习\n"
        report += "2. 使用STAR结构组织回答\n"
        report += "3. 多做模拟面试练习\n"
        
        return report