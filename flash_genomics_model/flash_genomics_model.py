import torch
import torch.nn.functional as F
from torch import nn, einsum, Tensor

from einops import rearrange, reduce

from flash_genomics_model.attend import Attend

# functions

# attention

class Attention(nn.Module):
    def __init__(
        self,
        dim,
        dim_head = 64,
        heads = 8,
        flash = True
    ):
        super().__init__()
        self.heads = heads
        dim_inner = heads * dim_head
        self.attend = Attend(flash = flash)

        self.to_qkv = nn.Linear(dim, dim_inner * 3, bias = False)
        self.to_out = nn.Linear(dim_inner, dim, bias = False)

    def forward(
        self,
        x,
        mask = None
    ):
        h = self.heads
        q, k, v = self.to_qkv(x).chunk(3, dim = -1)
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = h), (q, k, v))

        out = self.attend(q, k, v, mask = mask)

        out = rearrange(out, 'b h n d -> b n (h d)')
        return self.to_out(out)

# main class

class FlashGenomicsModel(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
