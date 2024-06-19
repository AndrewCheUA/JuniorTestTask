import os

from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from fastapi import HTTPException

from config import settings



# Initialize LangChain with a pre-trained summarization model
llm = HuggingFaceHub(
            repo_id=os.getenv("facebook/bart-large-cnn", "facebook/bart-large-cnn"),
            task="summarization",
            huggingfacehub_api_token=settings.huggingfacehub_api_token
        )


async def create_summary(user_text: str) -> str:
    try:

        # Define the summarization prompt
        prompt_template = "Please provide a concise summary of the following text:\n{text}"
        prompt = PromptTemplate(input_variables=["text"], template=prompt_template)

        # Create the LangChain summarization chain
        chain = LLMChain(llm=llm, prompt=prompt)

        # Generate summary using LangChain
        summary = chain.run(user_text)

        return summary
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
