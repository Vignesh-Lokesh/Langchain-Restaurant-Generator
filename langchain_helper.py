from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Use the smaller gemma3:1b model for M1 Macs
llm = Ollama(model="gemma3:1b", temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="List 5 menu items for {restaurant_name} as a comma-separated string. Do NOT include explanations or numbering."
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Sequential chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Run the chain
    response = chain({'cuisine': cuisine})

    # Clean up menu items
    response['menu_items'] = [item.strip() for item in response['menu_items'].split(",")]

    return response

# Test
if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
