# Name: Nir Hemo


from tkinter import *
from PIL import Image, ImageTk


def rotate_picture(source_image_path, target_image_path):
    img_rotate = Image.open(source_image_path)          # open the photo
    w, h = img_rotate.size              # Get the size of the photo
    new_img_rotate = img_rotate.copy()          # copy the Image
    mtrx = img_rotate.load()
    mtrx_new = new_img_rotate.load()    # get the mtrix from the IMG
    for x in range(w):
        for y in range(h):
            mtrx_new[x, y] = mtrx[w - x - 1, h - y - 1]         # change the Image mtrix

    if target_image_path is not "":         # If for know if too return for Preview or to save
        new_img_rotate.save(target_image_path)
    else:
        return new_img_rotate


def mirror_picture(source_image_path, target_image_path):
    img_mirror = Image.open(source_image_path)                  # like the first function
    w, h = img_mirror.size
    new_img_mirror = img_mirror.copy()
    mtrx = img_mirror.load()
    mtrx_new = new_img_mirror.load()
    for x in range(w):
        for y in range(h):
            mtrx_new[x, y] = mtrx[w - x - 1, y]         # change the first line in the mtrix to the last one
    if target_image_path is not "":
        new_img_mirror.save(target_image_path)
    else:
        return new_img_mirror


def resize_picture(source_image_path, target_image_path):
    img_resize = Image.open(source_image_path).convert("L")
    w, h = img_resize.size
    mtrx = img_resize.load()
    new = Image.new("L", (int(w/2), int(h/2)))
    new_mtrx = new.load()
    for x in range(int(w / 2)):             # took every 4 pixel and divide by 4 to calculate the average and crate merge pixle
        for y in range(int(h / 2)):
            new_mtrx[x, y] = (mtrx[x * 2, y * 2] + mtrx[x * 2 + 1, y * 2] + mtrx[x * 2, y * 2 + 1] + mtrx[
                x * 2 + 1, y * 2 + 1]) // 4
    if target_image_path is not "":
        new.save(target_image_path)
    else:
        return new


def edge(source_image_path, target_image_path,threshold):
    img_edge = Image.open(source_image_path).convert("L")
    w, h = img_edge.size
    new_img_edge = img_edge.copy()
    mtrx = img_edge.load()
    mtrx_new = new_img_edge.load()
    for i in range(w - 1):      # check if the ABS difference is higher or smaller from the threshold from the pixel around it and give it black or white pixel
        for j in range(1, h):
            if abs(mtrx[i, j] - mtrx[i + 1, j]) > threshold or abs(mtrx[i, j] - mtrx[i, j - 1]) > threshold:
                mtrx_new[i, j] = 255
            else:
                mtrx_new[i, j] = 0
    if target_image_path is not "":
        new_img_edge.save(target_image_path)
    else:
        return new_img_edge


def get_pixel(image, i, j): # Get the pixel from the given image
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


def convert_grayscale(source_image_path, target_image_path):
    image = Image.open(source_image_path)
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = Image.new("RGB", (width, height), "white")
    pixels = new.load()

    # Transform to grayscale
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)

        # Get R, G, B values (This are int from 0 to 255)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # Transform to grayscale
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

            # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    if target_image_path is not "":
        new.save(target_image_path)
    else:
        return new
