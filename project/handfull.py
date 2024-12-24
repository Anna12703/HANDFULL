import cv2
import mediapipe as mp
import pyttsx3

# 初始化 Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 初始化語音引擎
engine = pyttsx3.init()

# 定義手指升直與彎曲判斷函數
def count_fingers(hand_landmarks, hand_label):
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [3, 6, 10, 14, 18]
    count = 0
    straight_fingers = []
    
    # 大拇指判斷
    if hand_label == 'Right':
        thumb_tip = hand_landmarks.landmark[4].x
        thumb_base = hand_landmarks.landmark[3].x
        if thumb_tip < thumb_base:
            count += 1
            straight_fingers.append('Thumb')
    else:
        thumb_tip = hand_landmarks.landmark[4].x
        thumb_base = hand_landmarks.landmark[3].x
        if thumb_tip > thumb_base:
            count += 1
            straight_fingers.append('Thumb')
    
    # 其他手指判斷
    for tip, pip in zip(finger_tips[1:], finger_pips[1:]):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            count += 1
            straight_fingers.append(f'Finger_{tip}')
    
    # 判斷特定手勢數字
    if set(straight_fingers) == {'Thumb', 'Finger_8'}:
        return 7
    if set(straight_fingers) == {'Thumb', 'Finger_8', 'Finger_12'}:
        return 8
    if set(straight_fingers) == {'Thumb', 'Finger_8', 'Finger_12', 'Finger_16'}:
        return 9
    if set(straight_fingers) == {'Thumb', 'Finger_20'}:
        return 6
    if set(straight_fingers) == {'Finger_12', 'Finger_16', 'Finger_20'}:
        return 'OK'
    
    return count

# 啟動視訊捕捉
cap = cv2.VideoCapture(0)

previous_number = ""

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    hand_counts = []
    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[idx].classification[0].label
            finger_count = count_fingers(hand_landmarks, hand_label)
            hand_counts.append((hand_label, finger_count))
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    if len(hand_counts) == 2:
        hand_counts.sort(key=lambda x: x[0])  # 確保左手在前
        left_hand = hand_counts[0][1]
        right_hand = hand_counts[1][1]
        number = f"{left_hand}{right_hand}"
        cv2.putText(frame, number, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        if number != previous_number:
            engine.say(number)
            engine.runAndWait()
            previous_number = number
    elif len(hand_counts) == 1:
        single_hand = hand_counts[0][1]
        number = f"{single_hand}"
        cv2.putText(frame, number, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        if number != previous_number:
            engine.say(number)
            engine.runAndWait()
            previous_number = number
    
    cv2.imshow('Hand Number Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
