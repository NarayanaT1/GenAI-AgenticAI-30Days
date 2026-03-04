def detect_hallucination(context, answer):

    context_words = set(context.lower().split())
    answer_words = set(answer.lower().split())

    unknown_words = answer_words - context_words

    if len(unknown_words) > 3:
        return "Possible Hallucination", unknown_words
    else:
        return "Likely grounded answer", unknown_words


context = "The Eiffel Tower is located in Paris"
answer = "The Eiffel Tower is located in Paris and built in 1600"

result, words = detect_hallucination(context, answer)

print(result)
print("Unknown tokens:", words)
