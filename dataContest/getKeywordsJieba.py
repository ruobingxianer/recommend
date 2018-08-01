#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba.analyse

str = "本文基于2014年中国家庭追踪调查（CFPS）数据。研究表明，性别观念和工作家庭冲突对城镇和农村女性的婚姻幸福感的影响机制不同。性别观念对于城市女性的婚姻幸福感并不存在显著的影响。但是对农村女性而言，持有男女平等的性别观念将会降低婚姻幸福感。对于城市女性来说，女性的相对家务劳动时间越长，婚姻越不幸福。但是这一影响和女性的相对收入有关。然而，在考虑女性的相对收入以后，相对家务劳动时间对婚姻幸福感的影响几乎消失。如果家庭内部的分工模式为女性带来更强的工作-家庭冲突，女性的婚姻幸福感就会降低。在体制和文化观念双重转型背景下，这些发现不仅为推动婚姻家庭、工作等政策的优化提供经验证据，还为促进中国社会婚姻的幸福提供实践上的启示。"
seg_list = jieba.cut(str, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))
for x, w in jieba.analyse.textrank(str, withWeight=True):
    print('%s %s' % (x, w))
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))