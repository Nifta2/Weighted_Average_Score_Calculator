from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
Window.size = (380, 640)
Window.clearcolor = '#BFD3C1'
class CulculatorApp(App):

    def build(self):
        def calculate_bmi(instance):
            b = 0
            c = 0
            a = [0] * 16
            if a1.text == "":
                a[0] = 0
            else:
                a[0] = int(a1.text)
            if a2.text == "":
                a[1] = 0
            else:
                a[1] = int(a2.text)
            if a3.text == "":
                a[2] = 0
            else:
                a[2] = int(a3.text)
            if a4.text == "":
                a[3] = 0
            else:
                a[3] = int(a4.text)
            if a5.text == "":
                a[4] = 0
            else:
                a[4] = int(a5.text)
            if a6.text == "":
                a[5] = 0
            else:
                a[5] = int(a6.text)
            if a7.text == "":
                a[6] = 0
            else:
                a[6] = int(a7.text)
            if a8.text == "":
                a[7] = 0
            else:
                a[7] = int(a8.text)
            if a9.text == "":
                a[8] = 0
            else:
                a[8] = int(a9.text)
            if a10.text == "":
                a[9] = 0
            else:
                a[9] = int(a10.text)
            if a11.text == "":
                a[10] = 0
            else:
                a[10] = int(a11.text)
            if a12.text == "":
                a[11] = 0
            else:
                a[11] = int(a12.text)
            if a13.text == "":
                a[12] = 0
            else:
                a[12] = int(a13.text)
            if a14.text == "":
                a[13] = 0
            else:
                a[13] = int(a14.text)
            if a15.text == "":
                a[14] = 0
            else:
                a[14] = int(a15.text)
            if a16.text == "":
                a[15] = 0
            else:
                a[15] = int(a16.text)
            for i in range(16):
                if 0 < i + 1 <= 4:
                    if i + 1 == 1:
                        b += a[i] * 5 * 10
                        c += a[i] * 10
                    elif i + 1 == 2:
                        b += a[i] * 5 * 20
                        c += a[i] * 20
                    elif i + 1 == 3:
                        b += a[i] * 5 * 30
                        c += a[i] * 30
                    elif i + 1 == 4:
                        b += a[i] * 5 * 40
                        c += a[i] * 40
                elif 4 < i + 1 <= 8:
                    if i + 1 == 5:
                        b += a[i] * 4 * 10
                        c += a[i] * 10
                    elif i + 1 == 6:
                        b += a[i] * 4 * 20
                        c += a[i] * 20
                    elif i + 1 == 7:
                        b += a[i] * 4 * 30
                        c += a[i] * 30
                    elif i + 1 == 8:
                        b += a[i] * 4 * 40
                        c += a[i] * 40
                elif 8 < i + 1 <= 12:
                    if i + 1 == 9:
                        b += a[i] * 3 * 10
                        c += a[i] * 10
                    elif i + 1 == 10:
                        b += a[i] * 3 * 20
                        c += a[i] * 20
                    elif i + 1 == 11:
                        b += a[i] * 3 * 30
                        c += a[i] * 30
                    elif i + 1 == 12:
                        b += a[i] * 3 * 40
                        c += a[i] * 40
                elif 12 < i + 1 <= 16:
                    if i + 1 == 13:
                        b += a[i] * 2 * 10
                        c += a[i] * 10
                    elif i + 1 == 14:
                        b += a[i] * 2 * 20
                        c += a[i] * 20
                    elif i + 1 == 15:
                        b += a[i] * 2 * 30
                        c += a[i] * 30
                    elif i + 1 == 16:
                        b += a[i] * 2 * 40
                        c += a[i] * 40
            if b == 0:
                s=0.0
            elif b !=0:
                s = b / c
            s = round(s,2)
            print(s)
            result_culculator.text=f'Ваш бал: {s}!'
        def delete(instance):
            a1.text=""
            a2.text=""
            a3.text=""
            a4.text=""
            a5.text=""
            a6.text=""
            a7.text=""
            a8.text=""
            a9.text=""
            a10.text=""
            a11.text=""
            a12.text=""
            a13.text=""
            a14.text=""
            a15.text=""
            a16.text=""

        fl = FloatLayout()
        result_culculator = Label(text='Ваш бал: 0.00!', pos=(25, 500), size_hint=(0.194, 0.125), color='#000000')
        fl.add_widget(result_culculator)
        fl.add_widget(Label(text='Вес оценки:', pos=(15, 440), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='10', pos=(80, 440), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='20', pos=(150, 440), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='30', pos=(220, 440), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='40', pos=(290, 440), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='Пятёрка:', pos=(5, 400), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='Четвёрка:', pos=(5, 340), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='Тройка:', pos=(5, 280), size_hint=(0.194, 0.125), color='#000000'))
        fl.add_widget(Label(text='Двойка:', pos=(5, 220), size_hint=(0.194, 0.125), color='#000000'))

        x=[80,150,220,290]
        y=[420,360,300,240]
        a1 = TextInput(size_hint=(0.18, 0.0625),pos=(x[0], y[0]),background_color = '#FFE5D4')
        a2 = TextInput(size_hint=(0.18, 0.0625), pos=(x[1], y[0]),background_color = '#FFE5D4')
        a3 = TextInput(size_hint=(0.18, 0.0625), pos=(x[2], y[0]),background_color = '#FFE5D4')
        a4 = TextInput(size_hint=(0.18, 0.0625), pos=(x[3], y[0]),background_color = '#FFE5D4')

        a5 = TextInput(size_hint=(0.18, 0.0625), pos=(x[0], y[1]),background_color = '#FFE5D4')
        a6 = TextInput(size_hint=(0.18, 0.0625), pos=(x[1], y[1]),background_color = '#FFE5D4')
        a7 = TextInput(size_hint=(0.18, 0.0625), pos=(x[2], y[1]),background_color = '#FFE5D4')
        a8 = TextInput(size_hint=(0.18, 0.0625), pos=(x[3], y[1]),background_color = '#FFE5D4')

        a9 = TextInput(size_hint=(0.18, 0.0625), pos=(x[0], y[2]),background_color = '#FFE5D4')
        a10 = TextInput(size_hint=(0.18, 0.0625), pos=(x[1], y[2]),background_color = '#FFE5D4')
        a11 = TextInput(size_hint=(0.18, 0.0625), pos=(x[2], y[2]),background_color = '#FFE5D4')
        a12 = TextInput(size_hint=(0.18, 0.0625), pos=(x[3], y[2]),background_color = '#FFE5D4')

        a13 = TextInput(size_hint=(0.18, 0.0625), pos=(x[0], y[3]),background_color = '#FFE5D4')
        a14 = TextInput(size_hint=(0.18, 0.0625), pos=(x[1], y[3]),background_color = '#FFE5D4')
        a15 = TextInput(size_hint=(0.18, 0.0625), pos=(x[2], y[3]),background_color = '#FFE5D4')
        a16 = TextInput(size_hint=(0.18, 0.0625), pos=(x[3], y[3]),background_color = '#FFE5D4')

        fl.add_widget(a1)
        fl.add_widget(a2)
        fl.add_widget(a3)
        fl.add_widget(a4)

        fl.add_widget(a5)
        fl.add_widget(a6)
        fl.add_widget(a7)
        fl.add_widget(a8)

        fl.add_widget(a9)
        fl.add_widget(a10)
        fl.add_widget(a11)
        fl.add_widget(a12)

        fl.add_widget(a13)
        fl.add_widget(a14)
        fl.add_widget(a15)
        fl.add_widget(a16)

        button = Button(text='Рассчитать средневзвешенную оценку.',size_hint=(0.889, 0.0625), pos=(20, 170), color='#000000',background_color = '#EFC7C2')
        button.bind(on_press=calculate_bmi)
        fl.add_widget(button)
        button_clean = Button(text='Очистить.', size_hint=(0.444, 0.0625), pos=(20, 120), color='#000000',background_color = '#EFC7C2')
        button_clean.bind(on_press=delete)
        fl.add_widget(button_clean)

        return fl
CulculatorApp().run()
