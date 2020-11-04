"""
-*- coding: utf-8 -*-
Author:Wen
@Time: 2020-07-05 08:58
"""


# 此段代码是将9.22发布的测试集进行处理
# 1.转换成汉字全放在第一列，增加第二列全为O
# 2.将每一句结束的位置('\n')替换成“叕 O”
# 3.删去了所有换行符，再按每100行分割
origin_path = 'data/0922/NER-test2.txt'
after_path = 'data/0922/NER-test2_afterFormat.txt'


# 1. 2.

with open(after_path, 'w', encoding='utf-8') as af:
    with open(origin_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line_list = list(line)
            for ii in range(len(line_list)):
                if line_list[ii] != " " and line_list[ii] != '\n':
                    af.write(line_list[ii] + ' ' + 'O' + '\n')
                elif line_list[ii] == '\n':
                    af.write('叕' + ' ' + 'O' + '\n')
                elif line_list[ii] == ' ':
                    af.write('叒' + ' ' + 'O' + '\n')
                elif line_list[ii] == '　':
                    af.write('尛' + ' ' + 'O' + '\n')
                else:
                    af.write(line_list[ii] + '\n')

# 3.
# NER-test_afterFormat_split100.txt 作为测试集数据

sf = open('data/0922/NER-test3_afterFormat_split100.txt', 'w', encoding='utf-8')
with open(after_path, encoding='utf-8') as af:
    for index, line in enumerate(af):
        if index % 99 == 0:
            sf.write('\n' + line)
        else:
            sf.write(line)
