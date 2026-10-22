OPEN CV IMAGES — REAL PHOTOGRAPHS

This package downloads 20 real photos from Unsplash: cars, streets, landscapes,
forest, beach, waterfall, flowers, animals, bicycle, buildings, bridge, food,
fruit, portrait, sunset, mountains and a road landscape.

The photos themselves are not bundled because this environment could not access
the image host. Run the script on your computer with internet access to download
the JPGs into this folder.

Steps:
1. Extract the ZIP.
2. Open the folder in PyCharm.
3. Open PyCharm Terminal and run: python -m pip install requests
4. Run: python download_real_images.py

Example after the photos download:
    import cv2 as cv
    img = cv.imread(r"open cv images\01_car_sports.jpg")
    if img is not None:
        cv.imshow("Car", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Image not found; check the filename and path.")

Source: Unsplash. Check the Unsplash License and any applicable third-party rights
before using photographs outside personal learning.
