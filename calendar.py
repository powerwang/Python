# -*- coding: utf-8 -*-

G = ["庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己"]
Z = ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未"]

M = [
	["丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉", "甲戌", "乙亥", "丙子", "丁丑"],
	["戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未", "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑"],
	["庚寅", "辛卯", "壬辰", "癸巳", "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑"],
	["壬寅", "癸卯", "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑"],
	["甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥", "甲子", "乙丑"]
]


ND = [
	"初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
	"十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
	"廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"
]

NM = [
	["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"],
	["闰一", "闰二", "闰三", "闰四", "闰五", "闰六", "闰七", "闰八", "闰九", "闰十", "闰十一", "闰十二"]
]

DB = [
	0x04AE53,0x0A5748,0x5526BD,0x0D2650,0x0D9544,0x46AAB9,0x056A4D,0x09AD42,0x24AEB6,0x04AE4A,
	0x6A4DBE,0x0A4D52,0x0D2546,0x5D52BA,0x0B544E,0x0D6A43,0x296D37,0x095B4B,0x749BC1,0x049754,
	0x0A4B48,0x5B25BC,0x06A550,0x06D445,0x4ADAB8,0x02B64D,0x095742,0x2497B7,0x04974A,0x664B3E,
	0x0D4A51,0x0EA546,0x56D4BA,0x05AD4E,0x02B644,0x393738,0x092E4B,0x7C96BF,0x0C9553,0x0D4A48,
	0x6DA53B,0x0B554F,0x056A45,0x4AADB9,0x025D4D,0x092D42,0x2C95B6,0x0A954A,0x7B4ABD,0x06CA51,
	0x0B5546,0x555ABB,0x04DA4E,0x0A5B43,0x352BB8,0x052B4C,0x8A953F,0x0E9552,0x06AA48,0x6AD53C,
	0x0AB54F,0x04B645,0x4A5739,0x0A574D,0x052642,0x3E9335,0x0D9549,0x75AABE,0x056A51,0x096D46,
	0x54AEBB,0x04AD4F,0x0A4D43,0x4D26B7,0x0D254B,0x8D52BF,0x0B5452,0x0B6A47,0x696D3C,0x095B50,
	0x049B45,0x4A4BB9,0x0A4B4D,0xAB25C2,0x06A554,0x06D449,0x6ADA3D,0x0AB651,0x093746,0x5497BB,
	0x04974F,0x064B44,0x36A537,0x0EA54A,0x86B2BF,0x05AC53,0x0AB647,0x5936BC,0x092E50,0x0C9645,
	0x4D4AB8,0x0D4A4C,0x0DA541,0x25AAB6,0x056A49,0x7AADBD,0x025D52,0x092D47,0x5C95BA,0x0A954E,
	0x0B4A43,0x4B5537,0x0AD54A,0x955ABF,0x04BA53,0x0A5B48,0x652BBC,0x052B50,0x0A9345,0x474AB9,
	0x06AA4C,0x0AD541,0x24DAB6,0x04B64A,0x69573D,0x0A4E51,0x0D2646,0x5E933A,0x0D534D,0x05AA43,
	0x36B537,0x096D4B,0xB4AEBF,0x04AD53,0x0A4D48,0x6D25BC,0x0D254F,0x0D5244,0x5DAA38,0x0B5A4C,
	0x056D41,0x24ADB6,0x049B4A,0x7A4BBE,0x0A4B51,0x0AA546,0x5B52BA,0x06D24E,0x0ADA42,0x355B37,
	0x09374B,0x8497C1,0x049753,0x064B48,0x66A53C,0x0EA54F,0x06B244,0x4AB638,0x0AAE4C,0x092E42,
	0x3C9735,0x0C9649,0x7D4ABD,0x0D4A51,0x0DA545,0x55AABA,0x056A4E,0x0A6D43,0x452EB7,0x052D4B,
	0x8A95BF,0x0A9553,0x0B4A47,0x6B553B,0x0AD54F,0x055A45,0x4A5D38,0x0A5B4C,0x052B42,0x3A93B6,
	0x069349,0x7729BD,0x06AA51,0x0AD546,0x54DABA,0x04B64E,0x0A5743,0x452738,0x0D264A,0x8E933E,
	0x0D5252,0x0DAA47,0x66B53B,0x056D4F,0x04AE45,0x4A4EB9,0x0A4D4C,0x0D1541,0x2D92B5
]


year = 2014; month = 10; day = 27
NL = [year, 0, 0]
ISR = False



tmp	 = bin(DB[year - 1901]).replace("0b", "")
while len(tmp) < 24:
	tmp = "0" + tmp

data = [
	int(tmp[19:], 2), 		#阳历春节天
	int(tmp[17:19], 2),		#阳历春节月
	int(tmp[0:4], 2),		#闰月月份
	tmp[4:17]				#大小月列表
]
if (data[1] > month) or ((data[0] > day) and (data[1] == month)):
	tmp	 = bin(DB[year - 1902]).replace("0b", "")
	while len(tmp) < 24:
		tmp = "0" + tmp
	data = [
		int(tmp[19:], 2), 		#阳历春节天
		int(tmp[17:19], 2),		#阳历春节月
		int(tmp[0:4], 2),		#闰月月份
		tmp[4:17]				#大小月列表
	]
	NL[0] = year - 1


if (NL[0] % 4 == 0) and (NL[0] % 100 != 0):
	ISR = True
elif (NL[0] % 400 == 0):
	ISR = True

if data[2]:
	NM[0].insert(data[2], NM[1][data[2] - 1])


#计算天数差
days = 0

if NL[0] < year:

	i = 12
	while i > data[1]:
		if i in [1, 3, 5, 7, 8, 10, 12]:
			days += 31

		elif i in [4, 6, 9, 11]:
			days += 30

		else:
			if ISR:
				days += 29

			else:
				days += 28
		i -= 1


	i = 0
	while month > i:

		if i in [1, 3, 5, 7, 8, 10, 12]:
			days += 31

		elif i in [4, 6, 9, 11]:
			days += 30

		elif i == 2:
			if ISR:
				days += 29
			else:
				days += 28
		i += 1

else:
	i = month
	while i > data[1]:
		i -= 1
		if i == data[1]:
			break
		if i in [1, 3, 5, 7, 8, 10, 12]:
			days += 31

		elif i in [4, 6, 9, 11]:
			days += 30

		elif i == 2:
			if ISR:
				days += 29
			else:
				days += 28

if data[1] == month and NL[0] == year:
	days += day - data[0]

if data[1] != month or NL[0] != year:
	days += day
	if data[1] in [1, 3, 5, 7, 8, 10, 12]:
		days += (31 - data[0])
	elif data[1] in [4, 6, 9, 11]:
		days += (30 - data[0])
	elif data[1] == 2 and ISR:
		days += (29 - data[0])

	elif data[1] == 2 and not ISR:
		days += (28 - data[0])

i = 0

while i < days:
	NL[2] += 1
	if ((NL[1] - 1) == data[2]) and data[2]:
		if int(data[3][NL[1]]) and (NL[2] == 30):
			NL[1] += 1
			NL[2] = 0
		elif not int(data[3][NL[1]]) and (NL[2] == 29):
			NL[1] += 1
			NL[2] = 0

	elif int(data[3][NL[1]]) and (NL[2] == 30):
		NL[1] += 1
		NL[2] = 0
	elif not int(data[3][NL[1]]) and (NL[2] == 29):
		NL[1] += 1
		NL[2] = 0
	i += 1
# print(data[2])
# print(data)
print(NL[0], NM[0][NL[1]], ND[NL[2]])
