from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch


# Use the model
resultea= model.train(data="conf.yaml", epochs=1)  # train the model
