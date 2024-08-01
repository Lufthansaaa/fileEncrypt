from binary import *
from hook import *

ext = input("Enter target file extension: ")


name = f"recon.{ext}"
url = input("Enter the webhook url: ")

webhook = DiscordWebhook(url=url, username=name)

# Convert the image back to binary
reconstructed_binary_data = image_to_binary('output_image.png')
with open(f'recon.{ext}', 'wb') as f:
    f.write(reconstructed_binary_data)

with open(f"recon.{ext}", "rb") as f:
    webhook.add_file(file=f.read(), filename=f"recon.{ext}")

response = webhook.execute()
