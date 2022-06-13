
if __name__ == '__main__':
    s = '''
    A large data corpus3
is constructed to facilitate the investigation of answer understanding in reverse QA. The experimental
results indicate that the AntNet is significantly better than the
competing methods.
Our contributions are summarized as follows:
• An under-explored natural language understanding task,
namely, answer understanding in reverse QA, is investigated. To our knowledge, this is the first work that focuses
on this task.
• A new data corpus is compiled and publicly available for
interesting readers.
• A novel AntNet is proposed. The network consists of
three key modules, including skeleton extraction for
questions, relevance-aware representation of answers, and
multi-hop based fusion and significantly outperforms
existing methods in the experiments.
II. RELATED WORK
QA and Reverse QA are firstly reviewed. The NLP for
answer analysis is reviewed latter as this study also aims to
analyze answer texts. Our proposed methodology is inspired
by aspect-based sentiment analysis (ABSA), so ABSA is also
reviewed.
A. Question answering (QA)
QA is a crucial task that depends on natural language
understanding and domain knowledge [3]. QA aims to return
an appropriate answer to a user’s question. The answer is
usually selected from an answer corpus on the basis of a
question-answer matching model. The model calculates the
matching score between the question and each candidate
answer. The answer with the highest matching score is then
used to return to users.
In traditional QA methods, features of questions and answers are extracted by conventional methods, like tf-idf [8],
lexical cues [9], word order [10] and so on. Thereafter, a
similarity scoring function, such as cosine, is used to calculate
the matching score.
In deep QA methods, features of questions and answers are
extracted by deep learning methods, like convolutional neural
network (CNN) [11], LSTM [12], or Transformer [7]. An endto-end framework is usually used to combine the deep feature
extraction and the successive matching function training [13],
[14].
B. Reverse QA
In addition to meet users’ information requirements, machines in some real applications, such as telephone survey
and commercial intelligent customer service systems, are also
required to actively acquire the exact needs or feedbacks of
users [15]. Accordingly, machines may choose to proactively
raise questions to users and then analyze their answers. In
other words, machines are the questioners and humans are the
answerers. This process is a reverse of the conventional QA
process and is called reverse QA in this paper. Fig. 2 shows
the conventional QA and reverse QA processes.
3https://github.com/NlpResearch/AntNet-rverseQA
Fig. 2. The difference between conventional QA (a) and reverse QA (b).
In fact, although reverse QA is not explicitly described
in previous literature, it has been referred in various studies
especially in human-machine dialog [16]. Liu et al. [17]
utilized a bidirectional LSTM (BiLSTM) to encode machine’s
questions and user’s answers to a continuous representation in
an end-to-end task oriented dialogue system. Similarly, Zhang
et al. [18] take a question-answer pair as the input of slot-value
memory and external memory module. Furthermore, Westion
[19] improved machine’s ability to learn from the human’s
feedback by introducing forward prediction (FP) that learns
by predicting textual feedback.
C. NLP for answer texts
Existing NLP studies for answer texts are mainly about
question generation and answer retrieval.
In question generation, early work tackled question generation with a rule-based approach [20] or an overgenerateand-rank approach [21] which relied heavily on well-designed
rules or manually crafted features respectively. To overcome
these limitations, Du et al. [22] introduced a deep sequenceto-sequence learning approach to generate questions. Rao et
al. [23] introduced Generative Adversarial Networks (GANs)
to generate questions that are more useful and specific to the
context.
Compared with typical document retrieval, the answer retrieval model needs to exploit more semantic information.
Inspired by the advantage of translation in modeling the
relationship between words, Xue et al. [24] used a translationbased approach to solve the problem of mismatching. Subsequently, popular neural networks like CNN [25] and LSTM
[26] were used in this task. Tay et al. [27] proposed a recurrent
network using temporal gates to learn interactions between
question-answer pairs.
In this study, answer understanding is transformed into an
answer classification task. Fig. 3 shows the main difference
between answer retrieval in QA and answer classification in
reverse QA. In QA, answer selection relies on a matching
model between a given human question and candidate answers,
whereas, in reverse QA, answer classification relies on a model
that classifies the answer into one of the predefined categories.
The difference between answer-processing tasks for QA and
reverse QA is quite evident.
Our early proposed network, semi-interactive attention network (Semi-IAN) [4], is based on an ABSA network called
interactive attention network (IAN). A data corpus is compiled
to verify the effectiveness of Semi-IAN. On the basis of
this early work, this study compiles a larger data corpus and
proposes a more effective network to capture the dependency
between machine questions and human answers.
    '''
    print(s.replace('\n', ' '))