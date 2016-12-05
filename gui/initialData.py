# -*- coding: utf-8 -*-

companyList = [
    '营房仓库',
    '上级配发',
    '采购中心统购',
    'ZB1YB',
    'ZB1L',
    'ZB2L',
    'ZB3L',
    '1PL',
    'ZB2YB',
    'ZB4L',
    'ZB5L',
    'ZB6L',
    '2PL',
    'ZB3YB',
    'ZB7L',
    'ZB8L',
    'ZB9L',
    '3PL',
    'ZB4YB',
    'ZB10L',
    'ZB11L',
    'ZB12L',
    '4PL'
]

waterList = ['阀门', '生料带', '水龙头', '水管']
electricList = ['灯泡', '射灯', '花线', '铜线', '铝线']
furnitureList = ['单人床', '双人床', '干部柜', '四门柜', '两斗桌', '三斗桌', '学习椅']
equipmentList = ['84A帐篷', '93帐篷', '1.5KW汽油发电机', '3KW发电机']
othersList = ['垃圾桶', '门把手', '门锁', '沐浴喷头']

kinds = {'营产营具': furnitureList,
         '野营装备': equipmentList,
         '水料': waterList,
         '电料': electricList,
         '其它': othersList
         }


allList = ['全部']
for i in kinds.keys():
    for a in kinds[i]:
        allList.append(a)



