from sentence_transformers import SentenceTransformer,util
model = SentenceTransformer("all-MiniLM-L6-v2")

def analyze(reference,student):
    emb1 = model.encode(reference, convert_to_tensor=True)
    emb2 = model.encode(student, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()*100

    return score