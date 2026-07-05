import sys
import os

# Aggiunge il percorso genitore per permettere le importazioni relative
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Aggiunge anche la cartella del progetto stessa per le importazioni dirette
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

folder_name = os.path.basename(project_dir)

print(f"Avvio del server per '{folder_name}'...")

try:
    # Importa dinamicamente app.py usando il nome effettivo della cartella
    app_module = __import__(f"{folder_name}.app", fromlist=["app"])
    app = app_module.app
    
    # Importa la porta di ascolto definita nelle costanti
    from constants import Server
    
    print(f"Server in ascolto su http://localhost:{Server.LISTENING_PORT}/")
    app.run(port=Server.LISTENING_PORT)
except Exception as e:
    print(f"Errore durante l'avvio del server: {e}")
    import traceback
    traceback.print_exc()
    input("\nPremi INVIO per uscire...")
