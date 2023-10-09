import os

#Load data
dataset_dir = os.path.join(os.path.dirname(__file__), "dataset")

dataset_pos_file = os.path.join(dataset_dir, "Train.pos")
dataset_neg_file = os.path.join(dataset_dir, "Train.neg")

if not os.path.exists(dataset_neg_file) or not os.path.exists(dataset_pos_file):
    print("dataset file not found!!!!")
    exit(0)

train_positive = open(dataset_pos_file , "r", encoding="latin-1").read()
train_negative = open(dataset_neg_file , "r", encoding="latin-1").read()