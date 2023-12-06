from langserve import RemoteRunnable


remote_chain = RemoteRunnable("http://localhost:8000/category_chain/")

if __name__ == "__main__":
    print("starting invoke")
    print(remote_chain.invoke({"text": "colors"}))
    print("ended invoke")