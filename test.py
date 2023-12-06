import flet as ft
import os
import time

t1 = ft.Text(
     font_family="RobotoSlab"
)
t2 = ft.Text(
    size=100,
    weight=ft.FontWeight.W_900,
    text_align="CENTER",
    font_family="RobotoSlab")

def transmit(page, value, secret):
    t2.value = f"initializing..."
    page.update()
    n = 0
    length = len(value)
    for i in secret:
        nn = length-n
        if i == "1":
                os.system('stress-ng -c 12 -l 100 -q -t 2s')
                print('1')
                t2.value = f"transmitting:  '1'"
                page.update()
                n = n+1
        else:
                time.sleep(2)
                print('0')
                t2.value = f"transmitting:  '0'"
                page.update()
                n = n+1

def main(page: ft.Page):
    page.fonts = {
        "RobotoSlab": "https://github.com/blobject/agave/raw/master/dist/Agave-Bold-slashed.ttf"
    }
    page.title = "Covert Channel Demo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def button_clicked_binary(e):
        #t.value = f"Text:  '{tb.value}'."
        value = []
        for i in tb.value:
            text = ord(i)
            value.append(str(bin(text))[2:].zfill(8))
        value = str(value)
        t1.value = f"secret binary code:  '{value[1:-1]}'."
        page.update()
    
    def button_clicked_send(e):
        value = []
        secret = []
        for i in tb.value:
            text = ord(i)
            value.append(str(bin(text))[2:].zfill(8))
        value = " " + "".join(value)
        t1.value = f"secret binary code:  '{value}'."
        page.update()
        for i in value:
            secret.append(i)
        #print(secret)
        transmit(page, value, secret)
        page.update()

    
    tb = ft.TextField(
        label="enter your secret word",
        #on_change=textbox_changed,
    )
    b1 = ft.ElevatedButton(text="check binary code", on_click=button_clicked_binary)
    b2 = ft.ElevatedButton(text="TRANSMIT", on_click=button_clicked_send)

    page.add(tb, b1,b2, t1, t2)

ft.app(target=main)