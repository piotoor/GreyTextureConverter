from PIL import Image
import numpy as np


def convert_image_to_grey_format(input_img, half=True):
    pixels = np.transpose(np.array(list(input_img.getdata())).reshape((13 if half else 25, 16)))
    asm_code_lines = ["byte " + ", ".join(map(str, x[:13])) for x in pixels]
    # print(pixels)
    # print(np.transpose(pixels))
    print(asm_code_lines)
    return asm_code_lines

# def convert_image_to_grey_format(input_img, half=True):
#     pixels = np.transpose(np.array(list(input_img.getdata())).reshape((13 if half else 25, 16)))
#     asm_code_lines = ["byte " + ", ".join(map(str, x)) for x in pixels]
#     # print(pixels)
#     # print(np.transpose(pixels))
#     print(asm_code_lines)
#     return asm_code_lines


if __name__ == '__main__':
    path = "wall_test.tga"
    img = Image.open(path)
    asm_code = convert_image_to_grey_format(img)

    pass
