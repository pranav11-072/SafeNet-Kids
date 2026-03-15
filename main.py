import customtkinter as ctk
import os
from core.monitor import SafeNetMonitor
from core.process_manager import ProcessManager
from gui.dashboard import Dashboard

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("SafeNet Kids - Security Dashboard")
    app.geometry("800x500")
    app.resizable(False, False)

    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/safenet_audit.log"):
        open("data/safenet_audit.log", "w").close()

    process_manager = ProcessManager()
    monitor = SafeNetMonitor("data/threat_database.json", "data/safenet_audit.log", process_manager)

    dashboard = Dashboard(app, monitor, process_manager)
    dashboard.pack(fill="both", expand=True)

    def on_closing():
        monitor.stop()
        process_manager.stop_process_blocker()
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()

if __name__ == "__main__":
    main()
