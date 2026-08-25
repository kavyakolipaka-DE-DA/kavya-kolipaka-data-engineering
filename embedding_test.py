from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is used for data engineering.",
    "Python is commonly used to build data pipelines.",
    "I like eating pizza."
]

embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print(sentence)
    print("Vector length:", len(embedding))
    print("First 5 values:", embedding[:5])


