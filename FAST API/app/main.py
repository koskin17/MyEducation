from fastapi import FastAPI

# Creating App
app = FastAPI()


@app.get("/hotels")
def get_hotels():
    return "Отель Бридж Резорт 5 звёзд"