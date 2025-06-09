from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = FastAPI(title="多模态智能面试评测系统")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InterviewRequest(BaseModel):
    position_type: str  # 岗位类型
    resume_text: str    # 简历文本

@app.post("/evaluate")
async def evaluate_interview(
    request: InterviewRequest, # 非默认参数，放在最前面
    audio: UploadFile = File(...),
    video: UploadFile = File(...)
):
    """
    面试评测接口
    :param audio: 面试音频文件
    :param video: 面试视频文件
    :param request: 包含岗位类型和简历文本
    :return: 评测结果
    """
    # 这里将实现多模态分析逻辑
    return {"message": "评测功能待实现"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)