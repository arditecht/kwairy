import os
import openai

# access/create the .env file in the project dir for getting API keys. Create a .env file in the project/repository root,
# and add your own API key like "OPENAI_API_KEY = <your key>" without quotes, after you pull this code.
# .env has already been added to git ignore so don't worry when pushing all files to remote.
from dotenv import load_dotenv
load_dotenv()

# libraries for querying pipeline:
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select, column
from llama_index import LLMPredictor, ServiceContext, SQLDatabase, VectorStoreIndex
from llama_index import set_global_service_context
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine
from llama_index.objects import SQLTableNodeMapping, ObjectIndex, SQLTableSchema
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from langchain import OpenAI
import chromadb

## OPEN AI API KEY
openai_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_key

## MODE SELECTION AS PER ENV FILE
MODE = "high"

## CHROMA DB CLIENT SDK
chroma_client = chromadb.Client()

## Service context shared globally by the whole application
service_context = ServiceContext.from_defaults(embed_model="local")
set_global_service_context(service_context)

