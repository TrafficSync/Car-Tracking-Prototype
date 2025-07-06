from ultralytics import YOLO
import cv2

# Load model dan video
model = YOLO('best.pt')
video_path = 'wasd.mp4'
cap = cv2.VideoCapture(video_path)

# Inisialisasi counter
left_count = 0
right_count = 0
object_id = 0
prev_ids_left = set()
prev_ids_right = set()

# Toleransi sentuhan garis
line_touch_tolerance = 5

# Tracking posisi objek
prev_centers = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, stream=True)

    # Ukuran frame
    frame_height, frame_width = frame.shape[:2]

    # === Posisi garis kiri dan kanan ===
    line_y_left = int(frame_height * 0.73)   # Garis kiri di 73% tinggi layar
    line_y_right = int(frame_height * 0.6)   # Garis kanan di 60% tinggi layar

    # Garis kiri (hijau)
    line_x1 = 0
    line_x2 = frame_width // 2 - 50

    # Garis kanan (merah)
    line_x3 = frame_width // 2 + 50
    line_x4 = frame_width

    # Gambar garis kiri dan kanan
    cv2.line(frame, (line_x1, line_y_left), (line_x2, line_y_left), (0, 255, 0), 2)
    cv2.line(frame, (line_x3, line_y_right), (line_x4, line_y_right), (0, 0, 255), 2)

    new_centers = {}

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            if cls_id == 0:  # Class 'cars'
                # Gambar bounding box dan titik merah
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)

                # Simple tracking ID
                matched_id = None
                for pid, (pcx, pcy) in prev_centers.items():
                    if abs(cx - pcx) < 50 and abs(cy - pcy) < 50:
                        matched_id = pid
                        break

                if matched_id is None:
                    matched_id = object_id
                    object_id += 1

                new_centers[matched_id] = (cx, cy)

                # Hitung sentuhan garis kiri (0.78)
                if (abs(cy - line_y_left) <= line_touch_tolerance and
                    line_x1 <= cx <= line_x2 and
                    matched_id not in prev_ids_left):
                    left_count += 1
                    prev_ids_left.add(matched_id)
                    print(f"[LEFT] ID {matched_id} → Left Count: {left_count}")

                # Hitung sentuhan garis kanan (0.6)
                if (abs(cy - line_y_right) <= line_touch_tolerance and
                    line_x3 <= cx <= line_x4 and
                    matched_id not in prev_ids_right):
                    right_count += 1
                    prev_ids_right.add(matched_id)
                    print(f"[RIGHT] ID {matched_id} → Right Count: {right_count}")

    prev_centers = new_centers

    # Tampilkan counter di kiri atas
    cv2.putText(frame, f'Left Count : {left_count}', (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Right Count: {right_count}', (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Tampilkan frame
    cv2.imshow('TrafficSync - Dual Line Different Y', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
