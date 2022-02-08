from PIL import Image
import numpy as np

from collections import Counter
import warnings

from .utils import get_neighbors, get_neighbor_idx, get_words
from .locs import (
    make_d1v1p1,
    make_d1v1p2,
    make_d1v1p3,
    make_d1v2p1,
    make_d1v2p2,
    make_d2v1p1,
    make_d2v1p2,
    make_d2v2p1,
    make_d2v2p2
)

dd31v1p1 = Image.open('images/dd31v1p1.png')
dd31v1p2 = Image.open('images/dd31v1p2.png')
dd31v1p3 = Image.open('images/dd31v1p3.png')
dd31v2p1 = Image.open('images/dd31v2p1.png')
dd31v2p2 = Image.open('images/dd31v2p2.png')
dd31v2p3 = Image.open('images/dd31v2p3.png')
dd31v3p1 = Image.open('images/dd31v3p1.png').resize((2200, 1700))
dd31v3p2 = Image.open('images/dd31v3p2.png').resize((2200, 1700))
dd32v1p1 = Image.open('images/dd32v1p1.png')
dd32v1p2 = Image.open('images/dd32v1p2.png')
dd32v2p1 = Image.open('images/dd32v2p1.png')
dd32v2p2 = Image.open('images/dd32v2p2.png')
dd32v3p1 = Image.open('images/dd32v3p1.png').resize((2200, 1700))
dd32v3p2 = Image.open('images/dd32v3p2.png').resize((2200, 1700))

def is_number(word):
    return word.replace('.','').replace(',','').isdecimal()

def is_date(word):
    if len(word) in [7, 8] and word[2] == '/':
        return True
    else:
        return False

class VocabularyBuilder():
    """Vocabulary builder class to generate vocabulary."""
    
    def __init__(self, all_words, max_size = 512):
        self._words_counter = Counter()
        self.max_size = max_size
        self._vocabulary = { '<PAD>':0, '<NUMBER>':1, '<RARE>':2 }
        self.built = False
        self.all_words = all_words
        
    def add(self, word):
        if word in self.all_words and not is_number(word) and not is_date(word):
            self._words_counter.update([word.lower()])
            
    def build(self):
        for word, count in self._words_counter.most_common(self.max_size):
            self._vocabulary[word] = len(self._vocabulary)
        self.built = True
        return self._vocabulary

    def get_vocab(self):
        if not self.built:
            warnings.warn(
                "The vocabulary is not built. Use VocabularyBuilder.build(). Returning default vocabulary.", Warning)
            return self._vocabulary
        else:
            return self._vocabulary

def negative_samples(idx, text, locs, near_size=2, far_size=2):
    wrong_nearby_idx = set(np.random.choice(get_neighbor_idx(locs[idx], text, locs, num=20)[0], size=near_size))
    wrong_maybe_far_idx = set(np.random.randint(len(text), size=far_size))
    wrong_idx = set.union(wrong_nearby_idx, wrong_maybe_far_idx)
    if idx in wrong_idx:
        wrong_idx.remove(idx)
    while len(wrong_idx) < near_size + far_size:
        candidate = np.random.randint(len(text))
        if candidate != idx:
            wrong_idx.add(candidate)
    wrong_idx = np.int32(list(wrong_idx))
    wrong_text = text[wrong_idx]
    wrong_loc = locs[wrong_idx]
    return wrong_text, wrong_loc

def make_data_single_image(fields, text, locs, near_size=2, far_size=1, num_neighbors=20):
    n = len(fields) * (near_size + far_size + 1)
    field = np.empty((n, 1), dtype=object)
    candidate_pos = np.zeros((n, 2), dtype=np.float32)
    neighbor_text = np.empty((n, num_neighbors), dtype=object)
    neighbor_pos = np.zeros((n, num_neighbors, 2), dtype=np.float32)
    label = np.zeros((n, 1), dtype=np.uint8)
    counter = 0
    for i in range(len(fields)):
        correct_loc = locs[i:i+1]
        _, wrong_loc = negative_samples(i, text, locs, near_size, far_size)
        all_locs = np.concatenate((correct_loc, wrong_loc), 0)
        for idx, loc in enumerate(all_locs):
            nt, npos = get_neighbors(loc, text, locs, num_neighbors)
            l = np.array([int(idx == 0)])
            field[counter] = fields[i]
            candidate_pos[counter] = loc
            neighbor_text[counter] = nt
            neighbor_pos[counter] = npos
            label[counter] = l
            counter += 1
    return field, candidate_pos, neighbor_text, neighbor_pos, label

