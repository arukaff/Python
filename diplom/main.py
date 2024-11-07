import pandas as pd
import numpy as np
from langchain_objectbox.vectorstores import ObjectBox
from llama_cpp import Llama

objectbox = ObjectBox.from_texts(texts, embeddings,
       embedding_dimensions=768)