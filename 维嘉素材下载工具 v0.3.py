import urllib.request
from easygui import buttonbox, msgbox, ccbox
import os

"""————————————————————全是屎山代码，别介意，能用就行！————————————————————"""
""" 0.3版本 """

language = ccbox("选择使用维嘉素材下载器时的语言：", "选择", ["English", "Chinese"])

zh_cn = ["选择你要下载的维嘉素材", "维嘉素材下载工具", ["维嘉.png", "维嘉.jpg", "维嘉.webp", "维嘉.gif", "维嘉.ico",
                                                        "维嘉（ai生成视频）.mp4",
                                                        "维嘉（ai生成视频）.gif", "全套下载"], "维嘉素材",
         "维嘉AI生成视频{}s.mp4",
         "维嘉AI生成视频{}s.gif",
         "请选择AI生成视频的秒数（秒数不同视频也不同）",
         "文件已下载完成，已为您打开，在程序的路径（{}）下可以找到它！本程序作者李子恒，感谢使用ヾ(≧▽≦*)o", "提示", "维嘉，我来了！"

         ]
en_us = ["Select the Weijia footage you want to download",
         "ChenweijiaImageDownloaderTool",
         ["Weijia.png", "Weijia.jpg", "Weijia.webp",
          "Weijia.gif", "Weijia.ico",
          "Weijia（AI-generated videos）.mp4",
          "Weijia（AI-generated videos）.gif", "Download all"], "Weijia_Pictures",
         "Weijia AI generates video {}s.mp4", "Weijia AI generates video {}s.gif",

         "Please select the number of seconds for the AI-generated video "
         "(the video will be different for different number of seconds)",

         "The file has been downloaded successfully, 和 it has been opened for you. You can find it in the program's "
         "path ({}). The author of this program is Li Ziheng. Thank you for using it.", "Tip", "Weijia, I'm coming!"]

if language:
    language = en_us
else:
    language = zh_cn
# 下载网址
url = {language[2][3]:
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/c/c7/Weijia.gif/revision/latest?cb="
           "20240921125335&path-prefix=zh",
       language[2][1]:
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/e/eb/Weijia.jpg/revision/latest?cb="
           "20240921130335&path-prefix=zh",
       language[2][0]:
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/1/14/Weijia.png/revision/latest?cb="
           "20240921131715&path-prefix=zh",
       language[2][2]:
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/8/81/Weijia.webp/revision/latest?cb="
           "20240921131923&path-prefix=zh",
       language[2][4]:
           "https://static.wikia.nocookie.net/carambola1437warehouse/images/0/03/Weijia.ico/revision/latest?cb="
           "20240921132143&path-prefix=zh"
       }
url_ai_mp4 = {
    language[4].format("3"):
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/c/cf"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%913s.mp4/revision/latest?cb="
        "20240921132625&path-prefix=zh",
    language[4].format("6"):
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/6/6e"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%916s.mp4/revision/latest?cb="
        "20240921132807&path-prefix=zh",
    language[4].format("9"):
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/e/e8"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%919s.mp4/revision/latest?cb="
        "20240921132918&path-prefix=zh",
    language[4].format("12"):
        "https://static.wikia.nocookie.net/carambola1437warehouse/images/4/41"
        "/%E7%BB%B4%E5%98%89AI%E7%94%9F%E6%88%90%E8%A7%86%E9%A2%9112s.mp4/revision/latest?cb="
        "20240921133625&path-prefix=zh"
}
url_ai_gif = {
    language[5].format("3"): "https://github.com/1437Carambola/Carambola1437v/releases/download/weijia_ai_gif/AI.3s.gif"
    ,
    language[5].format("6"): "https://github.com/1437Carambola/Carambola1437v/releases/download/weijia_ai_gif/AI.6s.gif"
    ,
    language[5].format("9"): "https://github.com/1437Carambola/Carambola1437v/releases/download/weijia_ai_gif/AI.9s.gif"
    ,
    language[5].format("12"): "https://github.com/1437Carambola/Carambola1437v/releases/download/weijia_ai_gif/"
                              "AI.12s.gif"
}

pic = buttonbox(language[0], language[1], language[2])

PIC_ALL = ("https://github.com/Carambola1437/ChenweijiaImageDownloaderTool"
           "/releases/download/%E5%85%A8%E5%A5%97%E7%B4%A0%E6%9D%90%E5%8C%85/default.zip")
# 判断文件夹是否存在
try:
    os.mkdir(language[3])
except FileExistsError:
    pass
pic_path = f"{language[3]}/{pic}"
# 请求
# opener = urllib.request.build_opener()
# opener.addheaders = [('Referer', "https://static.wikia.nocookie.net")]
# urllib.request.install_opener(opener)
if pic == language[2][5]:
    pic = buttonbox(language[6], language[1],
                    [language[4].format("3"), language[4].format("6"), language[4].format("9"),
                     language[4].format("12")])
    # 下载
    urllib.request.urlretrieve(url_ai_mp4[pic], pic_path)
elif pic == language[2][6]:
    pic = buttonbox(language[6], language[1],
                    [language[5].format("3"), language[5].format("6"), language[5].format("9"),
                     language[5].format("12")])
    # 下载
    urllib.request.urlretrieve(url_ai_gif[pic], pic_path)
elif pic == language[2][-1]:
    urllib.request.urlretrieve(PIC_ALL, f"{language[3]}/维嘉全套素材.zip")
else:
    # 下载
    try:
        urllib.request.urlretrieve(url[pic], pic_path)
    except KeyError:
        pass
# 显示文件
os.startfile(language[3])
path_abs = os.path.abspath(language[3])
msgbox(language[7].format(path_abs), language[8], language[9])
