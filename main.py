
from dataset import dataset
import faiss
import numpy as np



# Step 1: Create Simple Embeddings

def text_to_vector(text):
    # Convert text into numeric vector (simple embedding)
    return np.array([
        len(text),
        sum(ord(c) for c in text) % 1000
    ], dtype='float32')

# Step 2: Build FAISS Index

vectors = np.array([text_to_vector(q) for q in dataset])
dimension = vectors.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(vectors)

print("FAISS index created with", index.ntotal, "vectors")

# Step 3: Define Answer Generators

def correct_answer(q):
    return f"{q} - This is a correct and concise answer."

def wrong_answer(q):
    return f"{q} - This is a very long but incorrect explanation that sounds confident but is wrong."

# Step 4: Simulated Judge

def judge(answer_a, answer_b):
    # Simulate bias: prefers longer answer
    return "A" if len(answer_a) > len(answer_b) else "B"

# Step 5: Run Evaluation

results = []

for q in dataset:
    a = correct_answer(q)
    b = wrong_answer(q)

    # Original order
    result1 = judge(a, b)

    # Swapped order
    result2 = judge(b, a)

    flip = result1 != result2

    results.append({
        "question": q,
        "original_order": result1,
        "swapped_order": result2,
        "flip_occurred": flip
    })

# Step 6: FAISS Search Example

query = "What is AI?"
query_vector = np.array([text_to_vector(query)], dtype='float32')

D, I = index.search(query_vector, k=2)

print("\n FAISS Search Results:")
print("Query:", query)
print("Nearest indices:", I)
print("Distances:", D)

# Step 7: Save Results

with open("results.txt", "w") as f:
    for r in results:
      
        f.write(f"Q: {r['question']}\n")
        f.write(f"Original: {r['original_order']}, Swapped: {r['swapped_order']}\n")
        f.write(f"Flip: {r['flip_occurred']}\n\n")

        
        
import time
start = time.time()

D, I = index.search(query_vector, k=2)

end = time.time()
print("Latency:", (end - start) * 1000, "ms")

print("\nTop Matches:")
for idx in I[0]:
    print("-", dataset[idx])
print("Vector count:", index.ntotal)
print("\n Results saved to results.txt")