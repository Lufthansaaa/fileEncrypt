from binary import *
from hook import *

ext = input("Enter target file extension: ")


name = f"recon.{ext}"
url = input("Enter the webhook url: ")

webhook = DiscordWebhook(url=url, username=name, avatar_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F236x%2Fa7%2Fd7%2Fb7%2Fa7d7b7ff01a18d719f63ccef5a699d29.jpg&f=1&nofb=1&ipt=4e4204fb6ef3e40184e35ab2aeeee996bca7d98a1283a487bb0cfde9b453bcb3&ipo=images", content="Decoded file")

# Convert the image back to binary
reconstructed_binary_data = image_to_binary('output_image.png')
with open(f'recon.{ext}', 'wb') as f:
    f.write(reconstructed_binary_data)

with open(f"recon.{ext}", "rb") as f:
    webhook.add_file(file=f.read(), filename=f"recon.{ext}")

response = webhook.execute()
