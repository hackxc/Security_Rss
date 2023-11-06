import requests,re
from flask import Flask,render_template
from fake_useragent import UserAgent
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, static_folder='static')
app.config['SERVER_NAME'] = 'localhost:8001' #设置地址，如果是ip请设置ip
app.config['APPLICATION_ROOT'] = '/'
app.config['PREFERRED_URL_SCHEME'] = 'http'
scheduler = BackgroundScheduler()
@app.route('/')

def generate_new_body():
    with app.app_context():
        with open("./rss_hackxc/xianzhi.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body1 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/freebuf.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body2 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/t00ls.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body3 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/butian.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body4 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/weixin.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body5 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/huoxian.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body6 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/changting.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body7 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/aliyun.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body8 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        with open("./rss_hackxc/nsfocus.txt", "r",encoding='utf-8') as f:
            content = f.readlines()
        body9 = [(line.strip().split(',')[0], line.strip().split(',')[1]) for line in content] #读取文件再放到html

        return render_template('index.html', body1=body1, body2=body2, body3=body3, body4=body4, body5=body5, body6=body6, body7=body7, body8=body8,body9=body9)

def update_page(): # 生成新的网页内容，实现自动更新flask
    xianzhi()  # 先知文章
    freebuf()  # Freebuf文章
    t00ls()    # T00ls文章
    butian()   # 补天文章
    weixin()   # 微信文章
    huoxian()  # 火线文章
    changting()# 长亭漏洞库
    aliyun()   # 阿里云漏洞库
    nsfocus()  # 绿盟漏洞预警

    new_body = generate_new_body()
    # 将新的网页内容更新到网页中
    with app.app_context():
        global body
        body = new_body

def index():
    return body #返回最新网页内容

scheduler.add_job(func=update_page, trigger='interval', seconds=10)
scheduler.start()

def xianzhi():
    url = 'https://xz.aliyun.com/feed'
    response = requests.get(url,headers=headers)
    html = response.text
    #print(response.request.headers['User-Agent'])
    rtitle = r'<entry><title>(.*?)</title><link href="'
    title = re.findall(rtitle, html,re.DOTALL)

    rurl = r'<link href="(.*?)" rel="alternate">'
    url = re.findall(rurl, html,re.DOTALL)

    with open("./rss_hackxc/xianzhi.txt", "w",encoding='utf-8') as f:
        for x, y in zip(url, title):
            f.write(str(x) + ',' + str(y) + '\n')

def freebuf():
    url = 'https://www.freebuf.com/articles/web'
    response = requests.get(url,headers=headers)
    html = response.text
    #print(html)
    #print(response.request.headers['User-Agent'])
    rtitle = r'" target="_blank" class="img-view" data-v-8bdd825c><img alt="(.*?)" style="color:#fff" data-v-8bdd825c> <p data-v-8bdd825c><span class="ant-tag ant-tag-has-color" style="background-color:#262626;opacity:.7;font-size:12px;border-radius:0" data-v-8bdd825c>'
    title = re.findall(rtitle, html,re.DOTALL)

    rurl = r'<div class="item-content" data-v-8bdd825c><a href="(/articles.*?)" target="_blank" class="img-view" data-v-8bdd825c><img alt="'
    url = re.findall(rurl, html,re.DOTALL)
    #print(url[0].strip(),title[0].strip())

    with open('./rss_hackxc/freebuf.txt', 'w',encoding='utf-8') as f:
        for x, y in zip(url, title):
            f.write(str(x) + ',' + str(y) + '\n')

def t00ls():
    url = 'https://i.hacking8.com/forums/'
    response = requests.get(url,headers=headers)
    html = response.text

    rtitle = r'href="https://www.t00ls.com(.*?)" rel="nofollow">(.*?)</a></td>'
    title = re.findall(rtitle, html,re.DOTALL)

    rurl = r'<div class="item-content" data-v-8bdd825c><a href="(/articles.*?)" target="_blank" class="img-view" data-v-8bdd825c><img alt="'
    url = re.findall(rurl, html,re.DOTALL)
    #print(title[0])

    count = 0  # 只写入35条数据
    with open('./rss_hackxc/t00ls.txt', 'w',encoding='utf-8') as f:
        for item in title:
            item = str(item).replace("'", "").replace("(", "").replace(")", "").replace(' ','')#处理格式
            f.write(item.strip()  + '\n')
            count += 1
            if count >= 35:
                break
def butian():
    titles = []
    url = 'https://forum.butian.net/community/all/newest'
    response = requests.get(url,headers=headers)
    html = response.text
    #print(response.request.headers['User-Agent'])
    rtitle = r'data-source-id=".*?"(.*?)</a></h2>'
    title = re.findall(rtitle, html,re.DOTALL)
    for t in title:
        t = t.replace('>', '').strip()
        titles.append(t)
        # print(titles)

    rurl = r'<a.*?href="https://forum.butian.net/share/(\d+)".*?>'
    url = re.findall(rurl, html,re.DOTALL)
    #print(url)

    with open('./rss_hackxc/butian.txt', 'w',encoding='utf-8') as f:
        for x, y in zip(url, titles):
            f.write(str(x) + ',' + str(y) + '\n')

def weixin():
    titles = []
    url = 'http://www.nmd5.com/test/index.php'
    response = requests.get(url, headers=headers)
    html = response.text
    # print(response.request.headers['User-Agent'])
    rtitle = r'<a href="https://mp.weixin.qq.com(.*?)" target="_blank">(.*?)</a>'
    title = re.findall(rtitle, html, re.DOTALL)
    #print(title)

    count = 0  # 只写入28条数据
    with open('./rss_hackxc/weixin.txt', 'w',encoding='utf-8') as f:
        for item in title:
            item = str(item).replace("'", "").replace("(", "").replace(")", "").replace(' ','')#处理格式
            f.write(item.strip()  + '\n')
            count += 1
            if count >= 28:
                break
def huoxian():
    url = 'https://zone.huoxian.cn/?sort=newest'
    response = requests.get(url, headers=headers)
    html = response.text
    # print(response.request.headers['User-Agent'])
    rtitle = r'<a href="https://zone.huoxian.cn/d(.*?)">(.*?)</a>'
    title = re.findall(rtitle, html, re.DOTALL)
    #print(title)
    count = 0  # 删除第一行置顶信息
    with open('./rss_hackxc/huoxian.txt', 'w', encoding='utf-8') as f:
        for t in title:
            t = str(t).strip().replace("'", "").replace("(", "").replace(")", "").replace(' ','').replace('\\n','')
            #print(t)
            if count < 1:
                count += 1
            else:
                f.write(t+"\n")
                count += 1

def changting():
    url = 'https://stack.chaitin.com/api/v2/vuln/list/?limit=25&offset=0&search='
    response = requests.get(url, headers=headers)
    html = response.json()
    html = html['data']['list']

    with open('./rss_hackxc/changting.txt', 'w', encoding='utf-8') as f:
        for item in html:
            f.write(item['id']+","+item['title']+"\n")

def aliyun():
    url = 'https://avd.aliyun.com/'
    response = requests.get(url, headers=headers)
    html = response.text
    rtitle = r'<td>(.*?)</td>'
    title = re.findall(rtitle, html, re.DOTALL)
    #print(title)

    rurl = r'<a href="(.*?)"'
    url = re.findall(rurl, html,re.DOTALL)
    #print(url)

    pairs = zip(url, title)#合并输出
    with open('./rss_hackxc/aliyun.txt', 'w', encoding='utf-8') as f:
        for pair in pairs:
            u, t = pair
            f.write(u+","+t+"\n")

def nsfocus():
    url = 'http://www.nsfocus.net/index.php?act=sec_bug'
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf-8')
    rtitle = r"</span> <a href='(.*?)'>(.*?)</a> <font color=#FF0000>New</font></li>"
    title = re.findall(rtitle, content, re.DOTALL)
    with open('./rss_hackxc/nsfocus.txt', 'w', encoding='utf-8') as f:
        for t in title:
            f.write(t[0]+","+t[1]+"\n")


if __name__ == '__main__':
    headers = {'User-Agent': UserAgent().random}
    xianzhi()  # 先知文章
    freebuf()  # Freebuf文章
    t00ls()  # T00ls文章
    butian()  # 补天文章
    weixin()  # 微信文章
    huoxian()  # 火线文章
    changting()  # 长亭漏洞库
    aliyun()  # 阿里云漏洞库
    nsfocus()  # 绿盟漏洞预警
    generate_new_body()
    app.run(host='0.0.0.0', port=8001)  # 启动Flask应用程序
