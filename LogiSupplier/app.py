from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def criar_banco():
    conn = sqlite3.connect("fornecedores.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fornecedores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa TEXT NOT NULL,
            cnpj TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            cidade TEXT
        )
    """)

    conn.commit()
    conn.close()

criar_banco()

@app.route("/")
def index():

    conn = sqlite3.connect("fornecedores.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM fornecedores")
    fornecedores = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        fornecedores=fornecedores
    )


@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    empresa = request.form["empresa"]
    cnpj = request.form["cnpj"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    cidade = request.form["cidade"]

    conn = sqlite3.connect("fornecedores.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO fornecedores
        (empresa, cnpj, telefone, email, cidade)
        VALUES (?, ?, ?, ?, ?)
    """, (empresa, cnpj, telefone, email, cidade))

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/excluir/<int:id>")
def excluir(id):

    conn = sqlite3.connect("fornecedores.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM fornecedores WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")



@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = sqlite3.connect("fornecedores.db")
    cursor = conn.cursor()

  
    if request.method == "POST":
        empresa = request.form["empresa"]
        cnpj = request.form["cnpj"]
        telefone = request.form["telefone"]
        email = request.form["email"]
        cidade = request.form["cidade"]

        cursor.execute("""
            UPDATE fornecedores 
            SET empresa = ?, cnpj = ?, telefone = ?, email = ?, cidade = ?
            WHERE id = ?
        """, (empresa, cnpj, telefone, email, cidade, id))
        
        conn.commit()
        conn.close()
        return redirect("/") 
        

    else:
        cursor.execute("SELECT * FROM fornecedores WHERE id = ?", (id,))
        fornecedor = cursor.fetchone()
        conn.close()
        

        return render_template("editar.html", fornecedor=fornecedor)


if __name__ == "__main__":
    app.run(debug=True)


