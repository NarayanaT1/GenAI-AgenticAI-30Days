# Minimal text generator using Hugging Face transformers (distilgpt2).
# Safe, public learning demo — no secrets, no proprietary data.
import argparse
import os

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def build_generator(model_name: str = "distilgpt2", device: int = -1):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=device  # -1 = CPU, 0 = first GPU if available
    )
    return generator

def generate_text(prompt: str, max_new_tokens: int = 60, temperature: float = 0.8, top_p: float = 0.95, seed: int = 42):
    if seed is not None:
        try:
            import random
            random.seed(seed)
            torch.manual_seed(seed)
        except Exception:
            pass

    device = 0 if torch.cuda.is_available() else -1
    gen = build_generator(device=device)
    outputs = gen(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
        pad_token_id=gen.tokenizer.eos_token_id
    )
    return outputs[0]["generated_text"]

def main():
    parser = argparse.ArgumentParser(description="Simple text generator using transformers (distilgpt2).")
    parser.add_argument("--prompt", type=str, required=True, help="Input prompt")
    parser.add_argument("--max_new_tokens", type=int, default=60)
    parser.add_argument("--temperature", type=float, default=0.8)
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    text = generate_text(
        args.prompt,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
        seed=args.seed
    )
    print(text)

if __name__ == "__main__":
    main()
