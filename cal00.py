import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("เครื่องคิดเลข")
        self.root.geometry("350x500")
        self.root.configure(bg="#17171c")
        self.root.resizable(False, False)

        self.expression = ""

        # หน้าจอแสดงผล
        self.display_var = tk.StringVar(value="0")
        self.display_label = tk.Label(
            root, 
            textvariable=self.display_var, 
            font=("Helvetica", 36), 
            anchor="e", 
            bg="#17171c", 
            fg="#ffffff", 
            padx=20, 
            pady=20
        )
        self.display_label.pack(expand=True, fill="both")

        # เฟรมสำหรับวางปุ่ม
        self.buttons_frame = tk.Frame(root, bg="#17171c")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # รูปแบบปุ่มและการจัดวาง (Layout)
        buttons = [
            ('C', '#a5a5a5', '#000000', 0, 0), ('±', '#a5a5a5', '#000000', 0, 1), ('%', '#a5a5a5', '#000000', 0, 2), ('/', '#ff9f0a', '#ffffff', 0, 3),
            ('7', '#333333', '#ffffff', 1, 0), ('8', '#333333', '#ffffff', 1, 1), ('9', '#333333', '#ffffff', 1, 2), ('*', '#ff9f0a', '#ffffff', 1, 3),
            ('4', '#333333', '#ffffff', 2, 0), ('5', '#333333', '#ffffff', 2, 1), ('6', '#333333', '#ffffff', 2, 2), ('-', '#ff9f0a', '#ffffff', 2, 3),
            ('1', '#333333', '#ffffff', 3, 0), ('2', '#333333', '#ffffff', 3, 1), ('3', '#333333', '#ffffff', 3, 2), ('+', '#ff9f0a', '#ffffff', 3, 3),
            ('0', '#333333', '#ffffff', 4, 0), ('.', '#333333', '#ffffff', 4, 2), ('=', '#ff9f0a', '#ffffff', 4, 3)
        ]

        # ตั้งค่าการขยายตัวของช่องตาราง (Grid)
        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)

        # สร้างปุ่มลงบนหน้าจอ
        for (text, bg, fg, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            
            # กรณีปุ่มเลข 0 ให้ขยายกว้าง 2 ช่อง
            if text == '0':
                btn = tk.Button(self.buttons_frame, text=text, bg=bg, fg=fg, font=("Helvetica", 18, "bold"), borderwidth=0, activebackground="#555555", command=action)
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            elif text == '.':
                btn = tk.Button(self.buttons_frame, text=text, bg=bg, fg=fg, font=("Helvetica", 18, "bold"), borderwidth=0, activebackground="#555555", command=action)
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            else:
                btn = tk.Button(self.buttons_frame, text=text, bg=bg, fg=fg, font=("Helvetica", 18, "bold"), borderwidth=0, command=action)
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("0")
        
        elif char == '±':
            if self.expression:
                if self.expression.startswith('-'):
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
                self.display_var.set(self.expression)
        
        elif char == '%':
            if self.expression:
                try:
                    self.expression = str(float(self.expression) / 100)
                    self.display_var.set(self.expression)
                except:
                    self.display_var.set("Error")
                    self.expression = ""

        elif char == '=':
            try:
                # คำนวณผลลัพธ์จากข้อความทางคณิตศาสตร์
                result = eval(self.expression)
                # จัดการทศนิยมไม่ให้ยาวเกินไป
                if isinstance(result, float):
                    result = round(result, 8)
                self.display_var.set(result)
                self.expression = str(result)
            except Exception:
                self.display_var.set("Error")
                self.expression = ""
        
        else:
            # ป้องกันไม่ให้ขึ้นเลข 0 นำหน้าโดยไม่จำเป็น
            if self.display_var.get() == "0" and char != '.':
                self.expression = char
            else:
                self.expression += char
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
