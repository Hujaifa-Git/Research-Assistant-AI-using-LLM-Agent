from inference import create_agent, generate
import config as ctg

if __name__ == '__main__':
    agent_executor = create_agent()
    while True:
        option = int(input(ctg.option))               
        if option==6:
            break
        else:
            query = input('Enter your query: ')
            query += ctg.option_dict[option]
            # print(query)
        # print(query, option)       
        response = generate(agent_executor,query)
        # print(response)