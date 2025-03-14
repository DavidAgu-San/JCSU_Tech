
from agents import Agent
from openai import OpenAI

# Ensure your OpenAI API key is set
API_KEY = "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"
client = OpenAI(api_key=API_KEY)

document = """Unnamed: 0Daily Time Spent on Site Age Area IncomeDaily Internet Usage Male TimestampClicked on Ad city
 0 93.67 62 69844.53 101.87Male 4/6/2024No Charlotte
 1 191.62 60 70121.18 35.95Female No Charlotte
 2 154.44 51 95206.52 187.48Female 5/7/2020No Charlotte
 3 131.77 26 31423.9 257.4Male 8/17/2024No Charlotte
 4 56.52 43 60698.1 178.22Male 9/15/2021No Charlotte
 5 56.52 19 103683.6 89.2Female 9/24/2023Yes Charlotte
 6 39.87 26 84289.75 39.09Female 6/23/2022No Charlotte
 7 177.25 26 60350.44 87.95Female Yes Charlotte
 8 132.19 57 111497.2 142.35Male 2/7/2023No Charlotte
 9 150.37 34 99536.05 235.1Male 6/27/2021No Charlotte
 10 33.5 18 53840.59 80.72Male 2/16/2022No Charlotte
 11 194.88 42 88076.09 224.34Male 4/9/2021Yes Charlotte
 12 171.52 60 83617.57 264.07Male 1/5/2025Yes Charlotte
 13 66.1 57 66106.91 152.57Female 2/28/2024No Charlotte
 14 60.91 59 63026.05 251.79Male 2/12/2023No Charlotte
 15 61.18 42 60920.44 179.76Female Yes Charlotte
"""

class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def process(self, input_text):
        response = client.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": input_text}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

Agents1 = Agent(
    name="data scanner",
    instructions="You are a data scientist, and are tasked with identifying data components.",
)

Agent2 = Agent(
    name="data analysis",
    instructions="You provide a summary of the data, and important finding that might be relevant to our consumers.",
)
    
Agent3 = Agent(
    name="data reporter",
    instructions="You are a data reporter, and you will be task clearning up Agent2's data report.",

)

Agent4 = Agent(
    name="data decider",
    instructions="you are a expert at decision, your job is to make non bias decision as to where we have to allocate our resources to. Specifically, you will be task with measuring the amount of time a user has interacted with an ad, as well as where a user is located."
)

Agent5 = Agent(
    name="data improver",
    instructions="You will act as a amicable soul, and receieve feedback to continuously improve the mult-agent AI service."
)

output = Agent2.process(document)
print("Data Analysis Output:\n", output)
output = Agent3.process(output)