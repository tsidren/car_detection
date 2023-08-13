import cv2
import numpy as np
import requests
import pytesseract
import datetime
import time
import csv

# Set the URL for image retrieval
url = "http://162.16.3.73:8080/shot.jpg"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize the list for license plate recognition results
license_plate_results = []

# Initialize the list for storing vehicle details
vehicle_details = []



# Function to perform license plate recognition
def recognize_license_plate(image):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    canny = cv2.Canny(gray, 30, 200)

    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    plate = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)

        if len(approx) == 4:
            plate = approx
            break

    if plate is not None:
        x, y, w, h = cv2.boundingRect(plate)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        license_plate = gray[y:y + h, x:x + w]
        license_plate = cv2.bitwise_not(license_plate)

        license_plate = pytesseract.image_to_string(license_plate, config='--psm 7')
        license_plate = "".join([c if c.isalnum() else "" for c in license_plate]).strip()

        license_plate_results.append(license_plate)


# Function to calculate average speed
def calculate_speed(start_time, end_time, distance):
    time_diff = end_time - start_time
    speed = distance / time_diff
    return speed

# Initialize variables for speed detection-
start_time = time.time()
previous_frame = None
distance = 10  # Specify the distance between two detection points in the video

# Open the CSV file for writing
csv_file = open("../data/vehicle_details.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Timestamp", "License Plate", "Average Speed"])

# Loop through the video frames
while True:
    # Fetch the image from the URL
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)

    # Check if the frame is valid
    if frame is None:
        break

    # Perform license plate recognition
    recognize_license_plate(frame)
    re_frame = cv2.resize(frame, (640, 480))
    # Display the license plate recognition result
    cv2.imshow('License Plate Recognition', re_frame)

    # Calculate speed if there's a previous frame
    if previous_frame is not None:
        current_time = datetime.datetime.now()
        curr = time.time()
        speed = calculate_speed(start_time, curr, distance)

        # Append the vehicle details to the list
        if license_plate_results:
            vehicle_details.append((str(current_time), license_plate_results[-1], speed))

    # Update the previous frame and start time
    previous_frame = re_frame
    start_time = time.time()

    # Check for key press
    key = cv2.waitKey(1)
        if key == ord('q'):
        break

# Write the vehicle details to the CSV file
for detail in vehicle_details:
    csv_writer.writerow(detail)

# Close the CSV file
csv_file.close()

# Print the license plate recognition results
for i, result in enumerate(license_plate_results):
    print(f"License Plate {i + 1}: {result}")

# Release the video capture and destroy windows
cv2.destroyAllWindows()
