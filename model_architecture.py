import torch
import torch.nn as nn
import torch.nn.functional as F

class Network(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(in_features=6, out_features=40) # Linear layer 1 
        self.fc2 = nn.Linear(in_features=40, out_features=81) # Linear layer 2
        self.fc3 = nn.Linear(in_features=81, out_features=36) # Linear layer 3
        self.fc4 = nn.Linear(in_features=36, out_features=19) # Linear layer 4
        self.out = nn.Linear(in_features=19, out_features=2) # Linear layer 5 (output layer)
        
    def forward(self, t):
        # input layer
        t=t
        # (1) hidden conv layer
        t = self.fc1(t)
        t = F.relu(t)

        # (2) hidden linear layer
        t = self.fc2(t)
        t = F.relu(t)
        
        # (3) hidden linear layer
        t = self.fc3(t)
        t = F.relu(t)
        
        # (4) hidden linear layer
        t = self.fc4(t)
        t = F.relu(t)
        
        # (5) output layer
        t = self.out(t)
        #t = F.softmax(t, dim=1)
        
        return t

        