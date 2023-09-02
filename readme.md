# car_detection
## Image_OCR_Text_logic (PyTessaract)

Using PyTessaract and OpenCV to read car's license plate and their speed and then sort them into two (overspeeding/non-overspeeding) from a live video stream in Python.

## Packages used in the Project 
1. opencv-python
2. numpy
3. requests
4. pytesseract
5. datetime
6. time
7. csv
8. pandas
   
## Initial Setup 
### 1. Numpy package 
to convert image byte data to an array 
```
pip install numpy
```
### 2. PyTessaract package
to recognize text from the image
```
pip install pytesseract
```
### 3. OpenCV package
to read an image and perform certain image-processing techniques
```
pip install opencv-python
```
### 4. Requests package
to fetch images from the wifi-camera(URL)
```
pip install requests
```
### 5. DateTime package
for logging the current time when a car is detected
```
pip install DateTime
```
### 6. Time package
to calculate the Speed of the car detected (YOLO)
```
pip install time
```
### 7. Pandas package
for cleaning the CSV file data 
```
pip install pandas
```
### 9. It would require the URL of a wifi-camera (I installed "IP webcam" from Google PlayStore)


> [!IMPORTANT]
> 1. If that didn't work then you can try these [commands](https://pip.pypa.io/en/stable/user_guide/).
> 2. If there is still a problem then you can install through a .whl file for that particular [package](https://www.w3docs.com/snippets/python/how-do-i-install-a-python-package-with-a-whl-file.html). [^1]

## Test Drive 
### Code Run: 
1. start the camera and change the URL in the "license_speed.py" file in the 'AI' directory.
2. Run the file "license_speed.py" in the 'AI' directory.
3. Run the file "clean.py" in the 'AI' directory.
4. check the output in the "vehicle_details.csv" or "filtered_file.csv" in the 'data' directory.

### Website Run:
1. start the camera and change the URL in the "main_web.html" file in the 'website' directory.
2. open website. (run that HTML file)
3. you can change the speed limit of the car. (which is later sorted into two list {overspeeding/non-overspeeding})

> [!NOTE]
> 1. Remember to perform the initial setup before test-driving.
> 2. you have to provide a constant video feed to the camera.
> 3. you can use multimedia to test the code.


[^1]: .whl files are given in the "for_package_installation_error" directory



