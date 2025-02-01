# Install necessary libraries
!pip install pillow matplotlib ipywidgets

# Import required libraries
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interactive

# Function to create a logo
def create_logo(text, shape, text_color, shape_color, font_size, save=False):
    # Create a blank image with white background
    width, height = 500, 500
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    
    # Load font
    font = ImageFont.load_default()
    
    # Draw shape (circle or rectangle)
    if shape == 'Circle':
        draw.ellipse([(width/4, height/4), (width*3/4, height*3/4)], fill=shape_color)
    elif shape == 'Rectangle':
        draw.rectangle([(width/4, height/4), (width*3/4, height*3/4)], fill=shape_color)
    
    # Add text in the center
    text_width, text_height = draw.textsize(text, font=font)
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, fill=text_color, font=font)
    
    # Display the image using matplotlib
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    
    # Optionally save the logo to a file
    if save:
        image.save('logo.png')
        print("Logo saved as 'logo.png'")

# Create interactive widgets
text_widget = widgets.Text(value='My Logo', description='Text:')
shape_widget = widgets.Dropdown(
    options=['Circle', 'Rectangle'],
    value='Circle',
    description='Shape:'
)
text_color_widget = widgets.ColorPicker(value='black', description='Text Color:')
shape_color_widget = widgets.ColorPicker(value='blue', description='Shape Color:')
font_size_widget = widgets.IntSlider(value=30, min=10, max=100, step=5, description='Font Size:')
save_widget = widgets.Checkbox(value=False, description="Save Logo")

# Create interactive plot
interactive_plot = interactive(create_logo, 
                               text=text_widget,
                               shape=shape_widget,
                               text_color=text_color_widget,
                               shape_color=shape_color_widget,
                               font_size=font_size_widget,
                               save=save_widget)

# Display the widgets
interactive_plot

