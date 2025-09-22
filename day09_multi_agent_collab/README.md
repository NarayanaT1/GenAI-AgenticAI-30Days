# Day 9 — Multi‑Agent Collaboration (Toy Buyer/Seller Chat)

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer. No proprietary/sensitive data.

## Overview
This toy demo shows **two simple agents** (Buyer & Seller) negotiating a purchase (apples).  
A small **Mediator** routes messages and stops when a deal or max turns is reached.

## How it works
- **BuyerAgent**: has a target price and max quantity; negotiates down the price.  
- **SellerAgent**: has a list price and a minimum acceptable price; counters until a threshold.  
- **Mediator**: tracks the transcript and stops when agreement is reached or turns are exhausted.

## Run
```bash
python multi_agent_demo.py
```

You can tweak parameters (prices, quantity, max turns) at the top of the script.

## Example
```
Buyer: I want to buy 10 apples.
Seller: Sure — list price is $2.00 per apple.
Buyer: That's high. Can you do $1.50?
Seller: I can do $1.60 per apple.
Buyer: Deal at $1.60. Confirm?
Seller: Deal confirmed at $1.60 x 10 = $16.00.
Mediator: Agreement reached.
```

## Files
- `multi_agent_demo.py` — toy multi‑agent buyer/seller with a mediator.  
- `README.md` — this explanation file.  
- `LICENSE` — MIT license.  
