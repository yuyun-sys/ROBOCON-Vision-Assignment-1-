from ultralytics import YOLO

model = YOLO(r"/home/hu/桌面/branches2/best_seg.pt")  # load a pretrained model (recommended for training)   
model.predict(
    source=r"/home/hu/桌面/train/images/train/0117.png",
    save=True,
    show=False, 
)
