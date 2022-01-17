import numpy as np
import cv2
import pytesseract
from pytesseract import Output

def get_words(image, show_locations=False, show_boxes=False):
    # Get all words and the centers of their bounding boxes
    width, height = [float(n) for n in image.size]
    img = np.uint8(image)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)

    words = np.empty((len(d['level'])), dtype=object)
    locs = np.zeros((len(d['level']), 2))
    for i in range(len(d['level'])):
        (x, y, w, h) = (
            d['left'][i] / width, 
            d['top'][i] / height, 
            d['width'][i] / width, 
            d['height'][i] / height,
        )
        text = d['text'][i]
        if text not in ['', ' ']:
            loc = (x + w / 2, y + h / 2)
            locs[i] = loc
            words[i] = text
            if show_locations:
                cv2.circle(img, (int(loc[0] * width), int(loc[1] * height)), 2, (0, 255, 0), thickness=2)
            if show_boxes:
                cv2.rectangle(img, (int(x * width), int(y * height)), (int((x + w) * width), int((y + h) * height)), (0, 255, 0), 2)
    if show_locations or show_boxes:
        return words[words != None], locs[locs != (0, 0)].reshape(-1, 2), img
    return words[words != None], locs[locs != (0, 0)].reshape(-1, 2)

def get_neighbors(loc, words, locs):
    # Given a location, get all words and locations in a window around the location
    x, y = loc
    a = locs[:, 0] > 0
    b = locs[:, 0] < 1
    c = locs[:, 1] > y - 0.1
    d = locs[:, 1] < y + 0.1
    e = (locs != (x, y)).any(1)
    idx = np.where(a & b & c & d & e)[0]
    neighbors = (words[idx], locs[idx])
    return neighbors
