from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
import os

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index

def load_pdfs_from_folder(folder_path):
    pdf_reader = PDFReader()
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            pdf_data = pdf_reader.load_data(file=pdf_path)
            data.extend(pdf_data)
    return data

pdf_folder_path = "data"

predict_pdfs_data = load_pdfs_from_folder(pdf_folder_path)

predict_index = get_index(predict_pdfs_data, "predict")

pdf_engine = predict_index.as_chat_engine()
