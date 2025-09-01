# LangChain Intro Demo (Safe)
# Chaining two toy tools together

def math_tool(a, b):
    return a + b

def formatter_tool(result):
    return f"The computed result is {result}."

# Chain execution
print("=== LangChain Toy Chain Demo ===")
step1 = math_tool(5, 7)
step2 = formatter_tool(step1)

print("Step 1 (Math Tool):", step1)
print("Step 2 (Formatter Tool):", step2)
