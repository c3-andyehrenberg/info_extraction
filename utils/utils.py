import numpy as np
import cv2
import pytesseract
from pytesseract import Output

def get_text_and_locations(image, show_locations=False, show_boxes=False):
    img = np.uint8(image)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)

    words = []
    locations = []
    for i in range(len(d['level'])):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        word = d['text'][i]
        if word not in ['', ' ']:
            loc = (x + w // 2, y + h // 2)
            words.append(word)
            locations.append(loc)
            if show_locations:
                cv2.circle(img, loc, 2, (0, 255, 0), thickness=2)
            if show_boxes:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if show_locations or show_boxes:
        return words, locations, img
    return words, locations
