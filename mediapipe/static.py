import cv2
import mediapipe

drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

with handsModule.Hands(static_image_mode=True) as hands:
    image = cv2.imread(r"C:\Users\Xylon\OneDrive\Desktop\SLR\mediapipe\open.jpg")

    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    imageHeight, imageWidth, _ = image.shape

    if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:
            drawingModule.draw_landmarks(image, handLandmarks, handsModule.HAND_CONNECTIONS)

            for point in handsModule.HandLandmark:
                normalizedLandmark = handLandmarks.landmark[point]
                pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                          normalizedLandmark.y,
                                                                                          imageWidth, imageHeight)

                print(point)
                print(pixelCoordinatesLandmark)
                print(normalizedLandmark)

    cv2.imshow('Test image', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
