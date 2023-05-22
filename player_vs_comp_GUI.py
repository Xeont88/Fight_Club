from tkinter import *
from Fighter import Fighter
from random import choice

root = Tk()
root.title('Бойцовский Клуб!!!')
root.geometry('450x150')

# Создаём фреймы слева и справа
frame_attack = Frame()
frame_defence = Frame()

# Создаём фрейм для текстового поля
text_frame = Frame()

# Размещаем фреймы слева и справа
frame_attack.pack(side='left', anchor='w')
frame_defence.pack(side='right', anchor='e')
text_frame.pack(side='bottom', anchor='s')

# переменная для хранения области для атаки
attack_var = IntVar()
attack_var.set(0)
# Создаем радиокнопки для выбора атаки
rb_attack_head = Radiobutton(frame_attack, text='Голова', variable=attack_var, value=0)
rb_attack_head.pack(anchor='w')
rb_attack_torso = Radiobutton(frame_attack, text='Торс', variable=attack_var, value=1)
rb_attack_torso.pack(anchor='w')
rb_attack_belt = Radiobutton(frame_attack, text='Пояс', variable=attack_var, value=2)
rb_attack_belt.pack(anchor='w')
rb_attack_legs = Radiobutton(frame_attack, text='Ноги', variable=attack_var, value=3)
rb_attack_legs.pack(anchor='w')

# переменная для хранения области для защиты
defense_var = IntVar()
defense_var.set(0)
# Создаем радиокнопки для выбора защиты
rb_defense_head = Radiobutton(frame_defence, text='Голова', variable=defense_var, value=0)
rb_defense_head.pack(anchor='w')
rb_defense_torso = Radiobutton(frame_defence, text='Торс', variable=defense_var, value=1)
rb_defense_torso.pack(anchor='w')
rb_defense_belt = Radiobutton(frame_defence, text='Пояс', variable=defense_var, value=2)
rb_defense_belt.pack(anchor='w')
rb_defense_legs = Radiobutton(frame_defence, text='Ноги', variable=defense_var, value=3)
rb_defense_legs.pack(anchor='w')

area_list = ["голову", "торс", "пояс", "ноги"]


def attack():
    # Получаем место защищаемое
    me.block(area_list[defense_var.get()])
    comp.block(choice(area_list))

    # Получаем место для удара
    me.hit(comp, area_list[attack_var.get()])
    comp.hit(me, choice(area_list))

    print(me.health, comp.health)


btn = Button(root, text='Ход', command=attack)
btn.pack(side='bottom')

log = Text(height=7, font='Times')
log.pack()

# Объявляем объекты бойцов
me = Fighter('Руслан', text_log=log)
comp = Fighter('ЧатБот ДжиПиТи', text_log=log)

root.mainloop()
