from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)


def run_chain(llm, prompt, text):

    chain = (
        ChatPromptTemplate.from_template(
            prompt
        )
        | llm
        | StrOutputParser()
    )

    return chain.invoke(
        {"text": text}
    )