import cv2
import cvlib as cv

def count_people(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Perform person detection
    bbox, label, conf = cv.detect_common_objects(image)

    # Count the number of people
    num_people = label.count('person')

    return num_people

# Provide the path to your image
folder = 'images/'
image_name = 'IMG_2295.JPG'
image_path = folder + image_name

# Count the number of people in the image
people_count = count_people(image_path)

print(f"There are {people_count} people in the image.")
