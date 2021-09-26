import os

from PIL import Image

# Crops the image and saves it as "new_filename"
def crop_image(img, crop_area, new_filename):
    cropped_image = img.crop(crop_area)
    cropped_image.save(new_filename)

# The x, y coordinates of the areas to be cropped. (x1, y1, x2, y2)
crop_areas = [(760, 300, 1160, 600)]

image_names = ['images/6dof_raw/6dof_pybullet1.png',
              'images/6dof_raw/6dof_pybullet2.png',
              'images/6dof_raw/6dof_pybullet3.png',
              'images/6dof_raw/6dof_pybullet4.png',
              'images/6dof_raw/6dof_pybullet5.png']

for image_name in image_names:
    
    img = Image.open(image_name)

    # Loops through the "crop_areas" list and crops the image based on the coordinates in the list
    for i, crop_area in enumerate(crop_areas):
        filename = os.path.splitext(image_name)[0]
        ext = os.path.splitext(image_name)[1]
        new_filename = filename + '_cropped' + ext

        crop_image(img, crop_area, new_filename)