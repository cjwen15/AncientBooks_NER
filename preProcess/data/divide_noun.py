"""
-*- coding: utf-8 -*-
Author:Wen
@Time: 2020-07-12 15:14
"""

# 1.已有书名、专名标签的语料作为训练数据，训练得到“书名、专名分类”模型
# 1.1 预测得到书名和专名的分类结果,经reverseFormat/find_different_line修正
# 1.2 经reverseFormat/select_other,将预测结果中的专名单独提取出来predict_other.txt
# 2.使用“专名归类”模型，对predict_other.txt中的专名进行归类（6类）

# 以下是“2.”的详细步骤
# 将 nounBIO.txt（实体词典）中的 bookname 和 other 分别保存到两个文件中 dict_booknameBIO.txt, dict_otherBIO.txt
# 然后对dict_otherBIO.txt进行操作，对里面的专名进行手动归类（(1)人名:person  (2)地名:location  (3)朝代名:time  (4)官名:title  (5)民族名:nation  (6)天文名:star）
# 归类完之后，dict_otherBIO.txt作为“专名归类”模型的训练数据
# 首先对predict_other.txt进行格式转换，转换成  每一行为 “char O”，每一个专名之间插入一个空行，文件命名为predict_other_withO.txt
# 使用训练好的“专名归类”模型，对predict_other_withO.txt中专名进行归类

# originFile = open('nounBIO.txt', 'r', encoding='utf-8')
# bookFile = open('dict_booknameBIO.txt', 'a+', encoding='utf-8')
# otherFile = open('dict_otherBIO.txt', 'a+', encoding='utf-8')
#
# text = []
# label = []
#
# for line in originFile.readlines():
#     data = line.split(' ')
#     if line != '\n':
#         text.append(data[0])
#         label.append(data[1].strip('\n'))
#     else:
#         text.append('\n')
#         label.append('\n')
#
# for i in range(len(label)):
#     if label[i] == 'B-noun_bookname':
#         bookFile.write(text[i] + ' ' + label[i] + '\n')
#         if label[i+1] != 'I-noun_bookname':
#             bookFile.write('\n')
#     elif label[i] == 'I-noun_bookname':
#         bookFile.write(text[i] + ' ' + label[i] + '\n')
#         if label[i+1] != 'I-noun_bookname':
#             bookFile.write('\n')
#     elif label[i] == 'B-noun_other':
#         otherFile.write(text[i] + ' ' + label[i] + '\n')
#         if label[i+1] != 'I-noun_other':
#             otherFile.write('\n')
#     elif label[i] == 'I-noun_other':
#         otherFile.write(text[i] + ' ' + label[i] + '\n')
#         if label[i+1] != 'I-noun_other':
#             otherFile.write('\n')
#     else:
#         continue
#
