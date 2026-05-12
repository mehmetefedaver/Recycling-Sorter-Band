from ultralytics import YOLO

# Kanka modelin tam yolunu buraya yazdım
model = YOLO(r"C:\Users\efek9\Downloads\best.pt")

# OpenVINO formatına çevir komutu
print("Çevirme işlemi başladı kanka, biraz bekle...")
model.export(format='openvino')
print("Hayırlı olsun, OpenVINO klasörün oluşturuldu!")