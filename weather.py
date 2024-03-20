import requests

# 根据「城市名称」获取对应的「城市编码」
def get_weather(city):
      city_code = get_city_code(city)
      r = requests.get(f'http://www.weather.com.cn/data/sk/{city_code}.html')
      r.encoding = 'utf-8'  
      weatherinfo = r.json()['weatherinfo']
      return f"城市:{weatherinfo.get('city')}\n温度:{weatherinfo.get('temp')}\n风向:{weatherinfo.get('WD')}\n风力:{weatherinfo.get('WS')}\n湿度:{weatherinfo.get('SD')}"


def get_city_code(city_name):
    # 读取城市编码表文件
    with open('城市代码.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()  # 每行记录代表一个城市，例如：101010100-beijing-北京

    # 遍历每一行（每个城市）
    for line in lines:
        if city_name in line:  # 如果该行包含城市名称
            return line[:9]    # 返回前9个城市编码字符
