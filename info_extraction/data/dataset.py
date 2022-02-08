import torch

class Dataset(torch.utils.data.Dataset):
    def __init__(self, field, candidate_pos, neighbor_text, neighbor_pos, label):
        self.field = field
        self.candidate_pos = candidate_pos
        self.neighbor_text = neighbor_text
        self.neighbor_pos = neighbor_pos
        self.label = label
        
    def __getitem__(self, idx):
        return (
            torch.Tensor(self.field[idx]),
            torch.Tensor(self.candidate_pos[idx]),
            torch.LongTensor(self.neighbor_text[idx]),
            torch.Tensor(self.neighbor_pos[idx]),
            torch.FloatTensor(self.label[idx])
        )
    
    def __len__(self):
        return len(self.label)