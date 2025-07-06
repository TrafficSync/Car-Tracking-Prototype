from ultralytics import YOLO

# Load model YOLOv8 (bisa pakai pre-trained atau dari awal)
model = YOLO('yolov8n.pt')  # Ganti dengan 'yolov8s.pt' atau lainnya untuk model lebih besar

# Latih modelmodel.val(data='path/to/data.yaml')
model.train(
    data='D:\!Hackahton\VehicleCount.v1\data.yaml',  # Path ke file data.yaml
    epochs=50,                 # Jumlah iterasi pelatihan
    imgsz=640,                 # Ukuran gambar (640x640 piksel)
    batch=16,                  # Jumlah gambar per batch
    name='custom_yolov8'       # Nama folder hasil pelatihan
)
