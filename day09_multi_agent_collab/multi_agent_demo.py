# Day 9 — Multi‑Agent Collaboration (Toy Buyer/Seller Chat)
# Safe, offline toy example (no external APIs)

from dataclasses import dataclass

@dataclass
class BuyerConfig:
    target_price: float = 1.50
    max_qty: int = 10
    max_increase_steps: int = 2  # how many times buyer will raise offer

@dataclass
class SellerConfig:
    list_price: float = 2.00
    min_price: float = 1.60       # seller won't go below this
    max_decrease_steps: int = 2   # how many times seller will discount

class BuyerAgent:
    def __init__(self, cfg: BuyerConfig):
        self.cfg = cfg
        self.offer = cfg.target_price
        self.steps_used = 0
        self.last_msg = ""

    def first_message(self):
        return f"I want to buy {self.cfg.max_qty} apples."

    def respond(self, seller_msg: str):
        self.last_msg = seller_msg.lower()
        if "list price is" in self.last_msg:
            # make first offer based on target price
            return f"That's high. Can you do ${self.offer:.2f}?"
        if "i can do $" in self.last_msg or "my counter is $" in self.last_msg:
            # parse seller price
            import re
            m = re.search(r"\$(\d+(?:\.\d{1,2})?)", self.last_msg)
            if m:
                seller_price = float(m.group(1))
                if seller_price <= self.offer:
                    return f"Deal at ${seller_price:.2f}. Confirm?"
                # try increasing the offer a bit if we still have room
                if self.steps_used < self.cfg.max_increase_steps:
                    self.steps_used += 1
                    self.offer = min(seller_price - 0.05, self.offer + 0.10)
                    return f"Could you do ${self.offer:.2f}?"
                else:
                    return "I'll pass for now."
        if "deal confirmed" in self.last_msg:
            return "Thanks!"
        # default fallback
        return "Can you share your best price per apple?"

class SellerAgent:
    def __init__(self, cfg: SellerConfig, qty:int):
        self.cfg = cfg
        self.qty = qty
        self.price = cfg.list_price
        self.steps_used = 0
        self.last_msg = ""

    def first_message(self):
        return f"Sure — list price is ${self.cfg.list_price:.2f} per apple."

    def respond(self, buyer_msg: str):
        self.last_msg = buyer_msg.lower()
        if "can you do $" in self.last_msg:
            import re
            m = re.search(r"\$(\d+(?:\.\d{1,2})?)", self.last_msg)
            if m:
                buyer_offer = float(m.group(1))
                # accept if above/equal min_price
                if buyer_offer >= self.cfg.min_price:
                    return f"Deal confirmed at ${buyer_offer:.2f} x {self.qty} = ${buyer_offer*self.qty:.2f}."
                # counter if we still have room
                if self.steps_used < self.cfg.max_decrease_steps:
                    self.steps_used += 1
                    # decrease gradually but not below min
                    self.price = max(self.cfg.min_price, self.price - 0.20)
                    return f"I can do ${self.price:.2f} per apple."
                else:
                    return "Best I can do is ${:.2f} per apple.".format(self.price)
        if "deal at $" in self.last_msg:
            import re
            m = re.search(r"\$(\d+(?:\.\d{1,2})?)", self.last_msg)
            if m:
                buyer_price = float(m.group(1))
                if buyer_price >= self.cfg.min_price:
                    return f"Deal confirmed at ${buyer_price:.2f} x {self.qty} = ${buyer_price*self.qty:.2f}."
                else:
                    return f"I can't go that low. Best is ${self.cfg.min_price:.2f}."
        if "pass" in self.last_msg:
            return "Understood — maybe next time."
        return "My counter is ${:.2f} per apple.".format(self.price)

class Mediator:
    def __init__(self, buyer: BuyerAgent, seller: SellerAgent, max_turns:int=10):
        self.buyer = buyer
        self.seller = seller
        self.max_turns = max_turns
        self.transcript = []

    def run(self):
        # opening
        b = self.buyer.first_message()
        s = self.seller.first_message()
        self.transcript.append(("Buyer", b))
        self.transcript.append(("Seller", s))

        for _ in range(self.max_turns):
            # buyer responds to seller
            b = self.buyer.respond(self.transcript[-1][1])
            self.transcript.append(("Buyer", b))
            if "deal confirmed" in b.lower():
                self.transcript.append(("Mediator", "Agreement reached."))
                break

            # seller responds to buyer
            s = self.seller.respond(self.transcript[-1][1])
            self.transcript.append(("Seller", s))
            if "deal confirmed" in s.lower():
                self.transcript.append(("Mediator", "Agreement reached."))
                break
        else:
            self.transcript.append(("Mediator", "No agreement — max turns reached."))

        return self.transcript

if __name__ == "__main__":
    buyer = BuyerAgent(BuyerConfig(target_price=1.50, max_qty=10, max_increase_steps=2))
    seller = SellerAgent(SellerConfig(list_price=2.00, min_price=1.60, max_decrease_steps=2), qty=10)
    m = Mediator(buyer, seller, max_turns=8)
    transcript = m.run()
    for role, msg in transcript:
        print(f"{role}: {msg}")
