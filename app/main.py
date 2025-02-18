from app.console import Console
from app.model import Notebook

def main():
    notebook = Notebook()
    console = Console(notebook)
    console.ejecutar()

if __name__ == "__main__":
    main()