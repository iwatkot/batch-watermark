import os
import json

from PIL import Image, ImageDraw, ImageFont

INPUT_DIR = './input/'
OUTDPUT_DIR = './output/'
DATA_DIR = './data/'
DIRS = [INPUT_DIR, OUTDPUT_DIR, DATA_DIR]
JSON_FILENAMES = 'filenames.json'
# Watermark settings.
WATERMARK_FONT = ImageFont.truetype('arial.ttf', 72)
WATERMARK_TEXT = 'WATERMARK'
# Choose the place where watermark should appear:
# TOPLEFT, TOPRIGHT, BOTLEFT, BOTRIGHT.
PLACE = 'TOPLEFT'
MARGIN = 30


def make_dirs():
    for dir in DIRS:
        try:
            os.mkdir(dir)
        except FileExistsError:
            pass


def pack_filenames_to_json():
    filenames = list(os.walk(INPUT_DIR))[0][2]
    if not filenames:
        raise Exception("There's no files in /input folder.")
    with open(DATA_DIR+JSON_FILENAMES, 'w') as jfnms:
        json.dump(filenames, jfnms, indent=1)


def add_watermark_to_image():
    with open(DATA_DIR+JSON_FILENAMES) as jfnms:
        filenames = json.load(jfnms)
    for filename in filenames:
        filepath = INPUT_DIR + filename
        picture = Image.open(filepath)
        draw = ImageDraw.Draw(picture)
        picsize = picture.size
        wmsize = draw.textsize(WATERMARK_TEXT, WATERMARK_FONT)
        x, y = calculate_coordinates(picsize, wmsize, PLACE)
        draw.text((x, y), WATERMARK_TEXT, font=WATERMARK_FONT)
        picture.save(f"{OUTDPUT_DIR}{filename}")


def calculate_coordinates(picsize, wmsize, place):
    image_width, image_height = picsize
    watermark_width, watermark_height = wmsize
    if place == 'TOPLEFT':
        x = y = MARGIN
    elif place == 'TOPRIGHT':
        y = MARGIN
        x = image_width - MARGIN - watermark_width
    elif place == 'BOTLEFT':
        x = MARGIN
        y = image_height - MARGIN - watermark_height
    elif place == 'BOTRIGHT':
        x = image_width - MARGIN - watermark_width
        y = image_height - MARGIN - watermark_height
    return x, y


def main():
    make_dirs()
    pack_filenames_to_json()
    add_watermark_to_image()


if __name__ == '__main__':
    main()
