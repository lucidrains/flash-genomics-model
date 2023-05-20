import torch
import torch.nn.functional as F
from torch import nn, einsum, Tensor

from einops import rearrange, reduce

from flash_genomics_model.attend import Attend

# functions
def exists(val):
    return val is not None

def default(val, d):
    return val if exists(val) else d

# helper classes

# main class

class FlashGenomicsModel(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
