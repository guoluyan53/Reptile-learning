from wordcloud import WordCloud
import PIL.Image as image
import jieba
jieba.setLogLevel(jieba.logging.INFO)

#中文停用词
stopwords = set()
content = [line.strip() for line in open('stop.txt','r',encoding='utf-8').readlines()]
stopwords.update(content)


def trans_CN(text):
    word_list = jieba.cut(text)  #分词
    res = " ".join(word_list)
    return res

def xiecheng():
    with open("xiecheng.txt", encoding='utf-8') as fp:
        text = fp.read()
        cut_text = trans_CN(text)
        cloud = WordCloud(
            font_path="HYQiHei-25J.ttf",
            width=1000,
            height=700,
            stopwords=stopwords
        )
        wordcloud = cloud.generate(cut_text)
        image_p = wordcloud.to_image()
        wordcloud.to_file('xieciyun1.jpg')
        image_p.show()

def tongcheng():
    with open("tongcheng.txt", encoding='utf-8') as fp:
        text = fp.read()
        cut_text = trans_CN(text)
        cloud = WordCloud(
            font_path="HYQiHei-25J.ttf", #设置字体，不然会乱码
            width=1000,
            height=700,
            stopwords = stopwords
        )
        wordcloud = cloud.generate(cut_text)
        image_p = wordcloud.to_image()
        wordcloud.to_file('tongciyun1.jpg') #保存图片
        image_p.show() #查看图片

if __name__ == '__main__':
    xiecheng()
    tongcheng()