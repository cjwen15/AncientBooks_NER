# AncientBooks_NER
CCL2020 “古联杯”古籍文献命名实体识别评测

## 运行环境：
1. python:3.7
2. tensorflow-gpu:1.15.0
3. numpy:1.16.5

## 运行步骤：
1. 下载预训练模型chinese_roberta_wwm_ext_L-12_H-768_A-12，link:https://github.com/ymcui/Chinese-BERT-wwm
2. 测试集数据“命名实体识别测试集.txt”，重命名为“NER-test3.txt”,存放到bert_bilstm_crf/data/0922文件夹中。
3. 运行bert_bilstm_crf/val_split.py，此步是修改测试集数据的格式，生成多个文件，其中bert_bilstm_crf/data/0922/NER-test3_afterFormat_split100.txt作为测试集路径。
4. 运行 bert_bilstm_crf/bert_lstm_ner.py （文件中的第38、39、41、42、211行的路径可能需要修改，203行对应训练集的路径，211行对应测试集路径）。默认重新训练模型。
5. 训练及预测完成后，生成的文件全部放在bert_bilstm_crf/output文件夹中。
6. 复制output/label_test.txt到preProcess/reverseFormat文件夹中。
由于预测得到的结果文件label_test.txt比测试集文件bert_bilstm_crf/data/NER-test3_afterFormat_split100.txt缺少了少数字符，此时运行preProcess/reverseFormat/find_differnent_Line.py，找出缺失的字符的位置，并手动补上（具体操作在该文件的注释）。
7. 手动补上后，运行preProcess/reverseFormat/submit_format，这一步会生成多个文件存放到preProcess/reverseFormat文件夹中，其中val_submit.txt即为要提交的结果文件（具体操作在该文件的注释）。
8. 结束。

## 补充：
1. 比赛网址：http://match.ancientbooks.cn
2. 后续对步骤6的缺陷作出了改进，并未补充到项目中，针对bert_bilstm_crf/bert_lstm_ner.py进行了修改，可参考https://github.com/FuYanzhe2/Name-Entity-Recognition/issues/15
3. 这里仅上传了一部分训练数据，剩余的后续进行补充。
4. 本项目的方法较为简单，可作为一个baseline。
5. 欢迎交流，学习！
