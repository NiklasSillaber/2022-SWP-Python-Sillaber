import cv2
import mediapipe as mp


class HandGestureLib():
    
    def __init__(self):
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        
        self.hands = self.mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5)
        
        self.gestureCounterLeft = 8
        self.gestureCounterRight = 8
        self.gestureBeforeLeft = None
        self.gestureBeforeRight = None
    
        
    def findHands(self, img, draw=True):
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        img.flags.writeable = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        self.results = self.hands.process(img)
        
        # Draw the hand annotations on the image.
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if(draw):
                    self.mp_drawing.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style())
        
        return img

    def getStructuredLandmarks(self, landmarks):
        global structuredLandmarks
        structuredLandmarks = []
        for j in range ( 42 ):
            if (j % 2 == 1):
                structuredLandmarks.append ( {'x': landmarks[j - 1] , 'y': landmarks[j]} )
        return structuredLandmarks
    
    def recognizeHandGesture(self, image, landmarks, handType, confidence = 10):
        
        fingers = [False, False, False, False, False] #[thumb, index, middle, ring, little]
        thumbUp = False
        recognizedHandGesture = None
    
        #Thumb
        if handType == 'Left':
            pseudoFixKeyPoint = landmarks[2]['x']
            if landmarks[3]['y'] < landmarks[5]['y'] and landmarks[3]['y'] < landmarks[9]['y'] and landmarks[3]['y'] < landmarks[9]['y'] and landmarks[3]['y'] < landmarks[17]['y'] and landmarks[1]['x'] < landmarks[10]['x']:
                thumbUp = True
                cv2.circle(image, (landmarks[4]['x'], landmarks[4]['y']), 10, (0, 0, 255), cv2.FILLED)
            elif pseudoFixKeyPoint < landmarks[3]['x'] < landmarks[4]['x']:
                fingers[0] = True
                cv2.circle(image, (landmarks[4]['x'], landmarks[4]['y']), 10, (255, 0, 255), cv2.FILLED)
        else:
            pseudoFixKeyPoint = landmarks[2]['x']
            if landmarks[3]['y'] < landmarks[5]['y'] and landmarks[3]['y'] < landmarks[9]['y'] and landmarks[3]['y'] < landmarks[9]['y'] and landmarks[3]['y'] < landmarks[17]['y'] and landmarks[1]['x'] > landmarks[10]['x']:
                thumbUp = True
                cv2.circle(image, (landmarks[4]['x'], landmarks[4]['y']), 10, (0, 0, 255), cv2.FILLED)
            elif pseudoFixKeyPoint > landmarks[3]['x'] > landmarks[4]['x']:
                fingers[0] = True
                cv2.circle(image, (landmarks[4]['x'], landmarks[4]['y']), 10, (255, 0, 255), cv2.FILLED)
    	
        #Index
        pseudoFixKeyPoint = landmarks[6]['y']
        if pseudoFixKeyPoint > landmarks[7]['y'] > landmarks[8]['y']:
            #indexFingerState = 'OPEN'
            fingers[1] = True
            cv2.circle(image, (landmarks[8]['x'], landmarks[8]['y']), 10, (255, 0, 255), cv2.FILLED)

        #Middle
        pseudoFixKeyPoint = landmarks[10]['y']
        if pseudoFixKeyPoint > landmarks[11]['y'] > landmarks[12]['y']:
            #middleFingerState = 'OPEN'
            fingers[2] = True
            cv2.circle(image, (landmarks[12]['x'], landmarks[12]['y']), 10, (255, 0, 255), cv2.FILLED)

        #Ring
        pseudoFixKeyPoint = landmarks[14]['y']
        if pseudoFixKeyPoint > landmarks[15]['y'] > landmarks[16]['y']:
            #ringFingerState = 'OPEN'
            fingers[3] = True
            cv2.circle(image, (landmarks[16]['x'], landmarks[16]['y']), 10, (255, 0, 255), cv2.FILLED)

        #Little
        pseudoFixKeyPoint = landmarks[18]['y']
        if pseudoFixKeyPoint > landmarks[19]['y'] > landmarks[20]['y']:
            #littleFingerState = 'OPEN'
            fingers[4] = True
            cv2.circle(image, (landmarks[20]['x'], landmarks[20]['y']), 10, (255, 0, 255), cv2.FILLED)
            
        count = sum(fingers)
        
        #general
        if count == 5: recognizedHandGesture = 'PAPIER'
        elif count == 2: recognizedHandGesture = 2
        elif count == 3: recognizedHandGesture = 3
        elif count == 4: recognizedHandGesture = 'EXIT'
        elif count == 0: recognizedHandGesture = 'STEIN'
        
        #specific
        if recognizedHandGesture == 2 and fingers[1] and fingers[2]: recognizedHandGesture = 'SCHERE'
        elif recognizedHandGesture == 3 and fingers[0] and fingers[1] and fingers[4]: recognizedHandGesture = 'ECHSE'
        if thumbUp: recognizedHandGesture = 'SPOCK'
            
        if handType == 'Left': 
            if recognizedHandGesture == self.gestureBeforeLeft:
                self.gestureCounterLeft -= 1
                self.gestureBeforeLeft = recognizedHandGesture
                if self.gestureCounterLeft < 0:
                    self.gestureCounterLeft = confidence
                    return recognizedHandGesture
                else: return None
            else: 
                self.gestureBeforeLeft = recognizedHandGesture
                self.gestureCounterLeft = confidence
                return None
            
        else: 
            if recognizedHandGesture == self.gestureBeforeRight:
                self.gestureCounterRight -= 1
                self.gestureBeforeRight = recognizedHandGesture
                if self.gestureCounterRight < 0:
                    self.gestureCounterRight = confidence
                    return recognizedHandGesture
                else: return None
            else: 
                self.gestureBeforeRight = recognizedHandGesture
                self.gestureCounterRight = confidence
                return None
            

    def findGesture(self, img):
        
        if self.results.multi_hand_landmarks:  # schauen ob Hand erkannt wird
            for hand, handedness in zip(self.results.multi_hand_landmarks, self.results.multi_handedness):
                
                handType = handedness.classification[0].label   #Typ der Hand
    
                landmark_data = []
                h, w, c = img.shape  # größe von image holen
                    
                for point in hand.landmark:
                    cx, cy = int(point.x * w), int(point.y * h)  # Koordinaten umrechnen ==> in Pixel
                    landmark_data.append(cx)
                    landmark_data.append(cy)
                    
                if handType == 'Left':
                    recognizedHandGesture = self.recognizeHandGesture(img, self.getStructuredLandmarks(landmark_data), handType)
                    if recognizedHandGesture != None:
                        #print('Left: ',recognizedHandGesture)
                        return recognizedHandGesture
                else:
                    recognizedHandGesture = self.recognizeHandGesture(img, self.getStructuredLandmarks(landmark_data), handType)
                    if recognizedHandGesture != None:
                        #print('Right: ',recognizedHandGesture)
                        return recognizedHandGesture
                    