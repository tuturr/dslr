import csv
import argparse
import numpy as np
import matplotlib.pyplot as plt
from CORE.maths import *

#----------------------------------------------------------------------
# Initialisation du parseur d'arguments

parser = argparse.ArgumentParser()
parser.add_argument("dataset", type=str, help="input dataset")
args = parser.parse_args()

#
#-----------------------------------------------------------------

def describe(filename):
    """Fonction affichage du tableau de donnee pour describe.py"""
    dataset = load_csv(filename)
    features = dataset[0]
    dataset = dataset[1:, :]
    print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
    for i in range(0, len(features)):
        print(f'{features[i]:15.15}', end=' |')
        try:
            data = np.array(dataset[:, i], dtype=float)
            data = data[~np.isnan(data)]
            if data.any() is False:
                raise Exception()
            print(f'{count_(data):>12.4f}', end=' |')
            print(f'{mean_(data):>12.4f}', end=' |')
            print(f'{std_(data):>12.4f}', end=' |')
            print(f'{min_(data):>12.4f}', end=' |')
            print(f'{percentile_(data, 25):>12.4f}', end=' |')
            print(f'{percentile_(data, 50):>12.4f}', end=' |')
            print(f'{percentile_(data, 75):>12.4f}', end=' |')
            print(f'{max_(data):>12.4f}')
        except:
            print(f'{count_(dataset[:, i]):>12.4f}', end=' |')
            print(f'{"No numerical value to display":>60}')

def load_csv(filename):
  """Chargement de la data depuis le csv"""
  dataset = list()
  with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    try:
      for _ in reader:
        row = list()
        for value in _:
          try:
            value = float(value)
          except:
            if not value:
              value = np.nan
          row.append(value)
        dataset.append(row)
    except csv.Error as e:
      print(f'file {filename}, line {reader.line_num}: {e}')
  return np.array(dataset, dtype=object)

if __name__ == "__main__":
    describe(args.dataset)
