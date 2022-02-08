import argparse
from distutils.util import strtobool

parser = argparse.ArgumentParser(description="Information Extraction args")

parser.add_argument("--near_size", type=int, default=2, help="Number of negative samples near the correct text")
parser.add_argument("--far_size", type=int, default=1, help="Number of negative samples far from the correct text")
parser.add_argument("--it_per_page", type=int, default=50, help="Number of random examples of each page")
parser.add_argument("--emb_dim", type=int, default=256, help="Embedding dimension")
parser.add_argument("--batch_size", type=int, default=128, help="Batch size")
parser.add_argument("--lr", type=float, default=0.001, help="Learning rate")
parser.add_argument("--num_epochs", type=int, default=3, help="Number of epochs")
parser.add_argument("--entity", type=str, default='andyehrenberg', help="Wandb username")