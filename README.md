# 多模态智能面试评测系统

## 项目概述

这是一个面向高校学生的多模态智能面试评测系统，能够模拟真实面试场景，通过语音、文本等多模态数据对学生的面试表现进行智能评测，并给出详细反馈和建议。

## 功能特点

1. **多场景覆盖**：支持人工智能、大数据、物联网等3个技术领域的典型岗位面试场景
2. **多模态分析**：整合语音(语调、情感)、文本(内容、简历)等多维度数据
3. **动态评测体系**：包含5项核心能力指标(专业知识、技能匹配度、表达能力等)
4. **智能反馈**：生成可视化报告(雷达图、问题定位、改进建议)

## 技术栈

- 前端：React + Ant Design + ECharts
- 后端：FastAPI + PyTorch + OpenCV
- 数据库：MongoDB
- 语音处理：SpeechRecognition + Librosa
- NLP：Transformers + Jieba

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 启动后端
uvicorn main:app --reload

# 启动前端
cd frontend && npm start
```