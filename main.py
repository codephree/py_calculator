import tkinter as tk 
import customtkinter as ctk

previous = '0'
result = ''

app = ctk.CTk()
app.title("My Codephree Calculator")
app.geometry('300x350')

def clear_screen():
    global previous
    previous = '0'
    display_string.set(value=previous)

def add_negative():
    global previous
    if previous  != '0':
        if previous[0] != '-':
            previous = '-'+previous
        else:
           previous = previous[1:]
    display_string.set(previous)

def remove_display():
    global previous
    if previous != "0":
        previous = previous.rstrip() 
   
    print(previous)
     
    display_string.set(value=previous)

def numberpressed(number_pressed):
    global previous 
    global result

    if result != '':
        previous ='0'
        # previous = result
        result = ''
    
    if previous == '0':
        previous = ''
        previous += number_pressed
    else:
        previous += number_pressed
    display_string.set(previous)

def calcultate(operator):
    global previous 
    global result 
    try:
        match operator:
            case '=':
              previous = str(eval(previous))
              # also set sum 
              result = previous
              display_string.set(str(previous))
            case '%':
                previous =  str (float(previous)/100)
                result = previous
                display_string.set(str(previous))
    except:
        display_string.set('Error')

display_font = ctk.CTkFont(family='MTN Brighter Sans ExtraBold Italic', size=20, weight='bold', slant='italic')
display_string = ctk.StringVar(value=str(previous))
display = ctk.CTkEntry(master=app, width=280, 
                       textvariable=display_string,
                       height=50, 
                       corner_radius=5, justify='right', state= 'disabled',
                       font=display_font)
display.place(x=10,y=10)

button_frame = ctk.CTkFrame(master=app, width=280, height=220, fg_color='transparent')
button_frame.place(x=10,y=68)


buttonclear = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='AC', 
                            font=display_font, command=clear_screen)
buttonclear.grid(row=0, column=0, ipadx=5, padx=3)

buttonne = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, border_width=0,
                          text='-/+', font=display_font, command=add_negative)
buttonne.grid(row=0, column=1,ipadx=5)

buttonp = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='%', 
                        font=display_font,command=lambda: calcultate('%'))
buttonp.grid(row=0, column=2,ipadx=5, padx=5)

button7 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='7',
                         font=display_font, command=lambda: numberpressed('7'))
button7.grid(row=1, column=0, ipadx=5, padx=3,pady=5)

button8 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='8', 
                        font=display_font,command=lambda: numberpressed('8'))
button8.grid(row=1, column=1,ipadx=5)

button9 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='9',
                         font=display_font,command=lambda: numberpressed('9'))
button9.grid(row=1, column=2,ipadx=5, padx=5)

buttondivi = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='/',
                            font=display_font, command=lambda: numberpressed('/'))
buttondivi.grid(row=0, column=3)

button4 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='4',
                         font=display_font,command=lambda: numberpressed('4'))
button4.grid(row=2, column=0, ipadx=5, padx=3, pady=3)

button5 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='5',
                         font=display_font,
                         command=lambda: numberpressed('5'))
button5.grid(row=2, column=1,ipadx=5)

button6 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='6', 
                        font=display_font,command=lambda: numberpressed('6'))
button6.grid(row=2, column=2,ipadx=5, padx=5)

buttontimes = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='x', 
                            font=display_font,  command=lambda: numberpressed('*'))
buttontimes.grid(row=1, column=3)

button1 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='1',
                         font=display_font, command=lambda: numberpressed('1'))
button1.grid(row=3, column=0, ipadx=5, padx=3)

button2 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='2', 
                        font=display_font, command=lambda: numberpressed('2'))
button2.grid(row=3, column=1,ipadx=5)

button3 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='3', 
                        font=display_font, command=lambda: numberpressed('3'))
button3.grid(row=3, column=2,ipadx=5, padx=5)

buttonminus = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='-', 
                            font=display_font,  command=lambda: numberpressed('-'))
buttonminus.grid(row=2, column=3)

button0 = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='0', 
                        font=display_font, command=lambda: numberpressed('0'))
button0.grid(row=4, column=0, ipadx=5, padx=3, pady=5)

buttondot = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='.', 
                          font=display_font, command=lambda: numberpressed('.'))
buttondot.grid(row=4, column=1,ipadx=5)

buttonequal = ctk.CTkButton(master=button_frame, 
                            width=60,height=50,corner_radius=0, 
                            text='=', 
                            # fg_color='white',
                            font=display_font, command=lambda: calcultate('='))
buttonequal.grid(row=4, column=2,ipadx=5, padx=5)

buttonplus = ctk.CTkButton(master=button_frame, width=60,height=50,corner_radius=0, text='+', 
                           font=display_font,  command=lambda: numberpressed('+'))
buttonplus.grid(row=3, column=3)

buttonq = ctk.CTkButton(master=button_frame, 
                            width=60,height=50,corner_radius=0, 
                            text='DEL', 
                            fg_color='red',
                            text_color='black',
                            hover_color='white',
                            font=display_font,
                            command=remove_display)
buttonq.grid(row=4, column=3, padx=0)

app.mainloop()