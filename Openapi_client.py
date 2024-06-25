from openai import OpenAI

client = OpenAI(api_key='sk-proj-1wTrkjk67XSESwPrBfZuT3BlbkFJLrAjd54VK5yjO4FidUtd')

def generate_response(prompt: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "An unexpected error occurred. Please try again later."


