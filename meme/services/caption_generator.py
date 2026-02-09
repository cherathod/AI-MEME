from transformers import pipeline


gererator = pipeline("text-generation", model ="gpt2")


def generate_caption(prompt: str) -> str:
    response = gererator(
        f"Generate a funny meme caption about {prompt}:",
        max_length = 30,
        temperature = 0.9
    )
    return response[0]["generated_text"]

