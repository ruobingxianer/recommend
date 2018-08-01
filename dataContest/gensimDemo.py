from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel
from gensim.test.utils import datapath

num_topics = 4
# Create a corpus from a list of texts
common_dictionary = Dictionary(common_texts)
common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]

print common_dictionary.items()
# Train the model on the corpus.
lda = LdaModel(common_corpus, num_topics=num_topics)

temp_file = datapath("/Users/wanghaoxian/Documents/GitHub/recommend/dataContest/model")
lda.save(temp_file)
list = lda.get_document_topics(common_corpus)

for topic in list:
    print topic
for i in range(0,num_topics,1):
    print i,lda.get_topic_terms(i,3)
