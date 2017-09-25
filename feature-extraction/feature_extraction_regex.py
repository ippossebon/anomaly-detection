#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def main():
    create_dict('./data/201706261220.txt')



def create_dict(file_name):
    date_regex = '((\d+)-(\d+)-(\d+))'
    timestamp_regex = '((\d+):(\d+):(\d+).(\d+))(\s+)((\d+).(\d+))'
    source_ipv4_regex = '(\S+)(\s+)((\d+).(\d+).(\d+).(\d+):(\d+)(\s+\S+\s+)'
    target_ipv4_regex = '((\d+).(\d+).(\d+).(\d+):(\d+)))'
    packets_regex = '(\s+) (\d+) (\s+)'
    size_regex = '(\S+) \S?'
    # regex = re.compile('(' + date_regex + timestamp_regex + source_ipv4_regex + target_ipv4_regex + packets_regex + size_regex +')');
    regex = re.compile('((\d+)-(\d+)-(\d+)) ((\d+):(\d+):(\d+).(\d+))(\s+)((\d+).(\d+)) (\S+)(\s+)((\d+).(\d+).(\d+).(\d+):(\d+)(\s+\S+\s+) ((\d+).(\d+).(\d+).(\d+):(\d+))) (\s+) (\d+) (\s+) (\S+) \S?')

    with open(file_name) as f:
        content = f.readlines()

    out_file = open('saida.txt', 'w')

    count = 1
    for line in content:
        match = re.match(regex, line)

        if match:
            data = match.group(1)
            timestamp = match.group(5)
            duracao = match.group(11)
            protocolo = match.group(14)
            ips = match.group(16)
            packets = match.group(30)
            tamanho = match.group(32)

            out_file.write('data: ' + data)
            out_file.write('duracao: ' + duracao)
            out_file.write('protocolo: ' + protocolo)
            out_file.write('ips: ' + ips)
            out_file.write('packets: ' + packets)
            out_file.write('tamanho: ' + tamanho)
            out_file.write('--------')
            import ipdb; ipdb.set_trace()
        else:
            print(line)
            count = count + 1

    print('Linhas não contabilizadas:')
    print(count)


if __name__ == '__main__':
    main()
