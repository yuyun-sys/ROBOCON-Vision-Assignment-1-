from ultralytics import YOLO

if __name__ == "__main__":
    # 建议继续从官方预训练权重开始，防止被上一轮不完美的模型带偏
    model = YOLO(r"yolo11s-seg.pt")  
    
    model.train(
        data=r"/home/hu/桌面/train/test.yaml", # 指向新的数据集 yaml
        epochs=200,
        imgsz=640, 
        batch=8,          
        device=0,
        cache="ram",     
        workers=4,        
        project="/home/hu/桌面/runs", 
        name="square_seg_v2_s",
    )
