#! /c/c64dev/projects/textureLoader/venv/Scripts/python.exe
from PIL import Image
import numpy as np
import os
import argparse

DST_EXTENSION = ".asm"


def convert_image_to_asm_code_80x50(input_img, full_size):
    pixels = np.array(list(input_img.getdata())).reshape((50 if full_size else 26, 32))[:26]
    print("pixels raw = {}".format(pixels))
    screen_buffer_pixels = []
    color_buffer_pixels = []

    for r in range(0,len(pixels), 2):
        for c in range(0, len(pixels[r]), 2):
            screen_buffer_pixels.append((pixels[r][c] << 4) | pixels[r + 1][c + 1])
            color_buffer_pixels.append(pixels[r][c + 1])

    print("separeted: \n{}\n\n{}".format(np.array(screen_buffer_pixels).reshape(13, 16), np.array(color_buffer_pixels).reshape(13, 16)))

    asm_code_screen_buffer = ["\tbyte " + ", ".join(map(str, x)) for x in np.array(screen_buffer_pixels).reshape(13, 16)]
    asm_code_color_buffer = ["\tbyte " + ", ".join(map(str, x)) for x in np.array(color_buffer_pixels).reshape(13, 16)]
    print(asm_code_screen_buffer)
    print("\n")
    print(asm_code_color_buffer)

    return asm_code_screen_buffer, asm_code_color_buffer


def save_image_to_asm_files_80x50(file_path, full_size):
    print("Processing {}".format(file_path))
    curr_img = Image.open(file_path)
    head, tail = os.path.split(file_path)
    src_file_name, ext = os.path.splitext(tail)

    sbf, cbf = convert_image_to_asm_code_80x50(curr_img, full_size)
    sbf_asm_file_path = os.path.join(head, "..", src_file_name) + DST_EXTENSION
    cbf_asm_file_path = os.path.join(head, "..", src_file_name + "b") + DST_EXTENSION
    with open(sbf_asm_file_path, 'w') as asm_file:
        print("Saving {}...".format(sbf_asm_file_path))
        screen_buffer_output = "\n".join(sbf)
        asm_file.write(screen_buffer_output)

    with open(cbf_asm_file_path, 'w') as asm_file:
        print("Saving {}...".format(cbf_asm_file_path))
        color_buffer_output = "\n".join(cbf)
        asm_file.write(color_buffer_output)


def convert_image_to_asm_code(input_img, full_size):
    pixels = np.flipud(np.transpose(np.array(list(input_img.getdata())).reshape((25 if full_size else 13, 16))))
    asm_code_lines = ["\tbyte " + ", ".join(map(str, x[:13])) for x in pixels]
    return asm_code_lines


def save_image_to_asm_files(file_path, full_size):
    print("Processing {}".format(file_path))
    curr_img = Image.open(file_path)
    head, tail = os.path.split(file_path)
    src_file_name, ext = os.path.splitext(tail)
    asm_file_path = os.path.join(head, "..", src_file_name) + DST_EXTENSION
    with open(asm_file_path, 'w') as asm_file:
        asm_file.write("\n".join(convert_image_to_asm_code(curr_img, full_size)))


def save_images_to_asm_files(textures_dir, extension, full_size):
    files_in_path = [x for x in os.listdir(textures_dir) if x.endswith(extension)]
    for src_file in files_in_path:
        full_src_file_path = os.path.join(textures_dir, src_file)
        save_image_to_asm_files(full_src_file_path, full_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--hi-res',
                        required=False,
                        dest='hires',
                        action='store_true')
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

    if args.hires:
        if args.single:
            save_image_to_asm_files_80x50(args.path, args.full_size)
        else:
            print("not available now")
    else:
        if args.single:
            save_image_to_asm_files(args.path, args.full_size)
        else:
            save_images_to_asm_files(args.path, "tga", args.full_size)


