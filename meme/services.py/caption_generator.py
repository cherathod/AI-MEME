from transformers import pipeline

generator = pipeline(
    "text-generation",
    model = "gpt2"
)


def generate_caption(prompt: str) -> str:
    response = generator(
        prompt,
        max_length = 30,
        num_return_sequences = 1,
        temperature = 0.9
    )
    return response[0]["generated_text"]