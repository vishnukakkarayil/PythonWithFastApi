from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "success"}

def main():
    x = 1
    print("Hello from pythonwithfastapi!", x)




if __name__ == "__main__":
    main()
