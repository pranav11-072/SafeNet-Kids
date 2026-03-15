import customtkinter as ctk
import os
import threading
import time
from gui.auth_window import AuthWindow


class Dashboard(ctk.CTkFrame):
    def __init__(self, master, monitor, process_manager):
        super().__init__(master)
        self.master = master
        self.monitor = monitor
        self.process_manager = process_manager
        self.log_file = "data/safenet_audit.log"

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar, text="SafeNet Kids", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.status_label = ctk.CTkLabel(self.sidebar, text="Status: STOPPED", text_color="red")
        self.status_label.grid(row=1, column=0, padx=20, pady=10)

        self.toggle_btn = ctk.CTkButton(self.sidebar, text="Start Monitoring", command=self._request_toggle)
        self.toggle_btn.grid(row=2, column=0, padx=20, pady=10)

        self.main_view = ctk.CTkFrame(self, corner_radius=10)
        self.main_view.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_view.grid_rowconfigure(1, weight=1)
        self.main_view.grid_columnconfigure(0, weight=1)

        self.log_label = ctk.CTkLabel(self.main_view, text="Live Activity Log",
                                      font=ctk.CTkFont(size=16, weight="bold"))
        self.log_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.log_box = ctk.CTkTextbox(self.main_view, width=500, height=300)
        self.log_box.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.log_box.configure(state="disabled")

        self.stats_frame = ctk.CTkFrame(self.main_view)
        self.stats_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")

        self.threats_label = ctk.CTkLabel(self.stats_frame, text="Threats Detected: 0", font=ctk.CTkFont(size=14))
        self.threats_label.pack(pady=10)

        self.update_thread = threading.Thread(target=self._update_logs, daemon=True)
        self.update_thread.start()

    def _request_toggle(self):
        AuthWindow(self.master, self._toggle_monitoring)

    def _toggle_monitoring(self):
        if self.monitor.is_running:
            self.monitor.stop()
            self.status_label.configure(text="Status: STOPPED", text_color="red")
            self.toggle_btn.configure(text="Start Monitoring")
        else:
            self.monitor.start()
            self.status_label.configure(text="Status: RUNNING", text_color="green")
            self.toggle_btn.configure(text="Stop Monitoring")

    def _update_logs(self):
        last_mtime = 0
        while True:
            if os.path.exists(self.log_file):
                mtime = os.path.getmtime(self.log_file)
                if mtime > last_mtime:
                    last_mtime = mtime
                    with open(self.log_file, "r") as f:
                        lines = f.readlines()

                    self.log_box.configure(state="normal")
                    self.log_box.delete("1.0", "end")
                    for line in lines[-20:]:
                        self.log_box.insert("end", line)
                    self.log_box.configure(state="disabled")

                    threat_count = sum(1 for line in lines if "Threat:" in line)
                    self.threats_label.configure(text=f"Threats Detected: {threat_count}")
            time.sleep(2)
