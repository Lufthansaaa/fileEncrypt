from binary import *
from hook import *

name = input("Enter name of the file (with extension): ")
url = input("Enter the webhook url: ")

embed = DiscordEmbed(title="File encrypted", description=f"File: {name}", color=0x3633ff)


dot_index = name.rfind(".")
file_extension = name[dot_index + 1:] if dot_index != -1 else ""

webhook = DiscordWebhook(url=url, username=name, avatar_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F236x%2Fa7%2Fd7%2Fb7%2Fa7d7b7ff01a18d719f63ccef5a699d29.jpg&f=1&nofb=1&ipt=4e4204fb6ef3e40184e35ab2aeeee996bca7d98a1283a487bb0cfde9b453bcb3&ipo=images")

# Example usage:
# Convert a binary file to an image
binary_data = file_to_binary(f'{name}')
binary_to_image(binary_data, f'output_image.png')

with open('output_image.png', 'rb') as f:
    webhook.add_file(file=f.read(), filename='pixels.png')

embed.set_author(name="Image Encrypt",icon_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F236x%2Fa7%2Fd7%2Fb7%2Fa7d7b7ff01a18d719f63ccef5a699d29.jpg&f=1&nofb=1&ipt=4e4204fb6ef3e40184e35ab2aeeee996bca7d98a1283a487bb0cfde9b453bcb3&ipo=images", url="https://github.com/Lufthansaaa")
embed.set_image(url="attachment://pixels.png")

webhook.add_embed(embed)

response = webhook.execute()
