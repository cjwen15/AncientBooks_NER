"""
-*- coding: utf-8 -*-
Author:Wen
@Time: 2020-09-11 09:17
"""

import re

# 将第一个变量设为“1”，运行代码结束后，再设回为“0”；
# 将第二个变量设为“1”，运行代码结束后，再设回为“0”；
# 以此类推，六个变量各设为“1”后，分别运行代码结束后，本文件即运行结束
delete_3col = 1
delete_line = 0
blank_line = 0
submit = 0
reverseBlank = 0
reverseTab = 0


# 1. 此段代码是将验证集预测结果（三列）中的第二列（全为O）删除
if delete_3col == 1:
    f = open('val_result_2col.txt', 'w', encoding='utf-8')
    with open('label_test.txt', encoding='utf-8')as originalFile:
        for line in originalFile.readlines():
            data = line.split(' ')
            if line != '\n':
                text = data[0]
                wrong_label = data[1]
                true_label = data[2]
                if text:
                    f.write(text + ' ' + true_label)
                else:
                    f.write('\n')
            else:
                f.write('\n')


# 2. 此段代码是将验证集预测结果（两列）每100行分割的换行符'\n'删掉
if delete_line == 1:
    f = open('val_result_2col_new.txt', 'w', encoding='utf-8')
    with open('val_result_2col.txt', encoding='utf-8')as originalFile:
        for index, line in enumerate(originalFile):
            if index % 100 == 0:
                if line == '\n':
                    continue
                else:
                    f.write(line)
            else:
                f.write(line)


# 3. 将“叕 O”改回换行符'\n'
if blank_line == 1:
    f = open('val_result_blankline.txt', 'w', encoding='utf-8')
    with open('val_result_2col_new.txt', encoding='utf-8')as originalFile:
        for line in originalFile.readlines():
            data = line.split(' ')
            text = data[0]
            label = data[1]
            if text == '叕':
                f.write('\n')
            else:
                f.write(line)


# 4.将结果文件格式（两列）转换成原训练集数据格式
if submit == 1:
	gb = open('val_result_blankline.txt', encoding='utf-8').readlines()
	fb = open('val_submit.txt', 'w', encoding='utf-8')

	text_list = []
	label_list = []

	for data in gb:
		datas = data.split(' ')
		if data != '\n':
			text = datas[0]
			label = datas[1].strip('\n')
			text_list.append(text)
			label_list.append(label)
		else:
			text_list.append('\n')
			label_list.append('')


	for i in range(len(text_list)):

		if label_list[i] == 'O':
			fb.write(text_list[i])

		elif label_list[i] == 'B-noun_bookname':
			fb.write('{{' + 'noun_bookname:' + text_list[i])
			if label_list[i+1] != 'I-noun_bookname':
				fb.write('}}')
			else:
				fb.write(text_list[i+1])
		elif label_list[i] == 'I-noun_bookname':
			if label_list[i+1] == 'I-noun_bookname':
				fb.write(text_list[i+1])
			elif label_list[i-1] == 'O':
				continue
			else:
				fb.write('}}')

		elif label_list[i] == 'B-noun_other':
			fb.write('{{' + 'noun_other:' + text_list[i])
			if label_list[i+1] != 'I-noun_other':
				fb.write('}}')
			else:
				fb.write(text_list[i+1])
		elif label_list[i] == 'I-noun_other':
			if label_list[i+1] == 'I-noun_other':
				fb.write(text_list[i+1])
			elif label_list[i-1] == 'O':
				continue
			else:
				fb.write('}}')

		else:
			fb.write(text_list[i])

# 5. 将生成的val_submit.txt中的“叒”替换成空格符" "
if reverseBlank == 1:
    f = open('val_submit.txt', 'r', encoding='utf-8')
    alllines = f.readlines()
    f.close()
    f = open('val_submit.txt', 'w+', encoding='utf-8')
    for eachline in alllines:
        a = re.sub('叒', ' ', eachline)
        f.writelines(a)
    f.close()

# 6. 将生成的val_submit.txt中的“尛”替换成"　"
if reverseTab == 1:
    f = open('val_submit.txt', 'r', encoding='utf-8')
    alllines = f.readlines()
    f.close()
    f = open('val_submit.txt', 'w+', encoding='utf-8')
    for eachline in alllines:
        a = re.sub('尛', '　', eachline)
        f.writelines(a)
    f.close()
