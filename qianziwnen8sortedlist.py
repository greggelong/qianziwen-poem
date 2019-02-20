import collections
import pprint
from natsort import natsorted 



hsk1=set('起 果 热 院 四 回 西 国 高 怎 系 北 一 七 三 上 下 不 东 子 医 字 个 十 中 午 气 学 么 开 水 九 习 书 汉 雨 买 见 视 零 觉 了 二 在 五 些 生 坐 电 块 影 很 校 客 样 家 桌 去 京 亮 想 友 人 没 什 对 今 叫 他 们 面 候 苹 做 小 少 吃 同 名 后 吗 听 会 爱 爸 租 呢 住 岁 作 你 和 茶 椅 的 车 站 那 钟 哪 狗 认 识 话 日 都 语 时 菜 说 请 读 儿 先 钱 我 八 六 老 关 兴 这 再 写 打 商 猫 谁 明 星 昨 飞 谢 是 喂 多 喜 喝 大 天 冷 看 太 几 出 女 她 好 睡 妈 工 现 衣 能 里 分 饭 馆 姐 前 欢 师 脑 火 漂 月 有 朋 服 年 期 本 米 店 机 来 杯 点')
qianziwen = '天地玄黄 宇宙洪荒 日月盈昃 辰宿列张 寒来暑往 秋收冬藏 闰馀成岁 律吕调阳 云腾致雨 露结为霜 金生丽水 玉出昆冈 剑号巨阙 珠称夜光 果珍李柰 菜重芥姜 海咸河淡 鳞潜羽翔 龙师火帝 鸟官人皇 始制文字 乃服衣裳 推位让国 有虞陶唐 吊民伐罪 周发殷汤 坐朝问道 垂拱平章 爱育黎首 臣伏戎羌 遐迩一体 率宾归王 鸣凤在竹 白驹食场 化被草木 赖及万方 盖此身发 四大五常 恭惟鞠养 岂敢毁伤 女慕贞洁 男效才良 知过必改 得能莫忘 罔谈彼短 靡恃己长 信使可复 器欲难量 墨悲丝染 诗赞羔羊 景行维贤 克念作圣 德建名立 形端表正 空谷传声 虚堂习听 祸因恶积 福缘善庆 尺璧非宝 寸阴是竞 资父事君 曰严与敬 孝当竭力 忠则尽命 临深履薄 夙兴温凊 似兰斯馨 如松之盛 川流不息 渊澄取映 容止若思 言辞安定 笃初诚美 慎终宜令 荣业所基 籍甚无竟 学优登仕 摄职从政 存以甘棠 去而益咏 乐殊贵贱 礼别尊卑 上和下睦 夫唱妇随 外受傅训 入奉母仪 诸姑伯叔 犹子比儿 孔怀兄弟 同气连枝 交友投分 切磨箴规 仁慈隐恻 造次弗离 节义廉退 颠沛匪亏 性静情逸 心动神疲 守真志满 逐物意移 坚持雅操 好爵自縻 都邑华夏 东西二京 背邙面洛 浮渭据泾 宫殿盘郁 楼观飞惊 图写禽兽 画彩仙灵 丙舍傍启 甲帐对楹 肆筵设席 鼓瑟吹笙 升阶纳陛 弁转疑星 右通广内 左达承明 既集坟典 亦聚群英 杜稿钟隶 漆书壁经 府罗将相 路侠槐卿 户封八县 家给千兵 高冠陪辇 驱毂振缨 世禄侈富 车驾肥轻 策功茂实 勒碑刻铭 磻溪伊尹 佐时阿衡 奄宅曲阜 微旦孰营 桓公匡合 济弱扶倾 绮回汉惠 说感武丁 俊乂密勿 多士寔宁 晋楚更霸 赵魏困横 假途灭虢 践土会盟 何遵约法 韩弊烦刑 起翦颇牧 用军最精 宣威沙漠 驰誉丹青 九州禹迹 百郡秦并 岳宗泰岱 禅主云亭 雁门紫塞 鸡田赤城 昆池碣石 钜野洞庭 旷远绵邈 岩岫杳冥 治本于农 务兹稼穑 俶载南亩 我艺黍稷 税熟贡新 劝赏黜陟 孟轲敦素 史鱼秉直 庶几中庸 劳谦谨敕 聆音察理 鉴貌辨色 贻厥嘉猷 勉其祗植 省躬讥诫 宠增抗极 殆辱近耻 林皋幸即 两疏见机 解组谁逼 索居闲处 沉默寂寥 求古寻论 散虑逍遥 欣奏累遣 戚谢欢招 渠荷的历 园莽抽条 枇杷晚翠 梧桐蚤凋 陈根委翳 落叶飘摇 游鹍独运 凌摩绛霄 耽读玩市 寓目囊箱 易輶攸畏 属耳垣墙 具膳餐饭 适口充肠 饱饫烹宰 饥厌糟糠 亲戚故旧 老少异粮 妾御绩纺 侍巾帷房 纨扇圆絜 银烛炜煌 昼眠夕寐 蓝笋象床 弦歌酒宴 接杯举觞 矫手顿足 悦豫且康 嫡后嗣续 祭祀烝尝 稽颡再拜 悚惧恐惶 笺牒简要 顾答审详 骸垢想浴 执热愿凉 驴骡犊特 骇跃超骧 诛斩贼盗 捕获叛亡 布射僚丸 嵇琴阮啸 恬笔伦纸 钧巧任钓 释纷利俗 竝皆佳妙 毛施淑姿 工颦妍笑 年矢每催 曦晖朗曜 璇玑悬斡 晦魄环照 指薪修祜 永绥吉劭 矩步引领 俯仰廊庙 束带矜庄 徘徊瞻眺 孤陋寡闻 愚蒙等诮 谓语助者 焉哉乎也'
qianziwenclean = qianziwen.replace(" ","")
found=hsk1.intersection(set(qianziwenclean))
print(len(found),found)
print(len(hsk1))
print(len(qianziwenclean))
print(len(set(qianziwenclean)))
print(996/4)

