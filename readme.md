# SuperAGI GPT-2 

https://contlo.notion.site/contlo/Assignment-32610c8f37dd4435b1f97ecaff93bdaf

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
  - [Single GPU Training](#single-gpu-training)
  - [Distributed Data Parallel (DDP)](#distributed-data-parallel-ddp)
  - [Fully Sharded Data Parallel (FSDP)](#fully-sharded-data-parallel-fsdp)
- [References](#references)



## Introduction

This repository provides a training loop for GPT-2 models, accommodating various training setups: single GPU, DDP, and FSDP. The script supports training on custom datasets and can be easily adapted for specific project requirements.

This repository contains a PyTorch-based training loop for GPT-2, supporting single GPU, Distributed Data Parallel (DDP), and Fully Sharded Data Parallel (FSDP) setups.

The `model.ipynb` interactive notebook contains a functional training loop for GPT-2, and it is equipped to handle single GPU, DDP, and FSDP training. Here's a brief overview of each function in the script:

- `create_model_optimizer(lr=5e-5)`: Function to create a GPT-2 model and an AdamW optimizer with a specified learning rate.
- `train_single_gpu(model, optimizer, criterion, dataloader, device)`: Function to train the model on a single GPU.
- `train_ddp(model, optimizer, criterion, dataloader, device)`: Function to train the model using Distributed Data Parallel (DDP) across multiple GPUs.
- `train_fsdp(model, optimizer, criterion, dataloader, device)`: Function to train the model using Fully Sharded Data Parallel (FSDP) for fully sharded parallelism.
- Sample dataset and dataloader: A placeholder for the dataset and dataloader; replace it with your actual implementation.
- `SampleDataset`: An example dataset class (replace with your custom dataset class).
- `criterion`: CrossEntropyLoss used as the loss function.



## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Mannxxx/SuperAGI_AI_Assignment_Submission.git
   cd SuperAGI_AI_Assignment_Submission

   ```

2. Install the required dependencies:

```
pip install torch torchvision
```

3. Replace the sample dataset and dataloader in the script (train.py) with your actual dataset and dataloader.



## Usage

### Single GPU Training

To train the model on a single GPU, use `train_single_gpu` function.

### Distributed Data Parallel (DDP)

To train the model using DDP across multiple GPUs, use `train_ddp` function.

### Fully Sharded Data Parallel (FSDP)

To train the model using FSDP for fully sharded parallelism, use `train_fsdp` function.



## References

- PyTorch's DDP Tutorial: https://pytorch.org/tutorials/intermediate/ddp_tutorial.html
- Gupta et al., "Training GPT-3 Like Models on a Single Machine": https://arxiv.org/pdf/2101.06840.pdf
- nanoGPT repo: https://github.com/karpathy/nanoGPT/blob/master/model.py
- "Attention Is All You Need": https://arxiv.org/abs/1706.03762

