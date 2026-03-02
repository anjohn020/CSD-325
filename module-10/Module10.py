import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        self.tasks = [] if not tasks else tasks

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Johnson-ToDo")  # my last name
        self.geometry("300x400")

        # Menu colors + File Exit
        menubar = tk.Menu(self)
        file_menu = tk.Menu(
            menubar,
            tearoff=0,
            background="#1E3A8A",
            foreground="#F59E0B",
            activebackground="#F59E0B",
            activeforeground="#1E3A8A"
        )
        file_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

        # Instructions label
        self.instructions = tk.Label(
            self.text_frame,
            text="Instructions: Press Enter to add a task. Right-click a task to delete it."
        )

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="n"
        )

        self.instructions.pack(side=tk.TOP, fill=tk.X)
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Purple / Yellow alternating task colors
        self.colour_schemes = [
            {"bg": "#7C3AED", "fg": "white"},  # purple
            {"bg": "#FACC15", "fg": "black"}   # yellow
        ]

        # First placeholder label
        todo1 = tk.Label(
            self.tasks_frame,
            text="--- Add Items Here ---",
            pady=10,
            bd=1,
            relief="solid"
        )
        self.set_task_colour(0, todo1)

        # Right-click delete
        todo1.bind("<Button-3>", self.remove_task)
        todo1.bind("<Button-2>", self.remove_task)  # mac compatibility

        self.tasks.append(todo1)
        todo1.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)

        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)

        self.tasks_canvas.bind("<Configure>", self.task_width)

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if task_text:
            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                pady=10,
                bd=1,
                relief="solid"
            )

            # Color it based on where it will be in the list
            self.set_task_colour(len(self.tasks), new_task)

            # Right-click delete
            new_task.bind("<Button-3>", self.remove_task)
            new_task.bind("<Button-2>", self.remove_task)

            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, choice = divmod(position, 2)
        scheme = self.colour_schemes[choice]
        task.configure(bg=scheme["bg"], fg=scheme["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    Todo().mainloop()