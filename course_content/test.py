from ultralytics import YOLO

model = YOLO("yolo11s-obb.pt")
model.export(format='onnx')