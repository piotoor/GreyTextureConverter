from PIL import Image
import numpy as np
import os
import argparse


def convert_image_to_asm_code(input_img, half=True):
    pixels = np.transpose(np.array(list(input_img.getdata())).reshape((13 if half else 25, 16)))
    asm_code_lines = ["byte " + ", ".join(map(str, x[:13])) for x in pixels]
    return asm_code_lines


def save_image_to_asm_files(file_path, half=True):
    print("Processing {}".format(file_path))
    curr_img = Image.open(file_path)
    head, tail = os.path.splitext(file_path)
    asm_file_path = head + ".asm"
    with open(asm_file_path, 'w') as asm_file:
        asm_file.write("\n".join(convert_image_to_asm_code(curr_img)))


def save_images_to_asm_files(textures_dir, extension="tga", half=True):
    files_in_path = [x for x in os.listdir(textures_dir) if x.endswith(extension)]
    for src_file in files_in_path:
        full_src_file_path = os.path.join(textures_dir, src_file)
        save_image_to_asm_files(full_src_file_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--single-file',
                        required=False,
                        dest='single',
                        action='store_true')
    parser.add_argument('path',
                        type=str)
    args = parser.parse_args()
    print(args.path)
    if args.single:
        save_image_to_asm_files(args.path)
    else:
        save_images_to_asm_files(args.path)


