import os
import openai

# access/create the .env file in the project dir for getting API keys. Create a .env file in the project/repository root,
# and add your own API key like "OPENAI_API_KEY = <your key>" without any quotes, after you pull this code in your IDE (VS Code devcontainer recommended).
# .env has already been added to git ignore so don't worry when pushing all files to remote.
from dotenv import load_dotenv
load_dotenv()

# libraries for this querying pipeline:
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select, column
from llama_index import LLMPredictor, ServiceContext, \
    					SQLDatabase, SimpleDirectoryReader, \
                        StorageContext, VectorStoreIndex, \
                        set_global_service_context
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine
from llama_index.objects import SQLTableNodeMapping, ObjectIndex, SQLTableSchema
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from langchain import OpenAI

# Global settings
from settings import runtime_logistics

## OPEN AI API KEY
openai_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_key

## MODE SELECTION AS PER SETTINGS.PY FILE
USE_PERFORMANCE_PIPELINE = runtime_logistics["performance_mode"]

## Service context shared globally by the whole application
service_context = ServiceContext.from_defaults(embed_model="local")
set_global_service_context(service_context)

class Kwairy () :
    pass