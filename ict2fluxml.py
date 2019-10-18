#!/usr/bin/env python3

import argparse
import numpy as np
import csv

MIN_STD = 0.01


class IctDatum:
    def __init__(self, name, weights, data):
        self.name = name
        self.weights = weights
        self.data = data

    def normalize_data(self):
        dsums = np.sum(self.data, axis=0)
        for dsum in dsums:
            if dsum == 0:
                dsum = 1
        return self.data/dsums


def parse_ict(filename):
    ict_data = []
    cur_name = ''
    data = []
    weights = []
    first = True
    with open(filename, 'r') as ict_file:
        ict_reader = csv.reader(ict_file, delimiter=',')
        for row in ict_reader:
            if len(row) >= 2:
                split_label = row[0].split('_')
                name = split_label[0]
                weight = split_label[1][1:].replace('.', ',')
                if name != cur_name:
                    if not first:
                        # new mid, add entry to icd_data
                        ict_data.append(IctDatum(cur_name, weights, data))
                    else:
                        first = False

                    # start new data set
                    cur_name = name
                    weights = [weight]
                    data = [list(map(float, (row[1:])))]

                else:
                    # append data
                    weights.append(weight)
                    data.append(list(map(float, (row[1:]))))
        # write final dataset
        ict_data.append(IctDatum(cur_name, weights, data))
    return ict_data


def to_fluxml(name, weight, value, stddev):
    print('        <datum id=\"{0}\", stddev=\"{1}\", weight=\"{2}\">{3}</datum>'.format(name, stddev, weight, value))


def main():
    parser = argparse.ArgumentParser('Convert the output of ICT to fluxml notation')
    parser.add_argument('filename', metavar='corr.txt', nargs=1, help='the file with the corrected data from ICT')
    args = parser.parse_args()
    ict_data = parse_ict(args.filename[0])
    for ict_datum in ict_data:
        normalized_data = ict_datum.normalize_data()
        for i in range(0, len(normalized_data)):
            mgroup_name = ict_datum.name
            weight = ict_datum.weights[i]
            stddev = max(MIN_STD, np.std(normalized_data[i]))
            value = np.mean(normalized_data[i])
            to_fluxml(mgroup_name, weight, value, stddev)


if __name__ == "__main__":
    main()
