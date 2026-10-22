IMAGES 2 — OpenCV Practice Pack
================================

This folder contains 20 sample images with descriptive filenames for beginner OpenCV practice.
The images are generated illustrations, not downloaded photographs. They are suitable for learning
image loading, display, resizing, cropping, color conversion, thresholding, blurring, edge detection,
contours, shape detection, and basic color segmentation.

Image guide
-----------
01_street_scene.jpg       Street scene: roads, buildings, sky
02_red_car.jpg            Car: vehicle shape and wheels
03_fruits.jpg             Fruits: different colors and overlapping objects
04_buildings.jpg          Buildings: windows and straight edges
05_flower.jpg              Flower: petals, center and stem
06_geometric_shapes.jpg   Shapes: rectangle, circle, triangle and line
07_coins.jpg              Coins: circular objects and contrast
08_checkerboard.jpg       Checkerboard: patterns and corner detection
09_color_gradient.jpg     Color gradient: color channels and intensity
10_document.jpg           Document: page boundaries and line detection
11_face_illustration.jpg  Face illustration: face-detection concepts (illustration, not a real face)
12_mountains.jpg          Landscape: segmentation and edge detection
13_water_surface.jpg      Water: texture and horizontal patterns
14_night_city.jpg         Night city: contrast and low-light enhancement
15_open_book.jpg          Book: page boundaries and text-like lines
16_coffee_cup.jpg         Cup: circles and object boundaries
17_bicycle.jpg            Bicycle: line and circle detection
18_dog_illustration.jpg   Dog illustration: object shape practice (not a real photo)
19_traffic_light.jpg      Traffic light: color segmentation
20_license_plate.jpg      Sample plate: text-region detection and OCR practice

Quick start
-----------
import cv2 as cv

img = cv.imread(r"C:\path\to\images 2\01_street_scene.jpg")
if img is not None:
    cv.imshow("Street scene", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Check the path and filename.")

Tip: use raw strings (r"...") for Windows paths, or forward slashes.
For Jupyter notebooks, matplotlib is often more convenient for displaying images inline.