freq = collections.Counter(qianziwenclean)
for k in freq:
    if freq[k]>1:
        print (k)
        
        
def find_dup(stringtext):
    seen = set()
    seen2time = []
    
     
    for idx, character in enumerate(stringtext):  # using enumerate to get the index
        print(idx, character)
        if character not in seen:
            seen.add(character)
            
        else:
            #seen2time.append(character+str(idx))
            seen2time.append(character) #stuck the index on as a string so I could see it
            print("duplicate character", character)
            
    return seen2time



def numtex(stringtext):
    indexedtext={}
    for idx, character in enumerate(stringtext):
        indexedtext[idx+1]=character
        print(idx+1,character)
    return indexedtext
        
duplist = find_dup(qianziwenclean)
print(duplist)  
qiandic =(numtex(qianziwenclean)) 
pprint.pprint(qiandic)   
print(qiandic[5])

for item in duplist:
    
    print([k for k,v in qiandic.items() if v == item], item) # list comprehension to look up multiple keys for same value

hsk_in_qian_idx=[]
for char in found:
    idx=[k for k,v in qiandic.items() if v == char]
    hsk_in_qian_idx.append(idx)
    hsk_in_qian_idx.append(char)
pprint.pprint(hsk_in_qian_idx)
print(len(hsk_in_qian_idx))

#print out orderd list of hsk1 characters in qianziwen order
hsk_in_qian_idx2=[]
for char in found:
    idx=[k for k,v in qiandic.items() if v == char]
    orderadd = str(idx)+" "+char
    hsk_in_qian_idx2.append(orderadd)
     
pprint.pprint(hsk_in_qian_idx2)
print(len(hsk_in_qian_idx))
# that didnt work so lets try agin with a dictionay with keys as 
hsk_in_qian_idx2=[]
for char in found:
    idx=[k for k,v in qiandic.items() if v == char]
    orderadd = str(idx[0])+"_"+char
    hsk_in_qian_idx2.append(orderadd)
     
pprint.pprint(hsk_in_qian_idx2)
print(len(hsk_in_qian_idx))

#using the imported third part lib natsort !!!! to sort the list
hskqiansort = natsorted(hsk_in_qian_idx2, key =lambda y: y.lower())

print(hskqiansort)