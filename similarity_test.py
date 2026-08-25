from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is used for data engineering.",
    "Python is commonly used to build data pipelines.",
    "I like eating pizza."
]

embeddings = model.encode(sentences)

similarity_1_2 = util.cos_sim(embeddings[0], embeddings[1])
similarity_1_3 = util.cos_sim(embeddings[0], embeddings[2])

print("Python/Data Engineering similarity:", similarity_1_2)
print("Python/Pizza similarity:", similarity_1_3)