import os
import openai

from typing import Union
import collections
from IPython.display import Markdown, display

# access/create the .env file in the project dir for getting API keys. Create a .env file in the project/repository root,
# and add your own API key like "OPENAI_API_KEY = <your key>" without any quotes, after you pull this code in your IDE (VS Code devcontainer recommended).
# .env has already been added to git ignore so don't worry when pushing all files to remote.
from dotenv import load_dotenv

load_dotenv()

# import the required langchain and llama-index libraries.
# also the libraries for this querying pipeline.
from langchain import OpenAI
from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

from llama_index.langchain_helpers.agents import LlamaToolkit, create_llama_chat_agent, IndexToolConfig
from llama_index import (LLMPredictor, ServiceContext, SimpleDirectoryReader,
                         SQLDatabase, StorageContext, VectorStoreIndex,
                         set_global_service_context)
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine
from llama_index.indices.struct_store.sql_query import NLSQLTableQueryEngine
from llama_index.logger import LlamaLogger
from llama_index.callbacks import CallbackManager, LlamaDebugHandler
from llama_index.objects import (ObjectIndex, SQLTableNodeMapping,
                                 SQLTableSchema)
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.retrievers import VectorIndexRetriever

# DB Interface library
from sqlalchemy import (Column, Integer, MetaData, String, Table, column,
                        create_engine, select, inspect)

# import DB settings
from dbconnector import DBcomm

# Import Global runtime settings
from settings import runtime
##################################################################################################################################################################


# Logger object for logging the pipeline
llama_logger = LlamaLogger()

## OPEN AI API KEY
openai_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_key

## MODE SELECTION AS PER SETTINGS.PY FILE
USE_PRECISION_PIPELINE = runtime["precision_mode"]
USE_LOCAL_EMBED_MODEL = runtime["local_embed"]

## OPEN AI CONFIGURATION or LLAMA CONFIGURATION AS PER MODE SELECTION
class LLMConf () :
	def __init__(self) :
		if USE_PRECISION_PIPELINE : # This is by-default TRUE while development phase
			# gpt 3.5 and gpt 4 route
			self.llm_fast = LLMPredictor(llm=ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo-16k"))
			self.llm_deep = LLMPredictor(llm=ChatOpenAI(temperature=0.1, model_name="gpt-4"))
			self.llm_super = LLMPredictor(llm=ChatOpenAI(temperature=0.2, model_name="gpt-4-32k"))
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
supe_llm = llm_conf.llm_super

## LLAMA-INDEX CONFIGURATION
## Service context shared globally by the whole application
llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
service_context = ServiceContext.from_defaults (llm=deep_llm if USE_PRECISION_PIPELINE else fast_llm,
					       						#embed_model="local" if USE_LOCAL_EMBED_MODEL else None, # None for openai embeddings i.e. default for llamaindex
												llama_logger=llama_logger,
												callback_manager=callback_manager)
set_global_service_context(service_context) # only for dev phase, later remove this line and use locally instantiated service_context directly based on the usecase


class Kwairy () :
	def __init__(self) :
		self.task_stack = collections.deque()
		inspector = inspect(DBcomm.sql_engine)
		self.sql_table_names = inspector.get_table_names()
		self.sql_db = SQLDatabase(DBcomm.sql_engine, include_tables=self.sql_table_names)

	def chat_to_sql( self, question: Union[str, list[str]] , synthesize_response: bool = True ) :
		query_engine = NLSQLTableQueryEngine(
			sql_database=self.sql_db,
			tables=self.sql_table_names,
			synthesize_response=synthesize_response,
			service_context=service_context,
		)
		try:
			response = query_engine.query(question)
			response_md = str(response)
			sql = response.metadata["sql_query"]
		except Exception as ex:
			response = "Error"
			response_md = "Error"
			sql = f"ERROR: {str(ex)}"
		# response_template = """## Question: {question} ```  ## Answer: {response} ```  ## Generated SQL Query:``` {sql}"""
		# display(Markdown(response_template.format(question=question, response=response_md, sql=sql)))
		return response, response_md, sql
	
	def ingest(user_input : str) :
		# given this user query, we need to find the intent and entities
		# and then we need to find the relevant tables and columns
		# and then we need to generate the SQL query
		# and then we need to execute the SQL query
		# and then we need to return the results
		# and then we need to display the results
		# and then we need to ask the user if they want to continue
		# and then we need to ask the user if they want to ask another question
		# and then we need to ask the user if they want to exit
		# and then we need to exit

		pass
