"""
-*- coding: utf-8 -*-
Author:Wen
@Time: 2020-07-10 16:21
"""


# 此段代码是对比生成的label.txt和测试集task1_no_val_utf8_afterFormat_split100.txt哪里不同，
# 即目的是为了返回label.txt缺失的行的行号，然后根据task1_no_val_utf8_afterFormat_split100.txt，人工补上
# 运行一次，看第一次不同的地方在哪，手动补上后，再运行第二次；再看这次运行后第一次不同的地方在哪，手动补上......

test_file = open('NER-test3_afterFormat_split100.txt', 'r', encoding='utf-8')
new_file = open('label_test.txt', 'r', encoding='utf-8')

test_text = []
new_text = []

for line in test_file.readlines():
    if line == '\n':
        test_text.append('\n')
        # continue
    else:
        data = line.split(' ')
        test_text.append(data[0])


for line in new_file.readlines():
    if line == '\n':
        new_text.append('\n')
        # continue
    else:
        data = line.split(' ')
        new_text.append(data[0])


i = 0
for i in range(len(test_text)):
    if test_text[i] != new_text[i]:
        print(i)
        break
    else:
        continue