def make_data_page(boilerplate_words, boilerplate_locs, fn, n=20, near_size=2, far_size=1):
    field, candidate_pos, neighbor_text, neighbor_pos, label = [], [], [], [], []
    for i in range(n):
        locs, text, fields = fn()
        texts = np.concatenate((text, boilerplate_words), 0)
        locs = np.concatenate((locs, boilerplate_locs), 0)
        f, cp, nt, npos, l = make_data_single_image(fields, texts, locs, near_size, far_size)
        field.append(f)
        candidate_pos.append(cp)
        neighbor_text.append(nt)
        neighbor_pos.append(npos)
        label.append(l)
    field = np.concatenate(field, 0)
    candidate_pos = np.concatenate(candidate_pos, 0)
    neighbor_text = np.concatenate(neighbor_text, 0)
    neighbor_pos = np.concatenate(neighbor_pos, 0)
    label = np.concatenate(label, 0)
    return field, candidate_pos, neighbor_text, neighbor_pos, label

def make_data(near_size=2, far_size=1, it_per_page=50):
    boilerplate = [
        get_words(dd31v1p1), get_words(dd31v1p2), get_words(dd31v1p3), 
        get_words(dd31v2p1), get_words(dd31v2p2), get_words(dd31v2p3), 
        get_words(dd31v3p1), get_words(dd31v3p2),
        get_words(dd32v1p1), get_words(dd32v1p2), 
        get_words(dd32v2p1), get_words(dd32v2p2),
        get_words(dd32v3p1), get_words(dd32v3p2)
    ]
    fns = [
        make_d1v1p1, make_d1v1p2, make_d1v1p3, 
        make_d1v1p1, make_d1v1p2, make_d1v1p3,
        make_d1v2p1, make_d1v2p2,
        make_d2v1p1, make_d2v1p2, 
        make_d2v1p1, make_d2v1p2, 
        make_d2v2p1, make_d2v2p2
    ]
    field, candidate_pos, neighbor_text, neighbor_pos, label = [], [], [], [], []
    all_words = []
    for pair, fn in zip(boilerplate, fns):
        text_boilerplate, locs_boilerplate = pair
        all_words += list(text_boilerplate)
        f, cp, nt, npos, l = make_data_page(text_boilerplate, locs_boilerplate, fn, it_per_page, near_size, far_size)
        field.append(f)
        candidate_pos.append(cp)
        neighbor_text.append(nt)
        neighbor_pos.append(npos)
        label.append(l)
    all_words = set(all_words)
    f = np.concatenate(field, 0)
    field_dict = dict()
    for i in f:
        t = i[0]
        if t not in field_dict:
            field_dict[i[0]] = len(field_dict)
    n_fields = len(field_dict)
    field = np.zeros((len(f), n_fields))
    for i, f_ in enumerate(f):
        field[i] = np.eye(n_fields)[field_dict[f_[0]]]
    candidate_pos = np.concatenate(candidate_pos, 0)
    text = np.concatenate(neighbor_text, 0)
    vocab = VocabularyBuilder(all_words, 1000)
    for i in text:
        for j in i:
            vocab.add(j)
    vocab_dict = vocab.build()
    neighbor_text = np.zeros(text.shape, dtype=np.int32)
    for i in range(text.shape[0]):
        for j in range(text.shape[1]):
            t = text[i, j]
            if is_number(t) or is_date(t):
                neighbor_text[i, j] = 1
            elif t not in vocab_dict:
                neighbor_text[i, j] = 2
            else:
                neighbor_text[i, j] = vocab_dict[t]
    neighbor_pos = np.concatenate(neighbor_pos, 0)
    label = np.concatenate(label, 0)
    return field, candidate_pos, neighbor_text, neighbor_pos, label, field_dict, vocab_dict