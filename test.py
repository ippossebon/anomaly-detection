import re
import os

def execute():
    timestamp_regex = re.compile('(\d*-\d*-\d*) (\d*:\d*:\d*)')
    ips_regex = re.compile('((\d*\@)?\d*\.\d*\.\d*\.\d*(:\d*)?)')

    for filename in os.listdir('./errorLogs/'):
        if filename.endswith('.txt'):
            complete_filename = './errorLogs/' + filename

            with open(complete_filename) as file_data:
                import ipdb; ipdb.set_trace()
                for line in file_data:
                    timestamp_matched = re.match('(\d*-\d*-\d*) (\d*:\d*:\d*)', line)
                    if timestamp_matched:
                        date = timestamp_matched.group(1)
                        time = timestamp_matched.group(2)
                        print("Match timestamp: ", date, time)

                    ips_matched = re.match('((\d*\@)?\d*\.\d*\.\d*\.\d*(:\d*)?)', line)
                    if ips_matched:
                        target_ip = ips_matched.group(1)
                        source_ip = ips_matched.group(2)
                        print("Match ips: ", target_ip, source_ip)


if __name__ == '__main__':
    execute()
