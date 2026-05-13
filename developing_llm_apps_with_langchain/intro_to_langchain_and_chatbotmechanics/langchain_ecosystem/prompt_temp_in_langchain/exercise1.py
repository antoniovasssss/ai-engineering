from langchain_core.prompts import PromptTemplate

template = "Explain {concept} in simple terms"

prompt = PromptTemplate(
    input_variables=["concept"],
    template=template
)

final_prompt = prompt.format(concept="Artificial Intelligence")

print(final_prompt)