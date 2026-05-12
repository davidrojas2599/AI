import os

import requests

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(topic: str) -> str:
    prompt = f"""
        You are a partner account manager of TCS, a GSI partner at Red Hat. You are responsicble for creating new solutions to take to market with TCS.
        You have a goals of 220 million for the year. Look for opportunities to create new solutions with TCS to reach that goal. 
        create a Linkedin post on technology that is relevant to TCS and Red Hat's partnership. The post should be engaging and informative, highlighting the benefits of the partnership and how it can help businesses achieve their goals.
        The post should also include a call to action, encouraging readers to learn more about the partnership and how it can help them.
        Here's the topic for the post:
        <topic>
        {topic}
        </topic>
    """
    
    payload = {
        "model": "gpt-4.1-mini",
        "input": prompt
    }
    response = requests.post(
        "https://api.openai.com/v1/responses",
        json=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    )
    
    response__text = response.json().get("output", [{}])[0].get("content", [{}])[0].get("text", "")

    return response__text


def main():
    # take user input => LLM to generate X post => output post

    usr_input = input("what should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print(x_post)


if __name__ == "__main__":
    main()
