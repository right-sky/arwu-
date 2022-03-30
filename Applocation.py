import requests
import re
import os
import pandas as pd
#导入必要的包

dir_path = "data/"
if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
    os.makedirs(dir_path)
#创建根目录data和文件dir_path（后面要用到（前面加一个判断条件方便反复测试

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
#U-A伪装

def arwu_year_data(year="2003"):
    url = f"https://www.shanghairanking.cn/api/pub/v1/arwu/rank?year={year}"
    #f把{}的字符串格式化
    resp = requests.get(url, headers=headers)
    #发送get请求返回给resp
    resp.encoding = 'utf-8'
    #设置编码格式为utf-8
    data = resp.json()
    results = {
        "排名": [],
        "学校名称": [],
        "国家/地区": [],
        "国家/地区 排名": [],
        "总分": [],
        "校友获奖": [],
    }
    inds = {_['nameCn']: _['code'] for _ in data['data']['inds']}
    for r in data['data']['rankings'][:100]:
        results['排名'].append(r['ranking'])
        results['学校名称'].append(r['univNameCn'])
        results['国家/地区'].append(r['region'])
        results['国家/地区 排名'].append(r['regionRanking'])
        results['总分'].append(r['score'])
        # 筛选出前100名的学校并把参数和对应的数据连接起来并返回给results
        if "校友获奖" in inds:
            results['校友获奖'].append(r['indData'].get(inds['校友获奖'], "0"))
        else:
            results['校友获奖'].append('')
    return results
    # 筛选出前100名的学校并把参数和对应的数据连接起来，但是这个地方用postman解析过json之后发现校友获奖这一栏在一个叫inds二级目录里，所以这里加一个判断条件把这个数据单独对应出来
#def的这个函数用来获取学术的排名

def get_all_sub():
    base_str = """{
                code: "RS01",
                nameCn: "理学",
                weight: a,
                color: "#C62C2C",
                subjs: [{
                    code: "RS0101",
                    nameCn: "数学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0102",
                    nameCn: "物理学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0103",
                    nameCn: "化学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0104",
                    nameCn: "地球科学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0105",
                    nameCn: "地理学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0106",
                    nameCn: "生态学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0107",
                    nameCn: "海洋科学",
                    weight: a,
                    years: [i, j, g, k]
                }, {
                    code: "RS0108",
                    nameCn: "大气科学",
                    weight: a,
                    years: [i, j, g, k]
                }]
            }, {
                code: "RS02",
                nameCn: "工学",
                weight: a,
                color: "#629E46",
                subjs: [{
                    code: "RS0201",
                    nameCn: "机械工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0202",
                    nameCn: "电力电子工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0205",
                    nameCn: "控制科学与工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0206",
                    nameCn: "通信工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0207",
                    nameCn: "仪器科学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0208",
                    nameCn: "生物医学工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0210",
                    nameCn: "计算机科学与工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0211",
                    nameCn: "土木工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0212",
                    nameCn: "化学工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0213",
                    nameCn: "材料科学与工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0214",
                    nameCn: "纳米科学与技术",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0215",
                    nameCn: "能源科学与工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0216",
                    nameCn: "环境科学与工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0217",
                    nameCn: "水资源工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0219",
                    nameCn: "食品科学与工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0220",
                    nameCn: "生物工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0221",
                    nameCn: "航空航天工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0222",
                    nameCn: "船舶与海洋工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0223",
                    nameCn: "交通运输工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0224",
                    nameCn: "遥感技术",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0226",
                    nameCn: "矿业工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0227",
                    nameCn: "冶金工程",
                    weight: a,
                    years: [l, i, j, g, k]
                }]
            }, {
                code: "RS03",
                nameCn: "生命科学",
                weight: a,
                color: "#EF8322",
                subjs: [{
                    code: "RS0301",
                    nameCn: "生物学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0302",
                    nameCn: "基础医学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0303",
                    nameCn: "农学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0304",
                    nameCn: "兽医学",
                    weight: a,
                    years: [l, i, j, g, k]
                }]
            }, {
                code: "RS04",
                nameCn: "医学",
                weight: a,
                color: "#47AFE2",
                subjs: [{
                    code: "RS0401",
                    nameCn: "临床医学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0402",
                    nameCn: "公共卫生",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0403",
                    nameCn: "口腔医学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0404",
                    nameCn: "护理学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0405",
                    nameCn: "医学技术",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0406",
                    nameCn: "药学",
                    weight: a,
                    years: [l, i, j, g, k]
                }]
            }, {
                code: "RS05",
                nameCn: "社会科学",
                weight: a,
                color: "#9D68AA",
                subjs: [{
                    code: "RS0501",
                    nameCn: "经济学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0502",
                    nameCn: "统计学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0503",
                    nameCn: "法学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0504",
                    nameCn: "政治学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0505",
                    nameCn: "社会学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0506",
                    nameCn: "教育学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0507",
                    nameCn: "新闻传播学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0508",
                    nameCn: "心理学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0509",
                    nameCn: "工商管理",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0510",
                    nameCn: "金融学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0511",
                    nameCn: "管理学",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0512",
                    nameCn: "公共管理",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0513",
                    nameCn: "旅游休闲管理",
                    weight: a,
                    years: [l, i, j, g, k]
                }, {
                    code: "RS0515",
                    nameCn: "图书情报科学",
                    weight: a,
                    years: [l, i, j, g, k]
                }]
            }]
        }"""
    sub_id = re.findall('code\: \"(.*?)\"', base_str, re.S)
    sub_name = re.findall('nameCn\: \"(.*?)\"', base_str, re.S)
    #这里用正则筛选出刚才base_str中学校的code和nameCn，并且需要吧flags设置成包括换行在内的所有字符
    items = []
    for sub, name in zip(sub_id, sub_name):
        #id和name返回成列表
        if len(sub) > 4:
            item = {"id": sub, "name": name}
            items.append(item)
            #循环获得所有的ID和name并且返回给items
    return items
