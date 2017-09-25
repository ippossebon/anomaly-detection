#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ast
import math

features_file = open('../dicts/features_201706261220.txt', 'w')

def main():
    s = open('../dicts/dict_201706261220.txt', 'r').read()
    data = ast.literal_eval(s)

    get_flow(data)

def reading(file_name):
    s = open(file_name, 'r').read()
    data = ast.literal_eval(s)

    for source_ip, source_port, target_ip, target_port, protocol, records in data:
        print(item)


def calculate_features(flow, data):
    print("{0} : {1}".format(flow, data))
    import ipdb; ipdb.set_trace()
    print('ok')


def get_flow(data):
    for k, v in data.items():
        if isinstance(v, dict):
          #features_file.write(str(v).rstrip('\n'))
          #features_file.write(str(v))

          get_flow(v)
        else:
          # key = data.keys()[data.values().index(v)]
          features_file.write(str(v))
          features_file.write('\n')
          calculate_features(flow=k, data=v)


if __name__ == '__main__':
    main()
