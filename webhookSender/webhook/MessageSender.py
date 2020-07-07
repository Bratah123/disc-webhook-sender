from discord_webhook import DiscordWebhook


def send_basic_webhook_message(webhook_creator): # sends just a regular discord message
    webhook = DiscordWebhook(url=webhook_creator.url, content=webhook_creator.message,
                             avatar_url=webhook_creator.avatar_url, username=webhook_creator.username)
    response = webhook.execute()


def send_multi_webhook(webhook_creator, multi_url): # multi_url parameter takes in an array of webhook URLs
    webhook = DiscordWebhook(url=multi_url, content=webhook_creator.message,
                             avatar_url=webhook_creator.avatar_url, username=webhook_creator.username)
    response = webhook.execute()


# TODO Implement embedded message system into GUI
def send_embed_message(webhook_creator, embed): # embed parameter takes in an embeded message using DiscordEmbed()
    webhook = DiscordWebhook(url=webhook_creator.url, content=webhook_creator.message,
                             avatar_url=webhook_creator.avatar_url, username=webhook_creator.username)
    webhook.add_embed(embed)
    response = webhook.execute()