#def的这个函数用来获取全部的学科名称

def gras_rank_year(subid, year):
    url = f"https://www.shanghairanking.cn/api/pub/v1/gras/rank?year={year}&subj_code={subid}"
    #经典字符串格式化（划掉
    resp = requests.get(url, headers=headers)
    #抓包并且分析json发现都是get的请求，所以用get获取数据
    data = resp.json()
    results = {
        "排名": [],
        "学校名称": [],
        "国家/地区": [],
        "总分": [],
        "重要期刊论文数": [],
    }
    inds = {_['nameCn']: _['code'] for _ in data['data']['inds']}
    for r in data['data']['rankings'][:100]:
        results['排名'].append(r['ranking'])
        results['学校名称'].append(r['univNameCn'])
        results['国家/地区'].append(r['region'])
        results['总分'].append(r['score'])
        #筛选ranking为前一百的所有数据并把发生的数据返回给results里的对应栏
        if "重要期刊论文数" in inds:
            results['重要期刊论文数'].append(r['indData'].get(inds['重要期刊论文数'], "0"))
        else:
            results['重要期刊论文数'].append('')
            #和刚才获取学术排名时一样，这里也有二级目录，多写个if判断下这里存不存在数据并且重复刚才操作
    return results
#这个函数用来获取学科排名

def get_num(s):
    s = s.split("-")[0]
    return int(s)
#分离一下字符串( ﾟ∀。)

if __name__ == '__main__':
    all_sub = get_all_sub()
    begin_year = 2003
    #定义一个开始爬取年份
    while begin_year <= 2021:
        #意为结束爬取年份2021
        cur_dir = os.path.join(dir_path, str(begin_year))
        #拼接文件的路径
        if not os.path.exists(cur_dir):
            os.makedirs(cur_dir)
            #创建cur_dir
        if begin_year >= 2017:
            #这里因为经过粗略观察发现2017年以前没有学科排名的数据，为了节约运行资源就让他从2017年开始爬了（
            for sub in all_sub:
                cur_data = gras_rank_year(sub['id'], begin_year)
                cur_filename = os.path.join(cur_dir, sub['name'] + ".csv")
                pd.DataFrame(cur_data).to_csv(cur_filename, index=False)
                #学科排名数据保存为csv
        us_data = arwu_year_data(str(begin_year))
        cur_filename = os.path.join(cur_dir, "学术排名.csv")
        pd.DataFrame(us_data).to_csv(cur_filename, index=False)
        #学术排名保存csv
        begin_year += 1
    #用while循环重复完成固定操作
print('欧耶完成咯！')
