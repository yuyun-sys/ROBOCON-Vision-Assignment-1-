```
# Assignment 3 - YOLO

## 1. 任务说明

选择目标：队里那个上红下蓝的方块

## 2. 数据集

数据集名称：dataset_branch2

数据集来源：用realsense相机拍的

包含哪些类别：top_blue top_red side_upper_blue_lower_blue side_upper_red_lower_blue

## 3. 模型训练

使用的 YOLO 版本：8.4.173

使用的预训练模型：yolo26n.pt  yolo 11s-seg.pt

训练命令：mytrain.py已发送至src

主要训练参数：         epochs=200,
                 imgsz=640, 
                 batch=-1, 
                  #-1自动找最合适的数
                 cache="ram",
                 workers=4,

## 4. 模型测试

测试使用的命令：newpredict.py已发送至src
               
检测结果：

result.jpg已上传

## 5. 对 YOLO 的理解

1. YOLO 是用来做什么的？
通过深度学习让机器可以识别图片所包含的特定信息
2. 什么是 Bounding Box？
YOLO用框框住物体表示其成功识别出来这个的类别
3. 什么是 Confidence？
置信度，高于阈值则认为该物体是目标物体，反之则抛弃
4. Training 和 Predict 有什么区别？
Training是通过yolo和已经标注的数据库训练模型，而Predict是通过模型识别并标注物体
5. 训练得到的 .pt 文件是什么？
核心是权重参数，用于预测的最主要部分，相当于模型形成的“直觉”，还记录了类别，权重参数等信息

```
