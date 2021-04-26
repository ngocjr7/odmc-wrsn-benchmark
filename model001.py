import sys
sys.path.insert(0, './model001')

from utils import device, pdump, pload
from utils import WRSNDataset
from utils import WrsnParameters as wp, DrlParameters as dp
from model import MCActor
import main as model001
import os
import torch
import random_strategy

def run(data_loader, name, save_dir):
    actor = MCActor(dp.MC_INPUT_SIZE,
                    dp.SN_INPUT_SIZE,
                    dp.hidden_size,
                    dp.dropout).to(device)

    save_dir = os.path.join(save_dir, name)
    checkpoint = 'model001/checkpoints/mc_20_10_0/21'
    path = os.path.join(checkpoint, 'actor.pt')
    actor.load_state_dict(torch.load(path, device))

    ret = model001.validate(data_loader, actor, render=False)

    return ret

def run_random(data_loader, name, save_dir):
    save_dir = os.path.join(save_dir, name)
    return random_strategy.validate(data_loader, save_dir)