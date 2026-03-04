
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge

reference = "The cat is sitting on the mat"
generated = "A cat sits on the mat"

# BLEU
bleu = sentence_bleu([reference.split()], generated.split())
print("BLEU Score:", bleu)

# ROUGE
rouge = Rouge()
scores = rouge.get_scores(generated, reference)
print("ROUGE Score:", scores)
