import React, { useState } from 'react';
import { Upload, Button, message, Card, Row, Col, List } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import ReactECharts from 'echarts-for-react';
import './App.css';

const { Dragger } = Upload;

function App() {
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState(null);
  
  const uploadProps = {
    name: 'file',
    multiple: true,
    action: 'http://localhost:8000/evaluate',
    onChange(info) {
      const { status } = info.file;
      if (status === 'uploading') {
        setLoading(true);
      }
      if (status === 'done') {
        setLoading(false);
        setReport(info.file.response);
        message.success(`${info.file.name} 上传成功`);
      } else if (status === 'error') {
        setLoading(false);
        message.error(`${info.file.name} 上传失败`);
      }
    },
  };

  const getRadarOption = () => {
    if (!report) return {};
    
    return {
      radar: {
        indicator: Object.keys(report.scores).map(key => ({
          name: key,
          max: 1
        })),
        radius: '65%'
      },
      series: [{
        type: 'radar',
        data: [{
          value: Object.values(report.scores),
          name: '能力评估',
          areaStyle: {
            color: 'rgba(64, 158, 255, 0.2)'
          }
        }]
      }]
    };
  };

  return (
    <div className="App">
      <Row gutter={16} style={{ marginTop: '20px' }}>
        <Col span={12}>
          <Card title="上传面试材料" loading={loading}>
            <Dragger {...uploadProps}>
              <p className="ant-upload-drag-icon">
                <UploadOutlined />
              </p>
              <p className="ant-upload-text">点击或拖拽上传面试视频和音频</p>
              <p className="ant-upload-hint">
                支持上传MP4视频和WAV音频文件
              </p>
            </Dragger>
            
            <Button 
              type="primary" 
              block 
              style={{ marginTop: '20px' }}
              onClick={() => message.info('请先上传面试材料')}
            >
              开始评测
            </Button>
          </Card>
        </Col>
        
        <Col span={12}>
          <Card title="评测结果" loading={loading}>
            {report ? (
              <>
                <ReactECharts option={getRadarOption()} style={{ height: 400 }} />
                
                <List
                  header={<div>反馈建议</div>}
                  bordered
                  dataSource={report.feedback}
                  renderItem={item => <List.Item>{item}</List.Item>}
                />
              </>
            ) : (
              <div style={{ textAlign: 'center', padding: '50px 0' }}>
                <p>请上传面试材料获取评测结果</p>
              </div>
            )}
          </Card>
        </Col>
      </Row>
    </div>
  );
}

export default App;