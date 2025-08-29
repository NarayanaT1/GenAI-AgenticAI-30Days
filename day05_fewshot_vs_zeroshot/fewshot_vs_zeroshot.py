# Few-shot vs Zero-shot Prompting (Safe Demo)
# This is a toy example, no external API calls.

print("=== Zero-shot ===")
print("Prompt: Translate 'Good night' to French")
print("Expected: Bonne nuit")

print("\n=== Few-shot ===")
prompt = \"\"\"Translate English to French:
- Hello -> Bonjour
- Thank you -> Merci
- Good morning -> Bonjour
Translate: Good night ->\"\"\"
print(prompt)
print("Expected: Bonne nuit")
