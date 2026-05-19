from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="experiment_data.csv")
data = loader.load()
for row in data:
    print(row.page_content)