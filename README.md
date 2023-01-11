## Overview

This is a simple script that uses `pillow` to add text watermarks to images. At initial it creates empty folders (if they're not exist). Then it's reading contains of **input** folder using `os.walk()`, expecting to find images and put the list of files to a **JSON** file into **data** directory. It will raise an Exception if there're no files in the directory.<br>
After that the script is reading **JSON** file and adding text watermark to the specified coordinates.

## Settings

There're a some settings, that can be changed, they all storing in constants:<br>
`DIRS` contains the list of directories (for input, output and JSON file)<br>
`WATERMARK_FONT` is responsible for font, which will be used in watermark<br>
`WATERMARK_TEXT` is the watermark itself<br>
`MARGIN` is the margin between the watermark and image edge<br>
`PLACE` is where watermark should be placed (top left, top right, etc.)