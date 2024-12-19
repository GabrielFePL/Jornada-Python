import flet as ft
def main(page):
    title = ft.Text('Hashzap')
    popup_title = ft.Text('Welcome to Hashzap')
    popup_input_name = ft.TextField(label='Register your name to chat:')
    chat = ft.Column()
    def websocket_send(message):
        text_chat = ft.Text(message)
        chat.controls.append(text_chat)
        page.update()
    page.pubsub.subscribe(websocket_send)
    def send_message(event):
        message_text = chat_input_message.value
        user_name = popup_input_name.value
        message = f'{user_name}: {message_text}'
        page.pubsub.send_all(message)
        message_text = ''
        page.update()
    chat_input_message = ft.TextField(label='Text message', on_submit=send_message)
    chat_send_button = ft.ElevatedButton('Send', on_click=send_message)
    chat_row_input_send = ft.Row([chat_input_message, chat_send_button])
    def open_chat(event):
        page.remove(title)
        page.remove(start_button)
        popup.open = False
        page.add(chat)
        page.add(chat_row_input_send)
        message = f'{popup_input_name.value} joined the chat'
        page.pubsub.send_all(message)
        page.update()
    popup_button = ft.ElevatedButton('Start Chat', on_click=open_chat)
    popup = ft.AlertDialog(
        title=popup_title, 
        content=popup_input_name, 
        actions=[popup_button])
    def start_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()
    start_button = ft.ElevatedButton('Start Chat', on_click=start_chat)
    page.add(title)
    page.add(start_button)
ft.app(main, view=ft.WEB_BROWSER)