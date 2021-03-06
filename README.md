# 项目介绍

开发在城市道路环境下，有路口数据提前感知的情况下，开发一个建议车速应用。

---

## 功能目标

- 显示实时车速
- 显示前方车辆车速
- 计算建议车速
- 显示计算好的建议车速
- 输入前方车辆个数
- 显示前方路况信号灯状态
- 能记录并保存数据文件
- 能控制网络连接启停(Socket)
- 能控制数据记录启停

## 目前进展
- √ 界面框架
- √ 数据包接收与解析
- √ 以 Excel 格式保存记录的数据
- √ 显示接收数据
- √ 计算 GLOSA 建议车速
- √ OBU_Core.Node.Publisher
- √ GLOSA_Core.Node.Subscriber

## 当前问题
- 同时进行数据接收，车速计算，界面显示（刷新），数据记录（多线程）
- 配合 ROS 对各部分重写
    - 单一节点，多话题订阅
    - 单一节点，同时订阅、处理完、发布
    - 话题的设置
- Qt.QAction 中 Slot&Signal 

## 未来计划
- ~~多线程化~~
- ROS 化
- 界面美化

## 开发流程剖分
1. 确定功能需求
2. 原型设计
3. UI 设计
4. 开发
    - Socket
    - Serial
    - Resolve
    - GLOSA
    - GUI
    - Record
    - ROS (Publisher & Subscriber)
5. 测试
