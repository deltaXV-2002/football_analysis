from ultralytics import YOLO

model = YOLO('yolov8x') #loading the YOLO model

#results variable is going to have the results of the detection in it i.e the output video
results = model.predict('input_videos/8fd33_4.mp4', save=True)
print(results[0])
print('**********************************************')
for box in results[0].boxes:
  print(box)