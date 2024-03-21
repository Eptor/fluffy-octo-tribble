from PIL import Image, ImageDraw, ImageFont

# Load the image
image = Image.open('static/boleto.png')

# Set up the font size
font_size = 20

# Set up the font (using a basic built-in PIL font here)
font = ImageFont.load_default(font_size)

# Prepare to draw on the image
draw = ImageDraw.Draw(image)

# Define coordinates and color
x = [550, 940]
y = [35, 130]
color = "red"
image_paths = []

# Rectangle dimensions
rect_width = 40  # You may need to adjust this width
rect_height = font_size

for i in range(2):  # If you want to create tickets for numbers 0x0 to 0x9
    num = hex(i)

    # Create a new image object for each ticket to avoid overwriting
    image = Image.open(f'static/boleto.png')
    draw = ImageDraw.Draw(image)

    # Draw rectangles to cover existing numbers
    draw.rectangle([x[0], y[0], x[0] + rect_width, y[0]], fill="#EAEAEA")
    draw.rectangle([x[1], y[1], x[1] + rect_width, y[1]], fill="#EAEAEA")

    # Draw the hexadecimal number on the ticket
    draw.text((x[0], y[0]), num, fill=color, font=font)
    draw.text((x[1], y[1]), num, fill=color, font=font)

    # Save the edited image with a dynamic name indicating the number
    edited_img_path = f'static/boleto_{i}.png'
    image.save(edited_img_path)

    # Add the image path to our list
    image_paths.append(edited_img_path)

# Now we will create the PDF
pdf_path = 'static/tickets.pdf'
images = [Image.open(x) for x in image_paths]

# Convert all images to RGB mode and save as PDF
images_converted = [x.convert('RGB') for x in images]
images_converted[0].save(pdf_path, save_all=True, append_images=images_converted[1:])