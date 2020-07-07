from tkinter import Entry, Label, Button, Tk

from webhook import MessageSender
from webhook.WebhookCreator import WebhookCreator


class GuiHandler:
    def __init__(self):
        self._title = "Brandon's Discord Webhook Sender"

    def setup(self):
        root = Tk()
        root.title(self._title)
        # this will create a label widget
        url_label = Label(root, text="Webhook URL:")
        content_label = Label(root, text="Message:")
        username_label = Label(root, text="Username:")
        avatar_label = Label(root, text="Avatar URL:")

        # grid method to arrange labels in respective
        # rows and columns as specified
        url_label.grid(row=1, column=0, pady=2)
        username_label.grid(row=0, column=0, pady=2)
        avatar_label.grid(row=2, column=0, pady=2)
        content_label.grid(row=3, column=0, pady=2)

        # entry widgets, used to take entry from user
        hook_url = Entry(root, width=90)
        content = Entry(root, width=90)
        username = Entry(root)
        avatar_url = Entry(root, width=90)

        # place entries to grid
        hook_url.grid(row=1, column=1, pady=2)
        username.grid(row=0, column=1, pady=2)
        avatar_url.grid(row=2, column=1, pady=2)
        content.grid(row=3, column=1, pady=2)

        # Buttons
        send_message_button = Button(root, padx=10, pady=5, text="Send Message",
                                     command=lambda: self.send_message(entry=hook_url, message_entry=content,
                                                                       avatar_url=avatar_url, username=username,
                                                                       root=root))
        quit_button = Button(root, padx=10, pady=5, text="Quit Program", command=root.quit)

        # place buttons on grid
        send_message_button.grid(row=4, column=0)
        quit_button.grid(row=4, column=2)

        # main loop
        root.resizable(False, False)
        root.mainloop()

    # TODO send a successful message, or make a chat box logs when clicking "Send Message" Button
    def send_message(self, entry, message_entry, avatar_url, username, root):
        url = entry.get()
        message = message_entry.get()
        username = username.get()
        avatar_url = avatar_url.get()
        webhook_creator = WebhookCreator(url=str(url), message=str(message), username=str(username),
                                         avatar_url=str(avatar_url))
        try:
            MessageSender.send_basic_webhook_message(webhook_creator)
        except:
            # TODO fix this not sending error message
            root.messagebox.showerror(title="Error", message="Please input all fields correctly")

    # def start_discord_rpc(self):
    #     discord_rpc.initialize('722899544957911042', log=False)
    #     discord_rpc.update_presence(
    #         **{
    #             'details': '@Author Not Brandon#4444',
    #             'large_image_key': 'default'
    #         }
    #     )
    #     discord_rpc.update_connection()
    # TODO Get Discord Rich Presence Working

    def start(self):
        self.setup()