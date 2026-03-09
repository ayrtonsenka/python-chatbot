from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    '''useful for a performing basic arithetic calculations with numbers'''
    return f'sum of {a} and {b} is {a+b}'

def main():
    model = ChatOpenAI(temperature = 0)
    tools = [calculator]

    agent_executor = create_react_agent(model, tools)

    print('welcome, how can i help u today?')

    while True:
        user_input = input('\nyou: ').strip()
        
        if user_input == 'q':
            break

        print('\nbot: ', end='')
        for chunk in agent_executor.stream(
            {
                'messages':[HumanMessage(content=user_input)]
            }
        ):
            if 'agent' in chunk and 'messages' in chunk['agent']:
                for message in chunk['agent']['messages']:
                    print(message.content, end='')
        print()

if __name__ == '__main__':
    main()