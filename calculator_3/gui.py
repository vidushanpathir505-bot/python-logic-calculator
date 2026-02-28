import tkinter as tk
import calculator_logic as cal

# //-----------------\\
FILE_PATH = 'calculator_3\\history.txt'
# //-----------------\\
        
def start_app():

        # //-----------------\\
        '''Getting valid input'''
        def get_input(widgest):
                return float(widgest.get().strip()) 
        
        # //-----------------\\
        '''Show the answer in answer label'''
        def show_answer(ans):
                return answer_value.config(text=ans)

        # //-----------------\\
        '''Show the history in history box'''       
        def show_history(text):
                current_text = history_box.cget("text")

                updated_text = current_text + "\n" + text

                history_box.config(text=updated_text)

        # //-----------------\\ 
        '''Save answers to history.txt file'''             
        def save_file(text):
                with open(FILE_PATH, 'a') as f:
                        f.write(text + '\n')

        # //-----------------\\
        '''Clear the input fields'''
        def clear_input():
                input_1.delete(0, tk.END)
                input_2.delete(0, tk.END)
                input_1.focus()

        # //-----------------\\
        '''Clear history bow'''
        def clear_history():
                history_box.config(text='')

        # //-----------------\\
        '''Calculate the answers and show result'''        
        def calculate(operator):

                if operator == '√':
                        value = input_1.get().strip()
                        if not value:
                                text = 'Number 1 is empty'
                                show_answer(text)
                                clear_input()
                        else:
                                num1 = float(value)
                                ans = cal.operations[operator](num1)
                                show_answer(ans)

                                new_result = f'sqrt({num1}) = {ans}'
                                show_history(text=new_result)
                                save_file(text=new_result)
                                clear_input()

                else: 
                        try:                              
                                num1 = get_input(input_1)
                                num2 = get_input(input_2)

                                ans = cal.operations[operator](num1, num2)

                                show_answer(ans=ans)

                                new_result = f'{num1} {operator} {num2} = {ans}'
                                show_history(text=new_result)
                                save_file(text=new_result)
                                clear_input()

                        except ValueError:
                                answer_value.config(text='Enter valid Numbers!')
                                clear_input()

        # //-----------------\\
        '''Create the window'''

        root = tk.Tk()
        root.title('Calculator')
        root.geometry('500x550')
        root.configure(bg='#2c3e50')

        root.grid_columnconfigure(0, weight=1)
       
        # //-----------------\\

        title_label = tk.Label(root,
                        text='CALCULATOR',
                        font=('Times New Roman', 20, 'bold'),
                        fg='white',
                        bg='#2c3e50')
        title_label.grid(row=0, pady=(20, 10))

        # //-----------------\\

        input_frame = tk.Frame(root,
                        width=380,
                        height=110,
                        bg='#34495e',
                        highlightbackground='#3498db',
                        highlightthickness=2)

        input_frame.grid(row=1, pady=10)
        input_frame.grid_propagate(False)

        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(2, weight=2)

        tk.Label(input_frame,
                text='Number 1:',
                font=('Times New Roman', 14, 'bold'),
                fg='#ecf0f1',  
                bg='#34495e'
                ).grid(row=0, column=1, padx=(20, 5), pady=(20, 10), sticky='e')

        input_1 = tk.Entry(input_frame,
                        font=('Times New Roman', 14),
                        bg='#ecf0f1',
                        fg='#2c3e50',
                        relief='solid',
                        borderwidth=1)
        input_1.grid(row=0, column=2, padx=(5, 20), pady=(20, 10), sticky='ew')

        tk.Label(input_frame,
                text='Number 2:',
                font=('Times New Roman', 14, 'bold'),
                fg='#ecf0f1',
                bg='#34495e'
                ).grid(row=1, column=1, padx=(20, 5), pady=(0, 20), sticky='e')

        input_2 = tk.Entry(input_frame,
                        font=('Times New Roman', 14),
                        bg='#ecf0f1',
                        fg='#2c3e50',
                        relief='solid',
                        borderwidth=1)
        input_2.grid(row=1, column=2, padx=(5, 20), pady=(0, 20), sticky='ew')

        # //-----------------\\

        button_frame = tk.Frame(root,
                                width=420,
                                height=120,
                                background='#2c3e50')

        button_frame.grid(row=3, pady=10)
        button_frame.grid_propagate(False)

        btn_add = tk.Button(button_frame, text='➕', font=('Times New Roman', 16, 'bold'),
                        width=4, height=2, bg='#27ae60', fg='white',
                        relief='raised', bd=3, activebackground='#2ecc71',
                        activeforeground='white', cursor='hand2', command=lambda: calculate('+'))
        btn_add.grid(row=0, column=0, padx=4, pady=10)

        btn_subtract = tk.Button(button_frame, text='➖', font=('Times New Roman', 16, 'bold'),
                                width=4, height=2, bg='#e67e22', fg='white',
                                relief='raised', bd=3, activebackground='#f39c12',
                                activeforeground='white', cursor='hand2', command=lambda: calculate('-'))
        btn_subtract.grid(row=0, column=1, padx=4, pady=10)

        btn_multiply = tk.Button(button_frame, text='✖', font=('Times New Roman', 16, 'bold'),
                                width=4, height=2, bg='#e74c3c', fg='white',
                                relief='raised', bd=3, activebackground='#c0392b',
                                activeforeground='white', cursor='hand2', command=lambda: calculate('*'))
        btn_multiply.grid(row=0, column=2, padx=4, pady=10)

        btn_divide = tk.Button(button_frame, text='➗', font=('Times New Roman', 16, 'bold'),
                                width=4, height=2, bg='#3498db', fg='white',
                                relief='raised', bd=3, activebackground='#2980b9',
                                activeforeground='white', cursor='hand2', command=lambda: calculate('/'))
        btn_divide.grid(row=0, column=3, padx=4, pady=10) 

        btn_power = tk.Button(button_frame, text='x²', font=('Times New Roman', 16, 'bold'),
                                width=4, height=2, bg='#9b59b6', fg='white',
                                relief='raised', bd=3, activebackground='#8e44ad',
                                activeforeground='white', cursor='hand2', command=lambda: calculate('**'))
        btn_power.grid(row=0, column=4, padx=4, pady=10) 

        btn_sqrt = tk.Button(button_frame, text='√', font=('Times New Roman', 16, 'bold'),
                                width=4, height=2, bg='#f1c40f', fg='white',
                                relief='raised', bd=3, activebackground='#f39c12',
                                activeforeground='white', cursor='hand2', command=lambda: calculate('√'))
        btn_sqrt.grid(row=0, column=5, padx=4, pady=10)

        # //-----------------\\

        answer_frame = tk.Frame(root,
                                bg='#34495e',
                                highlightbackground='#3498db',
                                highlightthickness=2)
        answer_frame.grid(row=4, padx=20, pady=10, sticky='ew')
        answer_frame.grid_columnconfigure(1, weight=1)

        tk.Label(answer_frame,
                text='Answer:',
                font=('Courier New', 14, 'bold'),
                fg='#ecf0f1',
                bg='#34495e'
                ).grid(row=0, column=0, padx=(10, 5), pady=10, sticky='w')
        
        answer_value = tk.Label(answer_frame,
                                text='',
                                font=('Courier New', 14, 'bold'),
                                fg='#f1c40f',
                                bg='#34495e',
                                relief='sunken',
                                bd=1,
                                width=10)
        
        answer_value.grid(row=0, column=1, padx=(5, 10), pady=10, sticky='ew')

        # //-----------------\\
        
        history_frame = tk.Frame(root, bg='#34495e', highlightbackground='#3498db', highlightthickness=2)
        history_frame.grid(row=8, pady=10, padx=20, sticky='ew')
        history_frame.grid_columnconfigure(0, weight=1)

        tk.Label(history_frame,
                text='History',
                font=('Courier New', 14, 'bold'),
                fg='#ecf0f1',
                bg='#34495e'
                ).grid(row=0, column=0, pady=(10, 5), sticky='w', padx=10)

        
        history_box = tk.Label(history_frame, font=('Courier New', 14, 'bold'), bg='#2c3e50', highlightbackground='#3498db', highlightthickness=1)
        history_box.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='ew')

        # //-----------------\\

        tk.Button(history_frame,
                text='CLEAR HISTORY',
                font=('Courier New', 10, 'bold'),
                bg='#e74c3c',        
                fg='white',           
                activebackground='#a93226', 
                activeforeground='white',
                bd=0,                 
                padx=10,
                pady=5,
                cursor="hand2",
                command=clear_history).grid(row=2, column=0, pady=(0, 10),)
        
        # //-----------------\\

        '''Run the main loop'''
        root.mainloop()


      