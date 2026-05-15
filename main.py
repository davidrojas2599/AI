import json
import os
from openai import OpenAI
# Run "uv sync" to install the below packages
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
# not need as its called directly from OpenAI()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(topic: str) -> str:
    with open("post-examples.json", "r") as f:
        examples = json.load(f)

    examples_str = ""
    for i, example in enumerate(examples, 1):
        examples_str += f"""
        <example-{i}>
            <topic>
            {example['topic']}
            </topic>

            <generated-post>
            {example['post']}
            </generated-post>
        </example-{i}>
        """
    
    prompt = f"""
        You are a partner account manager of TCS, a GSI partner at Red Hat. You are responsicble for creating new solutions to take to market with TCS.
        You have a goals of 220 million for the year. Look for opportunities to create new solutions with TCS to reach that goal. 
        create a Linkedin post on technology that is relevant to TCS and Red Hat's partnership. The post should be engaging and informative, highlighting the benefits of the partnership and how it can help businesses achieve their goals.
        The post should also include a call to action, encouraging readers to learn more about the partnership and how it can help them.
        Here's the topic for the post: 
        <topic>
        {topic}
        </topic>
        Here are some examples of Linkedin posts that you can use as inspiration for your post:
        <examples>
           {examples_str}
        </examples>

        Please use the tone and style of the above examples to create your post. The post should be no more than 150 words and should be written in a professional and engaging manner.
    """

    response = client.responses.create(
        model="gpt-4o",
        input=prompt
        
    )

    return response.output_text



def main():
    # user input => AI (LLM) to generate X post => output post

    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print(x_post)


if __name__ == "__main__":
    main()