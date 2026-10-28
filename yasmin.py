# Network Troubleshooting Expert System
# Modern GUI using CustomTkinter
# Install once: pip install customtkinter

import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class NetworkExpertSystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Network Troubleshooting Expert System")
        self.geometry("1000x790")
        self.minsize(900, 720)
        self.configure(fg_color="#0B1220")

        self.colors = {
            "panel": "#121D30",
            "panel2": "#17243A",
            "accent": "#38BDF8",
            "text": "#F1F5F9",
            "muted": "#A7B4C8",
            "green": "#34D399",
            "orange": "#FBBF24",
        }

        self._build_header()
        self._build_form()
        self._build_results()
        self._build_footer()

    def _build_header(self):
        header = ctk.CTkFrame(self, corner_radius=18, fg_color="#12233B")
        header.pack(fill="x", padx=22, pady=(22, 14))

        ctk.CTkLabel(
            header, text="NETWORK EXPERT SYSTEM",
            font=ctk.CTkFont(family="Arial", size=26, weight="bold"),
            text_color=self.colors["text"]
        ).pack(anchor="w", padx=24, pady=(20, 4))

        ctk.CTkLabel(
            header,
            text="Troubleshooting assistant • Rule-based diagnosis • Suggested solutions",
            font=ctk.CTkFont(family="Arial", size=13),
            text_color=self.colors["muted"]
        ).pack(anchor="w", padx=24, pady=(0, 20))

    def _build_form(self):
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="x", padx=22)

        form = ctk.CTkFrame(body, corner_radius=18, fg_color=self.colors["panel"])
        form.pack(side="left", fill="both", expand=True, padx=(0, 10))

        ctk.CTkLabel(
            form, text="NETWORK CHECKUP",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color=self.colors["accent"]
        ).pack(anchor="w", padx=20, pady=(18, 4))

        ctk.CTkLabel(
            form, text="Choose the answers that best describe the issue.",
            font=ctk.CTkFont(size=12), text_color=self.colors["muted"]
        ).pack(anchor="w", padx=20, pady=(0, 14))

        self.internet = self._dropdown(form, "1. Is the internet working?", ["Select", "Yes", "No"])
        self.speed = self._dropdown(form, "2. How is the internet speed?", ["Select", "Normal", "Slow"])
        self.connection = self._dropdown(form, "3. Connection type", ["Select", "Wi-Fi", "Cable"])
        self.connected = self._dropdown(form, "4. Is your device connected to the network?", ["Select", "Yes", "No"])
        self.router = self._dropdown(form, "5. Is the router powered on and showing normal lights?", ["Select", "Yes", "No"])
        self.other_devices = self._dropdown(form, "6. Can other devices access the internet?", ["Select", "Yes", "No"])

        buttons = ctk.CTkFrame(form, fg_color="transparent")
        buttons.pack(fill="x", padx=18, pady=(10, 18))

        ctk.CTkButton(
            buttons, text="Diagnose Network", command=self.diagnose,
            height=42, corner_radius=11, font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#0284C7", hover_color="#0369A1"
        ).pack(side="left", fill="x", expand=True, padx=(0, 7))

        ctk.CTkButton(
            buttons, text="Reset", command=self.reset,
            height=42, width=100, corner_radius=11,
            fg_color="#334155", hover_color="#475569"
        ).pack(side="left")

        tips = ctk.CTkFrame(body, corner_radius=18, fg_color=self.colors["panel2"], width=240)
        tips.pack(side="right", fill="y", padx=(10, 0))
        tips.pack_propagate(False)

        ctk.CTkLabel(
            tips, text="QUICK TIPS",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.colors["accent"]
        ).pack(anchor="w", padx=18, pady=(20, 12))

        for item in [
            "• Check cables and power",
            "• Confirm Wi-Fi connection",
            "• Compare with other devices",
            "• Restart router if needed",
            "• Contact ISP if outage persists",
        ]:
            ctk.CTkLabel(
                tips, text=item, wraplength=195, justify="left",
                font=ctk.CTkFont(size=12), text_color=self.colors["text"]
            ).pack(anchor="w", padx=18, pady=7)

        ctk.CTkLabel(
            tips,
            text="Note: This tool provides a rule-based preliminary diagnosis.",
            wraplength=195, justify="left",
            font=ctk.CTkFont(size=11), text_color=self.colors["muted"]
        ).pack(anchor="w", padx=18, pady=(20, 8))

    def _dropdown(self, parent, label, options):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=18, pady=5)

        ctk.CTkLabel(
            row, text=label, anchor="w", justify="left",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=self.colors["text"], wraplength=360
        ).pack(side="left", fill="x", expand=True, padx=(0, 10))

        menu = ctk.CTkOptionMenu(
            row, values=options, width=125, height=32,
            corner_radius=9, fg_color="#263750",
            button_color="#0284C7", button_hover_color="#0369A1",
            dropdown_fg_color="#17243A"
        )
        menu.set("Select")
        menu.pack(side="right")
        return menu

    def _build_results(self):
        self.result_frame = ctk.CTkFrame(self, corner_radius=18, fg_color=self.colors["panel"])
        self.result_frame.pack(fill="both", expand=True, padx=22, pady=(14, 8))

        ctk.CTkLabel(
            self.result_frame, text="DIAGNOSIS REPORT",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color=self.colors["accent"]
        ).pack(anchor="w", padx=20, pady=(16, 8))

        self.problem_label = ctk.CTkLabel(
            self.result_frame, text="Your diagnosis will appear here.",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.colors["text"], anchor="w", justify="left", wraplength=900
        )
        self.problem_label.pack(anchor="w", padx=20, pady=(2, 8))

        self.reason_label = ctk.CTkLabel(
            self.result_frame, text="Reason: —",
            font=ctk.CTkFont(size=13), text_color=self.colors["muted"],
            anchor="w", justify="left", wraplength=900
        )
        self.reason_label.pack(anchor="w", padx=20, pady=5)

        self.solution_label = ctk.CTkLabel(
            self.result_frame, text="Suggested solution: —",
            font=ctk.CTkFont(size=13), text_color=self.colors["green"],
            anchor="w", justify="left", wraplength=900
        )
        self.solution_label.pack(anchor="w", padx=20, pady=(5, 18))

    def _build_footer(self):
        ctk.CTkLabel(
            self, text="Python • CustomTkinter • Knowledge Base + Inference Rules",
            font=ctk.CTkFont(size=11), text_color="#718096"
        ).pack(pady=(0, 12))

    def diagnose(self):
        internet = self.internet.get()
        speed = self.speed.get()
        connection = self.connection.get()
        connected = self.connected.get()
        router = self.router.get()
        other_devices = self.other_devices.get()

        problem = reason = solution = None

        if internet == "Select":
            messagebox.showwarning("Missing information", "Please answer question 1.")
            return

        if internet == "Yes":
            if speed == "Select":
                messagebox.showwarning("Missing information", "Please answer question 2.")
                return
            if speed == "Slow":
                problem = "Slow Internet Connection"
                reason = "The connection works, but its speed is reported as slow."
                solution = "Run a speed test, reduce heavy network usage, and check router placement."
            else:
                problem = "Network Appears to Be Working"
                reason = "You reported that internet access and speed are normal."
                solution = "No immediate action is suggested. If an app still fails, check that app separately."
        else:
            if connection == "Select":
                messagebox.showwarning("Missing information", "Please answer question 3.")
                return
            if connected == "Select":
                messagebox.showwarning("Missing information", "Please answer question 4.")
                return

            if connected == "No":
                if connection == "Wi-Fi":
                    problem = "Wi-Fi Connection Not Established"
                    reason = "The device is not connected to the Wi-Fi network."
                    solution = "Select the correct Wi-Fi network, reconnect, and verify the password."
                else:
                    problem = "Possible Ethernet Cable Issue"
                    reason = "The device is not connected to the network over cable."
                    solution = "Reconnect the Ethernet cable and check the port/link lights."
            else:
                if router == "Select":
                    messagebox.showwarning("Missing information", "Please answer question 5.")
                    return
                if router == "No":
                    problem = "Possible Router or Power Issue"
                    reason = "The router is reported as not working normally."
                    solution = "Check the power adapter and cables, then restart the router if appropriate."
                else:
                    if other_devices == "Select":
                        messagebox.showwarning("Missing information", "Please answer question 6.")
                        return
                    if other_devices == "Yes":
                        problem = "Possible ISP or Router WAN Issue"
                        reason = "Multiple devices are unable to access the internet while the router is powered on."
                        solution = "Check the router's WAN/Internet status and service outage information; contact your ISP if needed."
                    else:
                        problem = "Possible Device Network Configuration Issue"
                        reason = "Other devices work, but this device cannot access the internet."
                        solution = "Restart this device and check its IP configuration, network adapter, proxy, and DNS settings."

        self.problem_label.configure(text=problem)
        self.reason_label.configure(text="Reason: " + reason)
        self.solution_label.configure(text="Suggested solution: " + solution)

    def reset(self):
        for menu in (self.internet, self.speed, self.connection, self.connected, self.router, self.other_devices):
            menu.set("Select")
        self.problem_label.configure(text="Your diagnosis will appear here.")
        self.reason_label.configure(text="Reason: —")
        self.solution_label.configure(text="Suggested solution: —")


if __name__ == "__main__":
    app = NetworkExpertSystem()
    app.mainloop()
