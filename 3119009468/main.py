import jieba
import gensim
import re

# 删除无效字符和标点符号
def delete(str):
    a = re.sub("[的了呢啊哦嗯吧在]", '', str)
    a = re.sub("[：+—()?【】“”！，。？、~@#￥%…&*（）]", '', a)
    return a

# jieba分词
def turn_to_vector(str):
    result = jieba.lcut(str)
    return result

# 传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def order_similarity(text1,text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    content = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', content, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    result = similarity[test_corpus_1][1]
    return result

# 主函数
def main():
    path_1 = input("参考论文的绝对路径：")
    path_2 = input("待检察文件的绝对路径：")
    f1 = open(path_1, 'r', encoding='UTF-8')
    f2 = open(path_2, 'r', encoding='UTF-8')
    str1 = f1.read()
    str2 = f2.read()
    delete1 = delete(str1)
    delete2 = delete(str2)
    text1 = turn_to_vector(delete1)
    text2 = turn_to_vector(delete2)
    result = order_similarity(text1, text2)
    print("文章相似度： %.4f"%result)

if __name__ == '__main__':
    main()