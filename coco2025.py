
import os
import json
import argparse

def stats_one_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            return 'MAYBE'
        else:
            for line in lines:
                line = line.strip()
                if 'YES' == line:
                    return 'YES'
                elif 'NO' == line:
                    return 'NO'
    return 'MAYBE'

def find_all_txt_files(directory):
    txt_files = []
    res = {
        'YES' : [],
        'NO' : [],
        'MAYBE' : [],
    }
    for root, dirs, files in os.walk(directory):
        trs = root.split("/")[-1]
        for file in files:
            if file.lower().endswith('.txt'):
                full_path = os.path.join(root, file)
                id = os.path.splitext(file)[0]
                res[stats_one_file(full_path)].append(id)
    return res


# 主程序
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--results_dir', type=str, required=True)
    parser.add_argument('--stats_file', type=str, default='coco2025_stats.json')
    args = parser.parse_args()
    results_dir = args.results_dir
    stats_file = args.stats_file
    res = find_all_txt_files(results_dir)
    print('MAYBE', len(res['MAYBE']))
    print('YES', len(res['YES']))
    print('NO', len(res['NO']))
    print('total', len(res['YES']) + len(res['NO']) + len(res['MAYBE']))
    with open(stats_file, 'w') as f:
        json.dump(res, f, indent=4)


