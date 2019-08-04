# !/usr/bin/env
# -*- coding:utf-8 -*-

import re
import pandas as pd


# # # convert encoding
# #
# all_data = pd.read_csv('../data/mydata/entity_all_gbk.csv', encoding='gbk')
# all_data = all_data.rename(columns={'序号':'id'})
# all_data.to_csv('../data/mydata/entity_all.csv', encoding='utf-8', index=False)

# # split data
# #
# all_data = pd.read_csv('../data/mydata/entity_all.csv', encoding='utf-8')
# valid_data = all_data.sample(n=int(len(all_data) * 0.2))
# print(valid_data.count())
# all_data = all_data.append(valid_data)
# train_data = all_data.drop_duplicates(keep=False)
# print(train_data.count())
# train_data.to_csv('../data/mydata/entity_train.csv', encoding='utf-8', index=False)
# valid_data.to_csv('../data/mydata/entity_valid.csv', encoding='utf-8', index=False)

# # preprocess
# #
# regex = r"[\u4e00-\ufaff]|[0-9]|[a-zA-Z]|['【', '】', '&', '.', ',', '。'，', '!', '！']"
# train_data = pd.read_csv('../data/mydata/entity_valid.csv', encoding='utf-8')
# train_data = train_data.fillna(' ')
# str_list = []
# person_list = []
# place_list = []
# org_list = []
# for index, row in train_data.iterrows():
#    char_list = re.findall(regex, row['text'], re.UNICODE)
#    str = ""
#    for char in char_list:
#        str += char
#    str = str.replace(' ','')
#    person = row['entity_person'].replace(' ','')
#    place = row['entity_place'].replace(' ','')
#    org = row['entity_org'].replace(' ','')
#    str_list.append(str)
#    person_list.append(person)
#    place_list.append(place)
#    org_list.append(org)
# train_data['text'] = str_list
# train_data['entity_person'] = person_list
# train_data['entity_place'] = place_list
# train_data['entity_org'] = org_list
# train_data.to_csv('../data/mydata/entity_valid_processed.csv', encoding='utf-8', index=False)

# # sequence labeling
# train_data = pd.read_csv('../data/mydata/entity_train_processed.csv', encoding='utf-8')
# train_data = train_data.fillna(' ')
# for index, row in train_data.iterrows():
#    person_list = row['entity_person'].split(',')
#    if person_list != [' ']:
#       print(person_list)
#    place_list = row['entity_place'].split(',')
#    if place_list != [' ']:
#       print(place_list)
#    org_list = row['entity_org'].split(',')
#    if org_list != [' ']:
#       print(org_list)
start = [m.start() for m in re.finditer('test', 'test is just test')]
b = ["o" for i in range(17)]
for i in start:
    b[i] = 'start'
    for index in range(len('test')-1):
        b[i + index + 1] = 'inside'
    b[i + len('test')] =


















































