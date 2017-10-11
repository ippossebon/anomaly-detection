#!/bin/bash
for file in ./asterisk_logs/*.txt; do
    grep -ri "failed for" > 'wrong_pass_out.txt'
done

for file in ./asterisk_logs2/*.txt; do
    grep -ri "failed for" > 'wrong_pass_out2.txt'
done
