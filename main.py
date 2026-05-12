import requests

def generate_x_post(usr_input: str) -> str:
    payload = {
        "model": "gpt-4.1-mini",
        "input": usr_input
    }
    response = requests.post(
        "https://api.openai.com/v1/responses",
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer adfssdf"
        }
    )
    response.raise_for_status()
    data = response.json()
    return data.get("output", [{}])[0].get("content", [{}])[0].get("text", "")


def main():
    # take user input => LLM to generate X post => output post

    usr_input = input("what should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print(x_post)


if __name__ == "__main__":
    main()
