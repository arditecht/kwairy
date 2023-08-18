import os
import openai

# access/create the .env file in the project dir for getting API keys. Create a .env file in the project/repository root,
# and add your own API key like "OPENAI_API_KEY = <your key>" without any quotes, after you pull this code in your IDE (VS Code devcontainer recommended).
# .env has already been added to git ignore so don't worry when pushing all files to remote.
from dotenv import load_dotenv
load_dotenv()

# libraries for this querying pipeline:
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select, column
from langchain import OpenAI
from llama_index import LLMPredictor, ServiceContext, \
    					SQLDatabase, SimpleDirectoryReader, \
                        StorageContext, VectorStoreIndex, \
                        set_global_service_context
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine
from llama_index.objects import SQLTableNodeMapping, ObjectIndex, SQLTableSchema
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor

## OPEN AI API KEY
openai_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_key

# Import Global settings
from settings import runtime

## MODE SELECTION AS PER SETTINGS.PY FILE
USE_PRECISION_PIPELINE = runtime["precision_mode"]
USE_LOCAL_EMBED_MODEL = runtime["local_embed"]

## OPEN AI CONFIGURATION or LLAMA CONFIGURATION AS PER MODE SELECTION
class LLMConf () :
	def __init__(self) :
		if USE_PRECISION_PIPELINE : # This is by-default TRUE while development phase
			# gpt 3.5 and gpt 4 route
			self.llm_fast = LLMPredictor(llm=OpenAI(temperature=0.1, model_name="gpt-3.5-turbo"))
			self.llm_deep = LLMPredictor(llm=OpenAI(temperature=0.1, model_name="gpt-4"))
		else :
			# llama 2 route: install LlamaCPP to enable GPU efficient LLama-2 13B chat model to work acc to the production environment chosen.
			# download guide: https://github.com/abetlen/llama-cpp-python#installation-with-openblas--cublas--clblast--metal
			# implementation guide: https://gpt-index.readthedocs.io/en/latest/examples/llm/llama_2_llama_cpp.html 
			'''
			from llama_index.llms import LlamaCPP
			from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt
			llm = LlamaCPP(
				# You can pass in the URL to a GGML model to download it automatically
				model_url="https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin",
				# optionally, you can set the path to a pre-downloaded model instead of model_url
				model_path=None,
				temperature=0.1,
				max_new_tokens=256,
				# llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
				context_window=3900,
				# kwargs to pass to __call__()
				generate_kwargs={},
				# kwargs to pass to __init__()
				# set to at least 1 to use GPU
				model_kwargs={"n_gpu_layers": 1},
				# transform inputs into Llama2 format
				messages_to_prompt=messages_to_prompt,
				completion_to_prompt=completion_to_prompt,
				verbose=True,
			)
			'''
			pass

## INSTANTIATE LLMs
llm_conf = LLMConf()
fast_llm = llm_conf.llm_fast
deep_llm = llm_conf.llm_deep


## LLAMA-INDEX CONFIGURATION
## Service context shared globally by the whole application
service_context = ServiceContext.from_defaults(embed_model="local" if USE_LOCAL_EMBED_MODEL else "remote")
set_global_service_context(service_context)

class Kwairy () :
    pass