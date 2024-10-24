from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def hello():
    return {"hello world"}

@app.get("/add")
async def root():
  return HTMLResponse(
      """
      <html>
        <head><title>Adicionar Item</title></head>
        <body>
          <h1>Adicionar Item</h1>
          <form method="post" action="/items">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required><br><br>
            <label for="description">Descrição:</label>
            <input type="text" id="description" name="description" required><br><br>
            <label for="price">Preço:</label>
            <input type="number" id="price" name="price" required><br><br>
            <button type="submit">Adicionar</button>
          </form>

          <h1>Adicionar Conta</h1>
          <form method="post" action="/accounts">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required><br><br>
            <label for="balance">Saldo:</label>
            <input type="number" id="balance" name="balance" required><br><br>
            <button type="submit">Adicionar</button>
          </form>
        </body>
      </html>
      """
  )

