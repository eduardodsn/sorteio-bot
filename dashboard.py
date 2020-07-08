import time
from tkinter import *
from usuals import run_bot
from tkinter import scrolledtext


class Dashboard:
    def __init__(self):
        self.bg_color = '#151515'
        self.fg_color = '#edf2f4'
    

    def create_dashboard(self):
        self.screen = Tk()
        self.screen.geometry('350x500')
        self.screen.title('Bot')
        self.screen.tk.call('wm', 'iconphoto', self.screen._w, PhotoImage(file='robo.png'))
        self.screen.configure(bg=self.bg_color)
        self.screen.resizable(False, False)

    
    def create_log_screen(self):
        self.log = Toplevel()
        self.log.geometry('350x350')
        self.log.title('Log')
        self.log.tk.call('wm', 'iconphoto', self.log._w, PhotoImage(file='robo.png'))
        self.log.configure(bg='#151515')
        self.log.resizable(False, False)
        return self.log


    def create_log_scrolled_text(self, tela):
        scrolled_text = scrolledtext.ScrolledText(tela, width=40, height=20, bg="#1D1D1D", fg="white")
        scrolled_text.place(relx=0.5, rely=0.5, anchor=CENTER)
        return scrolled_text


    def create_labels(self):
        self.generate_label('Sorteio Bot', 30, 0.19, 0.11)
        self.generate_label('Login do Instagram:', 11, 0.02, 0.3)
        self.generate_label('Senha do Instagram:', 11, 0.02, 0.4)
        self.generate_label('Link do sorteio:', 11, 0.02, 0.5)
        self.generate_label('Quantos marcar (por comentário):', 11, 0.02, 0.6)
        self.generate_label('Mostrar navegador?', 11, 0.02, 0.7)


    def create_entries(self):
        selected = StringVar()

        login_field = self.generate_entry('Digite seu login...', '', 20, 0.50, 0.3)
        pass_field = self.generate_entry('', '●', 20, 0.50, 0.4)
        link_field = self.generate_entry('Cole o link aqui...', '', 26, 0.38, 0.5)
        qnt_field = self.generate_entry('Qnt...', '', 5, 0.78, 0.6)
        self.generate_radio('Sim', 'yes', selected, 0.5, 0.7)
        self.generate_radio('Não', 'no', selected, 0.7, 0.7)
        
        self.create_button(login_field, pass_field, link_field, qnt_field, selected)


    def create_button(self, login_field, pass_field, link_field, qnt_field, selected):
        button = Button(self.screen, text='Iniciar bot', bg='white', fg='black', command=lambda:    run_bot(login_field.get(), pass_field.get(), link_field.get(), qnt_field.get(), selected.get()))
        button.place(relx=0.5, rely=0.9, anchor=CENTER)
    

    def generate_log(self, tela, box, message):
        box.insert(END, message + '\n')
        tela.update()

    
    def generate_label(self, text, font_size, x, y):
        new_label = Label(self.screen, text=text, font=('Ubuntu', font_size), bg=self.bg_color, fg=self.fg_color)
        new_label.place(relx=x, rely=y, anchor=W)


    def generate_entry(self, placeholder, to_show, width, x, y):
        new_entry = Entry(self.screen, width=width, show=to_show, bg=self.fg_color, borderwidth=0.5)
        new_entry.insert(0, placeholder)
        new_entry.bind("<FocusIn>", lambda args: new_entry.delete('0', 'end'))
        new_entry.place(relx=x, rely=y, anchor=W)
        return new_entry

    
    def generate_radio(self, text, value, variable, x, y):
        new_radio = Radiobutton(self.screen, text=text, value=value, fg='white', bg='#151515', activebackground='#151515',
                    activeforeground='white', selectcolor='#151515', variable=variable)
        new_radio.place(relx=x, rely=y, anchor=W)
        new_radio.select()

        return new_radio


def export_dashboard():
    dashboard = Dashboard()
    dashboard.create_dashboard()
    dashboard.create_labels()
    dashboard.create_entries()
    dashboard.screen.mainloop()
