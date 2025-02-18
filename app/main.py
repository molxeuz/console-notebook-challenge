from app.console import Console
from app.notebook import Notebook

def main():
    notebook = Notebook()
    console = Console()
    console.ejecutar()

if __name__ == "__main__":
    main()