#! /c/c64dev/projects/textureLoader/venv/Scripts/python.exe
from PIL import Image
import numpy as np
import os
import argparse

DST_EXTENSION = ".asm"


def convert_image_to_asm_code(input_img, full_size=False):
    pixels = np.transpose(np.array(list(input_img.getdata())).reshape((25 if full_size else 13, 16)))
    asm_code_lines = ["byte " + ", ".join(map(str, x[:13])) for x in pixels]
    return asm_code_lines


def save_image_to_asm_files(file_path, full_size=False):
    print("Processing {}".format(file_path))
    curr_img = Image.open(file_path)
    head, tail = os.path.splitext(file_path)
    asm_file_path = head + DST_EXTENSION
    with open(asm_file_path, 'w') as asm_file:
        asm_file.write("\n".join(convert_image_to_asm_code(curr_img, full_size)))


def save_images_to_asm_files(textures_dir, extension="tga", full_size=False):
    files_in_path = [x for x in os.listdir(textures_dir) if x.endswith(extension)]
    for src_file in files_in_path:
        full_src_file_path = os.path.join(textures_dir, src_file)
        save_image_to_asm_files(full_src_file_path, full_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--single-file',
                        required=False,
                        dest='single',
                        action='store_true')
    parser.add_argument('-f', '--full_size',
                        required=False,
                        dest='full_size',
                        action='store_true')
    parser.add_argument('path',
                        type=str)
    args = parser.parse_args()

    if args.single:
        save_image_to_asm_files(args.path, args.full_size)
    else:
        save_images_to_asm_files(args.path, "tga", args.full_size)


