# Answer with different embeddings.

- all-MiniLM-L6-v2

> Question:
What is the latest news about Messi?

> Answer:
 Lionel Messi's contract with Inter Miami was leaked and shows he will earn significant money in America for several years to come.

> Question:
Did PSV play any matches?

> Answer:
 Yes, it appears that the context suggests there were multiple instances of a club playing another in relation to their participation or performance.

> Question:
Which country does PSV belong to?

> Answer:
 The question is unclear as it doesn't provide any information about which sport or activity the football team belongs in, and hence cannot determine its nationality.


> Question:
Where do you get all the news from?

> Answer:
 I mostly rely on online sources such as articles in newspapers or websites that specialize in sports like AjaxFana


Impression: Faster, Answers are not too bad and relevant

---

- all-mpnet-base-v2

> Question:
hi

> Answer:
 The question is asking for some context about COVID-19, which was caused by SARS and originated in China but then spread globally through various modes of transportation such as air travel between different countries including the United States before spreading worldwide from there to Europe via infected travelers. It also highlights that people were not immune or resistant enough against it when they returned home after traveling abroad until some developed symptoms, which led them back into their homes and ultimately resulted in one death among other health issues experienced by many Americans during this time period (including the use of masks being a key factor for prevention).

> Question:
Did PSV play any matches?

> Answer:
 The question is asking if there were specific games played by PSV, but the answer only states that they competed at various competitions.

> Question:
Which country does PSV belong to?

> Answer:
 There is no specific information given on which club or country PSV belongs, so it's not possible for me to answer that question with certainty without further context.

 > Question:
Where do you get all the news from?

> Answer:
 From various sources such as newspapers, online websites like NU.nl or KantiNewsPaper website for sports updates/news articles about soccer teams in different countries around the world (e.g., Goal reports on football club matches), TV networks and broadcasters that cover popular competitions regularly including live streams of games through platforms such as ESPN3 / NBC Sports Network, social media sites like Twitter (@fifa_official) or Instagram (#FIFAWorldCup2022

> Question:
What is the latest news about Messi?

> Answer:
 The article does not provide any information on recent developments or updates regarding Lionel Messi.

 Impression: Except for one question, answers were not too great. Very slow.

 ---

 - all-MiniLM-L12-v2


> Question:
hi

> Answer:
 Hi! How can I assist you?

 > Question:
 Did PSV play any matches?

> Answer:
 Yes, he played in the Eredivisie for Vitesse Salland.

 > Question:
Where do you get all the news from?

> Answer:
 I use a variety sources such as CNN, BBC News, Reuters for international events like major sports tournaments or breaking political stories. For local coverage on specific topics in my country/town, I usually rely on newspapers and online media outlets that offer reliable information to their readership base based on relevance of the topic they cover.

 > Question:
What is the latest news about Messi?

> Answer:
 The Miami Herald newspaper claims to have information regarding Lionel Messi's contract details at Inter Miami FC and how he plans to line his pockets in America for years, including an option of another season. Additionally, Apple and Adidas are reportedly working on a separate deal with him too as they were doing it previously when there was no agreement yet between the two parties about money matters involved therein, especially related to Messi's salary which can be up to $1 million per year from 2022-2026 if he stays in MLS for this contract.

impression: Best replys. Slow takes about 40secs to 1min to answer. CPU load spikes by 50% when query runs.

---

###

# MODEL_PATH=models/ggml-mpt-7b-instruct.bin
# EMBEDDINGS_MODEL_NAME=all-MiniLM-L12-v2

Update privategpt.py backend to mpt 
llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='mpt', callbacks=callbacks, verbose=False)

> Question:
hi

> Answer:
 Hello

> Question:
Did PSV play any matches?

> Answer:
 They played against Spartak Moscow.

> Question:
Where do you get all the news from?

> Answer:
 Well we use a combination on public APIs, private databases provided by companies to access their internal data as well some RSS feeds. In addition our editors curate content they think are interesting or important.

> Question:
What is the latest news about Messi?

> Answer:
 Lionel has just signed his contract to play for Inter Miami
 
 > Question:
What is the latest news about sports other than football?

> Answer:
 The F1 calendar next year' 08-06 0 Charles Leclerc despondent : "We are clearly doing something wrong" 07 - 06

