from binary import *
from hook import *

name = input("Enter name of the file (with extension): ")
url = input("Enter the webhook url: ")

embed = DiscordEmbed(title="File encrypted", description=f"File: {name}", color=0x3633ff)


dot_index = name.rfind(".")
file_extension = name[dot_index + 1:] if dot_index != -1 else ""

webhook = DiscordWebhook(url=url, username=name, avatar_url="https://avatars0.githubusercontent.com/u/14542790")

# Example usage:
# Convert a binary file to an image
binary_data = file_to_binary(f'{name}')
binary_to_image(binary_data, f'output_image.png')

with open('output_image.png', 'rb') as f:
    webhook.add_file(file=f.read(), filename='pixels.png')

embed.set_author(name="Image Encrypt",icon_url="https://avatars0.githubusercontent.com/u/14542790")
embed.set_image(url="attachment://pixels.png")

webhook.add_embed(embed)

response = webhook.execute()
