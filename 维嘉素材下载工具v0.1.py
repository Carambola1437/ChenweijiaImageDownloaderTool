import urllib.request
from easygui import buttonbox, msgbox
import os
# 下载网址
url = {"维嘉.gif":
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/c/c7/Weijia.gif/revision/latest?cb="
           "20240921125335&path-prefix=zh",
       "维嘉.jpg":
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/e/eb/Weijia.jpg/revision/latest?cb="
           "20240921130335&path-prefix=zh",
       "维嘉.png":
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/1/14/Weijia.png/revision/latest?cb="
           "20240921131715&path-prefix=zh",
       "维嘉.webp":
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/8/81/Weijia.webp/revision/latest?cb="
           "20240921131923&path-prefix=zh",
       "维嘉.ico":
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/0/03/Weijia.ico/revision/latest?cb="
           "20240921132143&path-prefix=zh"
       }
url_ai_mp4 = {
    "维嘉AI生成视频3s.mp4":
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/c/cf"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%913s.mp4/revision/latest?cb="
        "20240921132625&path-prefix=zh",
    "维嘉AI生成视频6s.mp4":
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/6/6e"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%916s.mp4/revision/latest?cb="
        "20240921132807&path-prefix=zh",
    "维嘉AI生成视频9s.mp4":
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/e/e8"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%919s.mp4/revision/latest?cb="
        "20240921132918&path-prefix=zh",
    "维嘉AI生成视频12s.mp4":
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/4/41"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%9112s.mp4/revision/latest?cb="
        "20240921133625&path-prefix=zh"
}
url_ai_gif = {
    "维嘉AI生成视频3s.gif": "https://4key.cn/goY",
    "维嘉AI生成视频6s.gif": "https://4key.cn/vHQ",
    "维嘉AI生成视频9s.gif": "https://4key.cn/OYS",
    "维嘉AI生成视频12s.gif": "https://4key.cn/kOC"
}
pic = buttonbox("选择你要下载的维嘉素材", "维嘉素材下载工具",
                ["维嘉.png", "维嘉.jpg", "维嘉.webp", "维嘉.gif", "维嘉.ico", "维嘉（ai生成视频）.mp4",
                 "维嘉（ai生成视频）.gif", "全套下载（暂未开放）"])
# 判断文件夹是否存在
try:
    os.mkdir("维嘉素材")
except FileExistsError:
    pass
pic_path = f"维嘉素材/{pic}"
# 请求
# opener = urllib.request.build_opener()
# opener.addheaders = [('Referer', "https://static.wikia.nocookie.net")]
# urllib.request.install_opener(opener)
if pic == "维嘉（ai生成视频）.mp4":
    pic = buttonbox("请选择AI生成视频的秒数（秒数不同视频也不同）", "维嘉素材下载工具",
                    ["维嘉AI生成视频3s.mp4", "维嘉AI生成视频6s.mp4", "维嘉AI生成视频9s.mp4", "维嘉AI生成视频12s.mp4"])
    # 下载
    urllib.request.urlretrieve(url_ai_mp4[pic], pic_path)
elif pic == '维嘉（ai生成视频）.gif':
    pic = buttonbox("请选择AI生成视频的秒数（秒数不同视频也不同）", "维嘉素材下载工具",
                    ["维嘉AI生成视频3s.gif", "维嘉AI生成视频6s.gif", "维嘉AI生成视频9s.gif", "维嘉AI生成视频12s.gif"])
    # 下载
    urllib.request.urlretrieve(url_ai_gif[pic], pic_path)
else:
    # 下载
    try:
        urllib.request.urlretrieve(url[pic], pic_path)
    except KeyError:
        pass
# 显示文件
os.startfile("维嘉素材")
path_abs = os.path.abspath("./维嘉素材")
msgbox(f"文件已下载完成，已为您打开，在程序的路径（{path_abs}）下可以找到它！本程序作者李子恒，感谢使用ヾ(≧▽≦*)o", "提示",
       "维嘉，我来了！")
