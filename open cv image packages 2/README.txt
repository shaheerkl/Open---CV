OPEN CV IMAGE PACKAGES 2

Contains 30 separate image files for OpenCV practice, focused on hot-air balloons, windmills, bicycles, ships, boats, lighthouses, and related sea/coastal scenes.

These files are crops from a generated photorealistic contact-sheet preview, not independently downloaded original photographs. They are ready to load with OpenCV for basic image reading, resizing, display, cropping, and color conversion exercises.

Example:
import cv2
img = cv2.imread('01_hot_air_balloon.jpg')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
