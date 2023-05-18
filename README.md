## Flash Genomics Model (FGM)

My own attempt at a long context genomics model, leveraging recent advances in long context attention modeling (<a href="https://arxiv.org/abs/2205.14135">Flash Attention</a> + other hierarchical methods).

If you would like to collaborate and not averse to having the final model completely open sourced, get in touch. My goal is to simply figure out if long context is what holds us back from a new SOTA model.

## Citations

```bibtex
@inproceedings{dao2022flashattention,
    title   = {Flash{A}ttention: Fast and Memory-Efficient Exact Attention with {IO}-Awareness},
    author  = {Dao, Tri and Fu, Daniel Y. and Ermon, Stefano and Rudra, Atri and R{\'e}, Christopher},
    booktitle = {Advances in Neural Information Processing Systems},
    year    = {2022}
}
```

```bibtex
@article {Dalla-Torre2023.01.11.523679,
    author  = {Hugo Dalla-Torre and Liam Gonzalez and Javier Mendoza Revilla and Nicolas Lopez Carranza and Adam Henryk Grzywaczewski and Francesco Oteri and Christian Dallago and Evan Trop and Hassan Sirelkhatim and Guillaume Richard and Marcin Skwark and Karim Beguir and Marie Lopez and Thomas Pierrot},
    title   = {The Nucleotide Transformer: Building and Evaluating Robust Foundation Models for Human Genomics},
    elocation-id = {2023.01.11.523679},
    year    = {2023},
    doi     = {10.1101/2023.01.11.523679},
    publisher = {Cold Spring Harbor Laboratory},
    URL     = {https://www.biorxiv.org/content/early/2023/01/15/2023.01.11.523679},
    eprint  = {https://www.biorxiv.org/content/early/2023/01/15/2023.01.11.523679.full.pdf},
    journal = {bioRxiv}
}
```

```bibtex
@article {Benegas2022.08.22.504706,
    author  = {Gonzalo Benegas and Sanjit Singh Batra and Yun S. Song},
    title   = {DNA language models are powerful zero-shot predictors of genome-wide variant effects},
    elocation-id = {2022.08.22.504706},
    year    = {2023},
    doi     = {10.1101/2022.08.22.504706},
    publisher = {Cold Spring Harbor Laboratory},
    URL     = {https://www.biorxiv.org/content/early/2023/04/12/2022.08.22.504706},
    eprint  = {https://www.biorxiv.org/content/early/2023/04/12/2022.08.22.504706.full.pdf},
    journal = {bioRxiv}
}
```
