import torch
import torch.nn as nn
import torch.nn.functional as F

from einops import rearrange

class Attention(nn.Module):
    def __init__(self, dim, heads = 8, dim_head = 64, dropout = 0.):
        super().__init__()
        inner_dim = dim_head *  heads
        project_out = not (heads == 1 and dim_head == dim)

        self.heads = heads
        self.scale = dim_head ** -0.5

        self.attend = nn.Softmax(dim = -1)
        self.to_qkv = nn.Linear(dim, inner_dim * 3, bias = False)

        self.to_out = nn.Identity()

    def forward(self, x):
        qkv = self.to_qkv(x).chunk(3, dim = -1)
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = self.heads), qkv)

        dots = torch.matmul(q, k.transpose(-1, -2)) * self.scale

        attn = self.attend(dots)

        out = torch.matmul(attn, v)
        out = rearrange(out, 'b h n d -> b n (h d)')
        
        return self.to_out(out)
    
class NeighborEncoder(nn.Module):
    def __init__(self, dim, heads = 8, dim_head = 64, dropout = 0.):
        super().__init__()
        self.atn = Attention(dim, heads, dim_head, dropout)
        self.fc = nn.Sequential(
            nn.Linear(2*dim, 4*dim),
            nn.Dropout(dropout),
            nn.ReLU(inplace=True),
            nn.Linear(4*dim, dim)
            
        )
        self.pool = nn.AdaptiveMaxPool1d(1)
        
    def forward(self, input):
        x = self.atn(input)
        x = self.fc(x)
        x = x.transpose(-1, -2)
        x = self.pool(x).transpose(-1, -2)
        
        return x
    
class NeighborEmbedder(nn.Module):
    def __init__(self, vocab_size, dim, dropout = 0.):
        super().__init__()
        self.word_embed = nn.Embedding(vocab_size, dim)
        self.fc1 = nn.Linear(2, 128)
        self.fc2 = nn.Linear(128, dim)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(self, word, pos):
        word_emb = self.word_embed(word)
        pos_emb = F.relu(self.fc1(pos))
        pos_emb = self.dropout1(pos_emb)
        pos_emb = F.relu(self.fc2(pos_emb))
        pos_emb = self.dropout1(pos_emb)
        emb = torch.cat((word_emb, pos_emb), dim=-1)

        return emb
    
class Scorer(nn.Module):
    def __init__(self, emb_dim, vocab_size, dropout=0.):
        super().__init__()
        self.field_embedder = nn.Linear(3, emb_dim)
        self.cand_pos_embedder = nn.Linear(2, emb_dim)
        self.neigh_embedder = NeighborEmbedder(vocab_size, emb_dim, dropout)
        self.neighbor_encoder = NeighborEncoder(emb_dim * 2, dropout)
        self.fc = nn.Linear(3 * emb_dim, emb_dim)
        self.sim = nn.CosineSimilarity(dim=1, eps=1e-6)
        
    def forward(self, field, cand_pos, text, pos):
        field_embed = self.field_embedder(field)
        cand_pos_embed = self.cand_pos_embedder(cand_pos)
        
        neigh_embed = self.neigh_embedder(text, pos)
        neigh_encoding = self.neighbor_encoder(neigh_embed)
        
        cand_encoding = torch.cat((cand_pos_embed, neigh_encoding), dim=-1).squeeze(1)
        cand_encoding = F.relu(self.fc(cand_encoding))
        
        score = self.sim(field_embed, cand_encoding)
        score = (score + 1) / 2
        
        return score
