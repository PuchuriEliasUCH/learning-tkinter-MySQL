from tkinter import * 
from tkinter import ttk
import mysql.connector as con

class Persona:
    def __init__(self, root):
        self.root = root
        self.root.title("Registar Producto")
        self.root.geometry("350x500")

        # Combobox
        categorias = [i[1] for i in self.mostrar_categorias()]
        print(categorias)
        self.combo = ttk.Combobox(root, state = 'readonly', values = categorias)
        self.combo.current(0)
        self.combo.pack()


    def excecute_query(self, query, **params):
        config = {
            'user': 'root',     
            'password': "...",
            'host' : 'localhost', 
            'database':'tienda'
        }
        try:
            con.connect(**config)
        except:
            print("Error en conexión")

        cnx = con.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(query, **params)
        response = cursor.fetchall()
        cnx.commit()
        cnx.close()

        return response

        
    
    def mostrar_categorias(self):
        query = "SELECT * FROM categoria WHERE activo = TRUE;"
        response = self.excecute_query(query)
        return response



if __name__ == "__main__":
    root = Tk()

    Persona(root)

    root.mainloop()