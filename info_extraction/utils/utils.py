import numpy as np
import cv2
import pytesseract
from pytesseract import Output
import re
from sklearn.neighbors import KDTree

def remove_special_chars(text):
    ret = ''
    as_list = list(text)
    special_chars = '():[]|'
    for i in as_list:
        if i not in special_chars:
            ret += i
    return ret

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
        text = remove_special_chars(d['text'][i])
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

def vary_locs(indep_idx, locs):
    new_locs = locs + 0.01 * np.random.randn(2)
    move_indep_locs = np.random.randn(2 * len(indep_idx)).reshape(-1, 2) * (0.02, 0.01)
    new_locs[indep_idx] += move_indep_locs
    return new_locs

def make_new_locs(locs, indep_idx, size=200):
    new_locs = np.zeros((size, ) + locs.shape)
    for i in range(size):
        new_locs[i] = vary_locs(indep_idx, locs)
    return new_locs

def get_relative_positions(loc, locs):
    return locs - loc

def neighbors(loc, words, locs, num=20):
    # Given a location, get all words and relative locations in a window around the location
    x, y = loc
    a = locs[:, 0] > 0
    b = locs[:, 0] < 1
    c = locs[:, 1] > y - 0.1
    d = locs[:, 1] < y + 0.1
    e = (locs != (x, y)).any(1)
    idx = np.where(a & b & c & d & e)[0]
    w = words[idx]
    l = get_relative_positions(loc, locs[idx])
    diff = num - len(idx)
    if diff > 0:
        w = np.concatenate((w, np.zeros((diff))), 0)
        l = np.concatenate((l, np.zeros((diff, 2))), 0)
    elif diff < 0:
        i = np.random.choice(range(len(idx)), size=num, replace=False)
        w = w[i]
        l = l[i]

    return w, l

def get_neighbor_idx(loc, words, locs, num=20):
    tree = KDTree(locs)
    _, idx = tree.query(loc.reshape(1, -1), num)
    idx = idx[:, 1:]
    return idx

def get_neighbors(loc, words, locs, num=20):
    idx = get_neighbor_idx(loc, words, locs, num+1)
    w = words[idx]
    l = get_relative_positions(loc, locs[idx])
    return w, l

def get_dates(words, locs):
    date_words = []
    date_locs = []
    for idx, word in enumerate(words):
        res = re.findall(r'\d+\/\d+\/\d+', word)
        if res:
            date_words.append(word)
            date_locs.append(locs[idx])
    return np.array(date_words, dtype=object), np.array(date_locs)

def get_names(words, locs):
    name_words = []
    name_locs = []
    for idx, word in enumerate(words):
        res = re.findall(r'[A-Za-z]+', word)
        if res and len(res) == 1 and len(res[0]) == len(word):
            name_words.append(word)
            name_locs.append(locs[idx])
    return np.array(name_words, dtype=object), np.array(name_locs)

def get_phone_numbers(words, locs):
    cand_words = []
    cand_locs = []
    for idx, word in enumerate(words):
        res = re.findall(r'/(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?/g', word)
        if res and len(res) == 1 and len(res[0]) == len(word):
            cand_words.append(word)
            cand_locs.append(locs[idx])
    return np.array(cand_words, dtype=object), np.array(cand_locs)

def get_id_numbers(words, locs):
    cand_words = []
    cand_locs = []
    for idx, word in enumerate(words):
        res = re.findall(r'\d+', word)
        if res and len(res) == 1 and len(res[0]) == len(word):
            cand_words.append(word)
            cand_locs.append(locs[idx])
    return (np.array(cand_words, dtype=object), np.array(cand_locs))

def get_emails(words, locs):
    cand_words = []
    cand_locs = []
    for idx, word in enumerate(words):
        res = re.findall(r'\S+@\S+', word)
        if res and len(res) == 1 and len(res[0]) == len(word):
            cand_words.append(word)
            cand_locs.append(locs[idx])
    return (np.array(cand_words, dtype=object), np.array(cand_locs))

def get_candidates(words, locs):
    date_words, date_locs = get_dates(words, locs)
    name_words, name_locs = get_names(words, locs)
    phone_words, phone_locs = get_phone_numbers(words, locs)
    id_words, id_locs = get_id_numbers(words, locs)
    email_words, email_locs = get_emails(words, locs)
    
    return date_words, date_locs, name_words, name_locs, phone_words, phone_locs, id_words, id_locs, email_words, email_locs