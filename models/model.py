import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.data import  Dataset, DataLoader
import copy
import random
from sklearn.model_selection import train_test_split



class SongDataset(Dataset):    

    def __init__(self, songs, max_song):
        
        self.songs = songs
        self.max_song = max_song
        self.vector = np.zeros(max_song, dtype=np.float32)
        
    def get_vector(self, vec):
        cop_vector = copy.deepcopy(self.vector)
        if vec:
            cop_vector[vec] = 1            
        return cop_vector    

        
    def denosing(self, x):
        if len(x)<2:
            return x
        tr, te = train_test_split(x, test_size=0.2)
        return tr
    
    def __getitem__(self, idx):
        
        x = self.songs[idx]        
        d_x = self.denosing(x)
        d_x = self.get_vector(d_x)
        x = self.get_vector(x)
        return d_x, x
        
    def __len__(self):
        return len(self.songs)

    
    
class AE(nn.Module):
    def __init__(self, max_song):
        
        super(AE, self).__init__()        
        self.encoder = nn.Sequential(
                    nn.Linear(max_song, 128), 
                    nn.SELU(),
                    nn.Linear(128, 256),
                    nn.SELU(),
                    nn.Linear(256, 256),
                    nn.SELU()
        )
        self.dropout = nn.Dropout(p=0.7)
        self.decoder = nn.Sequential(
                    nn.Linear(256, 256),
                    nn.SELU(),                    
                    nn.Linear(256, 128),
                    nn.SELU(),                    
                    nn.Linear(128, max_song), 
                    nn.SELU()
        )
        
    def forward(self, x):
        
        x = self.encoder(x)
        x = self.dropout(x)
        x = self.decoder(x)        
        
        return x