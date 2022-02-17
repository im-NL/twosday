from PIL import Image
import imagehash
import cv2
import os 

def check_if_palindrome(string):
    reverse_string = string[::-1]

    if reverse_string == string:
        return "This is a palindrome!"
    else:
        return "This is not a palindrome :("

special_date = "22022022"
# print(check_if_palindrome(special_date))

def check_if_ambigram(image):
    reversed_image = image.rotate(180)  # makes PIL object of the image rotated 180 degrees
    hash0 = imagehash.average_hash(image) # makes a hash 
    hash1 = imagehash.average_hash(reversed_image)
    cutoff = 10

    if hash0 - hash1 < cutoff:
        print("This image is an ambigram!")
    else:
        print("This image is not an ambigram :(")

image = Image.open("twosday.jpeg")  # image of the date as a PIL object 
# check_if_ambigram(image)


def check_if_ambigram_using_cv2(image):
    method = cv2.TM_SQDIFF_NORMED
    image.save("image.jpeg")
    image.rotate(180).save("reversed_image.jpeg")

    image = cv2.imread("image.jpeg")
    reversed_image = cv2.imread("reversed_image.jpeg")


    result = cv2.matchTemplate(image, reversed_image, method)
    max_val = cv2.minMaxLoc(result)[1]
    threshold = 5

    if max_val < threshold:
        print("The image is an ambigram!")
    else:
        print("The image is not an ambigram")

    os.remove("image.jpeg")
    os.remove("reversed_image.jpeg")

# check_if_ambigram_using_cv2(image)