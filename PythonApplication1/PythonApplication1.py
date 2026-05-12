import os
import cv2
from ultralytics import YOLO
import serial
import time


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


model_yolu = r"C:\Users\efek9\Downloads\geri_donusum_modeli-20260501T160423Z-3-001\geri_donusum_modeli\weights\best_saved_model\best_float16.tflite"


model = YOLO(model_yolu)


etiketler = {0: 'Cam', 1: 'Metal', 2: 'Kagit', 3: 'Plastik', 4: 'Atik'}

son_komut_zamani = 0
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: 
        print("Kamera okunamadı")
        break

    
    results = model(frame, conf=0.5, task='detect', stream=True, verbose=False)

    for r in results:
        for box in r.boxes:
           
            cls = int(box.cls[0])
            etiket = etiketler.get(cls, "Atik")
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, etiket, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Recycling-Sorter-Band", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
