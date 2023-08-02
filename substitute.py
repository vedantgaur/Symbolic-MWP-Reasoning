import argparse
import numpy as np
import pandas as pd

from helpers import replace, get_len_problems

parser = argparse.ArgumentParser()
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
args = parser.parse_args()

len = get_len_problems()

data = pd.DataFrame(columns=["Question", "Equation"], index=np.arange(len))

for i in range(len):
    replace(replacements=args.list, index=i)
    data["Question"][i], data["Equation"][i] = replace(replacements=args.list, index=i)

path = f"Datasets/Variables/SVAMP_{args.list[0]}{args.list[1]}{args.list[2]}{args.list[3]}.csv"
data.to_csv(path)