from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)

instruction = "You are a helpful day planner. Create a fun and detailed day plans"

user_prompt = "plan a day for a {person} in {location} who likes {interests}"

prompt = ChatPromptTemplate.from_messages([("system", instruction), 
                                           ("human", user_prompt)])

person =input("person type: ")
location = input("Location: ")
interests = input("interests: ")

my_chain = prompt | llm
response = my_chain.invoke({
    "person": person,
    "location": location,
    "interests": interests
})

print("\n" + response.content)