# encoding=utf-8
import jieba
import jieba.analyse
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from gensim.test.utils import datapath

num_topics = 5
num_topic_terms = 15

texts = []
file = open('/Users/wanghaoxian/Desktop/数据大赛/title.txt')
for line in file:
    #seg_list = jieba.cut(line, cut_all=True)
    seg_list = jieba.analyse.extract_tags(line, topK=40,withWeight=True)
    words = []
    for word,w in seg_list:
        if(len(word)<2):
            continue
        words.append(word.encode('utf-8'))
    texts.append(words)

# Create a corpus from a list of texts
common_dictionary = Dictionary(texts)
common_corpus = [common_dictionary.doc2bow(text) for text in texts]

# Train the model on the corpus.
lda = LdaModel(common_corpus, num_topics=num_topics)

temp_file = datapath("/Users/wanghaoxian/Documents/GitHub/recommend/dataContest/model")
lda.save(temp_file)
documentTopics = lda.get_document_topics(common_corpus)


for doc in documentTopics:
    print doc

for i in range(0,num_topics,1):
    print "topic",i
    terms = lda.get_topic_terms(i,num_topic_terms)
    for term in terms:
        print common_dictionary[term[0]],term[1]
