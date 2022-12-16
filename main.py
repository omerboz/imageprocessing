import cv2

# Görüntü dosyasını oku
image = cv2.imread("okul.jpg")

# Yüzleri bulmak için Haar Cascades kullan
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(image, scaleFactor=1.092, minNeighbors=8)

# Eğer yüzler bulunamazsa, mesajı yazdır ve çık
if len(faces) == 0:
    print("No faces found")
    exit()

# Her bir yüz için kare çiz
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.rectangle(image, ((0, image.shape[0] - 35)), (500, image.shape[0]), (255, 255, 255), -1)
    cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0, image.shape[0] - 10),
    cv2.FONT_HERSHEY_DUPLEX, 1, (1, 1, 1), 1)
# Yüzlerin koordinatlarını ve yüzlerin sayısını yazdır
print(f"Found {len(faces)} faces at the following coordinates:")
print(faces)

# Görüntüyü göster
cv2.imshow("Faces", image)
cv2.waitKey(0)

