#!/usr/bin/env python3
print("rom-names-processing")

# Yaowen Xu
# 2021年2月1日

# 读文件并输出到 STDOUT
with open('rom-names.txt', 'r') as f:
    with open('rom-names-with-hyphen.txt', 'w') as of:
        for line in f:
            if line[0] == '#' :
                of.writelines(line)
                continue
            oline = "- " + line
            print(oline)
            of.writelines(oline)
