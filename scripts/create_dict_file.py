#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

data_dict = {}
flows_dict = {}

def main():
    create_dict_whitespace('./data/201706261220.txt')

def create_dict_whitespace(file_name):
    count = 0

    with open(file_name) as f:
        content = f.readlines()


    for line in content:
        count = count + 1
        add_dict_entry(line.split())
        print(count)

    out_file = open('./dicts/dict_201706261220.txt', 'w')
    out_file.write(str(flows_dict))
    # print(data_dict['224.186.103.110'])
    # print(flows_dict)


# Formato: [data, timestamp, duracao, protocolo, source, '->', destino, numero_pacotes, tamanho, 'M', '1']
# Exemplo: ['2017-06-26', '12:20:00.002', '0.000', 'TCP', '77.249.239.27:443', '->', '77.242.250.39:2711', '1024', '1.6', 'M', '1']
def add_dict_entry(item_list):
    try:
        source = item_list[4]
        source_list = source.split(':')

        source_ip = source_list[0]
        source_port = source_list[1]

        target = item_list[6]
        target_list = target.split(':')

        try:
            target_ip = target_list[0]
            target_port = target_list[1]
            protocol = item_list[3]

            if source_ip not in data_dict.keys():
                data_dict[source_ip] = {}

            data_dict[source_ip][source_port] = {
                'target_ip': target_ip,
                'target_port': target_port,
                'protocol': protocol,
                'date': item_list[0],
                'timestamp': item_list[1],
                'duration': item_list[2],
                'packets': item_list[7],
                'size_in_bytes': item_list[8]
            }

            if source_ip not in flows_dict.keys():
                flows_dict[source_ip] = {}

            if source_port not in flows_dict[source_ip].keys():
                flows_dict[source_ip][source_port] = {}

            if target_ip not in flows_dict[source_ip][source_port].keys():
                flows_dict[source_ip][source_port][target_ip] = {}

            if target_port not in flows_dict[source_ip][source_port][target_ip].keys():
                flows_dict[source_ip][source_port][target_ip][target_port] = {}

            if protocol not in flows_dict[source_ip][source_port][target_ip][target_port].keys():
                flows_dict[source_ip][source_port][target_ip][target_port][protocol] = {}
                flows_dict[source_ip][source_port][target_ip][target_port][protocol]['records'] = []

            flows_dict[source_ip][source_port][target_ip][target_port][protocol]['records'].append({
                'date': item_list[0],
                'timestamp': item_list[1],
                'duration': item_list[2],
                'packets': item_list[7],
                'size_in_bytes': item_list[8]
            })


        except Exception as e:
            print('Erro ao ler target_ip e target_port: {0}'.format(e))
            print(item_list)
    except Exception as e:
            print('Erro ao ler source_ip e source_port: {0}'.format(e))
            print(item_list)


if __name__ == '__main__':
    main()
