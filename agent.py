import time
from openai import OpenAI
from openai import RateLimitError

client = OpenAI()

def create_response_with_retry(model: str, prompt: str, max_retries: int = 5) -> str:
    backoff = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            response = client.responses.create(model=model, input=prompt)
            return response.output_text
        except RateLimitError:
            if attempt == max_retries:
                raise
            print(f"Rate limit hit (429). Retrying in {backoff:.1f}s... (attempt {attempt}/{max_retries})")
            time.sleep(backoff)
            backoff *= 2


if __name__ == "__main__":
    story = create_response_with_retry(
        model="gpt-5.5",
        prompt="Write a one-sentence bedtime story about a unicorn."
    )
    print(story)