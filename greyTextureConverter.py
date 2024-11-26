#!/usr/bin/env python3.12

from PIL import Image
import numpy as np
import os
import argparse

DST_EXTENSION = ".asm"


def convert_image_to_fli_64x26():
    curr_img = Image.open("WallJam01b_32x26.tga")
    cols = 64
    rows = 26
    pixels = np.array(list(curr_img.getdata())).reshape((rows, cols))
    print("pixels raw = {}".format(pixels))

    sr0_pixels = []
    sr1_pixels = []

    sr0_pixels_2 = []
    sr1_pixels_2 = []

    for c in range(0, len(pixels[0]), 2):
        if c < 32:
            for r in range(0,len(pixels), 2):
                sr0_pixels.append((pixels[r][c] << 4) | pixels[r][c + 1])
                sr1_pixels.append((pixels[r + 1][c] << 4) | pixels[r + 1][c + 1])
        else:
            for r in range(0,len(pixels), 2):
                sr0_pixels_2.append((pixels[r][c] << 4) | pixels[r][c + 1])
                sr1_pixels_2.append((pixels[r + 1][c] << 4) | pixels[r + 1][c + 1])

    print("tex part 1")
    print(sr0_pixels)
    print()
    print(sr1_pixels)
    print("tex part 2")
    print(sr0_pixels_2)
    print()
    print(sr1_pixels_2)

def convert_image_to_fli_32x26():
    curr_img = Image.open("WallJam01b_32x26.tga")
    cols = 32
    rows = 26
    pixels = np.array(list(curr_img.getdata())).reshape((rows, cols))
    print("pixels raw = {}".format(pixels))

    sr0_pixels = []
    sr1_pixels = []

    for c in range(0, len(pixels[0]), 2):
        for r in range(0,len(pixels), 2):
            sr0_pixels.append((pixels[r][c] << 4) | pixels[r][c + 1])
            sr1_pixels.append((pixels[r + 1][c] << 4) | pixels[r + 1][c + 1])


    print(sr0_pixels)
    print()
    print(sr1_pixels)


def convert_image_to_asm_code_fli_80x100(input_img):
    cols = 32
    rows = 52
    pixels = np.array(list(input_img.getdata())).reshape((rows, cols))
    print("pixels raw = {}".format(pixels))
    cols_0_7 = []
    cols_8_15 = []
    cols_16_23 = []
    cols_24_31 = []

    for c in range(0, cols, 2):
        for r in range(0, rows):
            if c < 8:
                cols_0_7.append((pixels[r][c] << 4) | pixels[r][c + 1])
            elif c < 16:
                cols_8_15.append((pixels[r][c] << 4) | pixels[r][c + 1])
            elif c < 24:
                cols_16_23.append((pixels[r][c] << 4) | pixels[r][c + 1])
            else:
                cols_24_31.append((pixels[r][c] << 4) | pixels[r][c + 1])

    cols_0_7_asm = ".byte\t" + ",".join(map(str, cols_0_7[0:52])) + "\n.byte\t" + ",".join(map(str, cols_0_7[52:104])) + "\n.byte\t" + ",".join(map(str, cols_0_7[104:156])) + "\n.byte\t" + ",".join(map(str, cols_0_7[156:208]))
    cols_8_15_asm = ".byte\t" + ",".join(map(str, cols_8_15[0:52])) + "\n.byte\t" + ",".join(map(str, cols_8_15[52:104])) + "\n.byte\t" + ",".join(map(str, cols_8_15[104:156])) + "\n.byte\t" + ",".join(map(str, cols_8_15[156:208]))
    cols_16_23_asm = ".byte\t" + ",".join(map(str, cols_16_23[0:52])) + "\n.byte\t" + ",".join(map(str, cols_16_23[52:104])) + "\n.byte\t" + ",".join(map(str, cols_16_23[104:156])) + "\n.byte\t" + ",".join(map(str, cols_16_23[156:208]))
    cols_24_31_asm = ".byte\t" + ",".join(map(str, cols_24_31[0:52])) + "\n.byte\t" + ",".join(map(str, cols_24_31[52:104])) + "\n.byte\t" + ",".join(map(str, cols_24_31[104:156])) + "\n.byte\t" + ",".join(map(str, cols_24_31[156:208]))

    print(cols_0_7_asm)
    print()
    print(cols_8_15_asm)
    print()
    print(cols_16_23_asm)
    print()
    print(cols_24_31_asm)
    print()

    return cols_0_7_asm, cols_8_15_asm, cols_16_23_asm, cols_24_31_asm


def save_image_to_asm_files_fli_80x100(file_path):
    print("Processing {}".format(file_path))
    curr_img = Image.open(file_path)
    head, tail = os.path.split(file_path)
    src_file_name, ext = os.path.splitext(tail)

    a, b, c, d = convert_image_to_asm_code_fli_80x100(curr_img)
    a_file_path = os.path.join(head, "..", src_file_name + "_a") + DST_EXTENSION
    with open(a_file_path, 'w') as asm_file:
        print("Saving {}...".format(a_file_path))
        screen_buffer_output = "".join(a)
        asm_file.write(screen_buffer_output)

    b_file_path = os.path.join(head, "..", src_file_name + "_b") + DST_EXTENSION
    with open(b_file_path, 'w') as asm_file:
        print("Saving {}...".format(b_file_path))
        screen_buffer_output = "".join(b)
        asm_file.write(screen_buffer_output)

    c_file_path = os.path.join(head, "..", src_file_name + "_c") + DST_EXTENSION
    with open(c_file_path, 'w') as asm_file:
        print("Saving {}...".format(c_file_path))
        screen_buffer_output = "".join(c)
        asm_file.write(screen_buffer_output)

    d_file_path = os.path.join(head, "..", src_file_name + "_d") + DST_EXTENSION
    with open(d_file_path, 'w') as asm_file:
        print("Saving {}...".format(d_file_path))
        screen_buffer_output = "".join(d)
        asm_file.write(screen_buffer_output)


def convert_image_to_asm_code_80x50(input_img, full_size, key_door_columns):
    cols = 38 if key_door_columns else 32
    pixels = np.array(list(input_img.getdata())).reshape((50 if full_size else 26, cols))[:26]
    print("pixels raw = {}".format(pixels))
    screen_buffer_pixels = []
    color_buffer_pixels = []

    for r in range(0,len(pixels), 2):
        for c in range(0, len(pixels[r]), 2):
            screen_buffer_pixels.append((pixels[r + 1][c] << 4) | pixels[r + 1][c + 1])
            color_buffer_pixels.append(pixels[r][c + 1])

    print("separated: \n{}\n\n{}".format(np.array(screen_buffer_pixels).reshape(13, cols // 2), np.array(color_buffer_pixels).reshape(13, cols // 2)))

    asm_code_screen_buffer = ["\t.byte " + ", ".join(map(str, x)) for x in np.flipud(np.transpose(np.array(screen_buffer_pixels).reshape(13, cols // 2)))]
    asm_code_color_buffer = ["\t.byte " + ", ".join(map(str, x)) for x in np.flipud(np.transpose(np.array(color_buffer_pixels).reshape(13, cols // 2)))]
    print(asm_code_screen_buffer)
    print("\n")
    print(asm_code_color_buffer)

    return asm_code_screen_buffer[::-1], asm_code_color_buffer[::-1]


def save_images_to_asm_files_80x50(textures_dir, extension, full_size, key_door_columns):
    files_in_path = [x for x in os.listdir(textures_dir) if x.endswith(extension)]
    for src_file in files_in_path:
        full_src_file_path = os.path.join(textures_dir, src_file)
        save_image_to_asm_files_80x50(full_src_file_path, full_size, key_door_columns)


def save_image_to_asm_files_80x50(file_path, full_size, key_door_columns):
    print("Processing {}".format(file_path))
    curr_img = Image.open(file_path)
    head, tail = os.path.split(file_path)
    src_file_name, ext = os.path.splitext(tail)

    sbf, cbf = convert_image_to_asm_code_80x50(curr_img, full_size, key_door_columns)
    sbf_asm_file_path = os.path.join(head, "..", src_file_name) + DST_EXTENSION
    cbf_asm_file_path = os.path.join(head, "..", src_file_name + "_b") + DST_EXTENSION
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
    asm_code_lines = ["\t.byte " + ", ".join(map(str, x[:13])) for x in pixels]
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

def printsr(sr):
    ans = "\t.fill 48,0\n"
    ans += "\t.byte "
    for x in sr:
        ans += str(x) + ", "

    return ans[:-2]


palette = (0, 0, 0,
           255, 255, 255,
           136, 0, 0,
           170, 255, 238,
           204, 68, 204,
           0, 204, 85,
           0, 0, 170,
           238, 238, 119,
           221, 136, 85,
           102, 68, 0,
           255, 119, 119,
           51, 51, 51,
           119, 119, 119,
           170, 255, 102,
           0, 136, 255,
           187, 187, 187)

palette_4colors = (
    0, 204, 85,         # 00 d021
    119, 119, 119,      # 01 d022
    187, 187, 187,      # 10 d023
    0, 0, 0             # 11 color ram
)

def convert_image_to_flat_16x16(path, out_path):
    curr_img = Image.open(path)
    curr_img.convert('1')
    curr_img.show()
    cols = 16
    rows = 16
    pixels = np.array(list(curr_img.getdata())) #.reshape((rows, cols))
    print(pixels.reshape((rows, cols)))
    sr = []
    sr_left = []

    for p in pixels:
        if p == 0:
            sr.append(0x00)
            sr_left.append(0x00)
        else:
            sr.append(0x0f)
            sr_left.append(0xf0)
    with open("char_mode_" + out_path, 'w') as asm_file:
        asm_file.write(printsr(sr))
        asm_file.write("\n")
    with open("char_mode_left_" + out_path, 'w') as asm_file:
        asm_file.write(printsr(sr))
        asm_file.write("\n")

def convert_image_to_fli_32x52(path, out_path, char_mode=False):
    curr_img = Image.open(path)
    pal_img = Image.new("P", (1, 1))
    if char_mode:
        pal_img.putpalette(palette_4colors + (255, 255, 255) * 240)
    else:
        pal_img.putpalette(palette + (255, 255, 255) * 240)
    curr_img = curr_img.convert("RGB").quantize(palette=pal_img).resize((32, 52))
    curr_img.show()

    cols = 32
    rows = 52
    pixels = np.array(list(curr_img.getdata()))
    # for x in pixels:
    #     print(x)
    pixels = pixels.reshape((rows, cols))
    # print("pixels raw = {}".format(pixels))


    if not char_mode:
        sr0_pixels = []
        sr1_pixels = []
        sr2_pixels = []
        sr3_pixels = []

        for c in range(0, len(pixels[0]), 2):
            for r in range(0, len(pixels), 4):
                sr0_pixels.append((pixels[r][c] << 4) | pixels[r][c + 1])
                sr1_pixels.append((pixels[r + 1][c] << 4) | pixels[r + 1][c + 1])
                sr2_pixels.append((pixels[r + 2][c] << 4) | pixels[r + 2][c + 1])
                sr3_pixels.append((pixels[r + 3][c] << 4) | pixels[r + 3][c + 1])

        with open(out_path, 'w') as asm_file:
            asm_file.write(printsr(sr0_pixels))
            asm_file.write("\n")
            asm_file.write(printsr(sr1_pixels))
            asm_file.write("\n")
            asm_file.write(printsr(sr2_pixels))
            asm_file.write("\n")
            asm_file.write(printsr(sr3_pixels))
            asm_file.write("\n")
    else:
        sr0_pixels_l = []
        sr1_pixels_l = []
        sr2_pixels_l = []
        sr3_pixels_l = []
        sr0_pixels_r = []
        sr1_pixels_r = []
        sr2_pixels_r = []
        sr3_pixels_r = []

        for c in range(0, len(pixels[0]), 2):
            for r in range(0, len(pixels), 4):
                a = (pixels[r][c] << 2) | pixels[r][c + 1]
                sr0_pixels_r.append(a)
                sr0_pixels_l.append(a << 4)

                a = (pixels[r + 1][c] << 2) | pixels[r + 1][c + 1]
                sr1_pixels_r.append(a)
                sr1_pixels_l.append(a << 4)

                a = (pixels[r + 2][c] << 2) | pixels[r + 2][c + 1]
                sr2_pixels_r.append(a)
                sr2_pixels_l.append(a << 4)

                a = (pixels[r + 3][c] << 2) | pixels[r + 3][c + 1]
                sr3_pixels_r.append(a)
                sr3_pixels_l.append(a << 4)

        with open("char_mode_left_" + out_path, 'w') as asm_file:
            asm_file.write(printsr(sr0_pixels_l))
            asm_file.write("\n")
            asm_file.write(printsr(sr1_pixels_l))
            asm_file.write("\n")
            asm_file.write(printsr(sr2_pixels_l))
            asm_file.write("\n")
            asm_file.write(printsr(sr3_pixels_l))
            asm_file.write("\n")

        with open("char_mode_right_" + out_path, 'w') as asm_file:
            asm_file.write(printsr(sr0_pixels_r))
            asm_file.write("\n")
            asm_file.write(printsr(sr1_pixels_r))
            asm_file.write("\n")
            asm_file.write(printsr(sr2_pixels_r))
            asm_file.write("\n")
            asm_file.write(printsr(sr3_pixels_r))
            asm_file.write("\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str)
    parser.add_argument("output_path", type=str)
    args = parser.parse_args()
    # convert_image_to_fli_32x52(args.input_path, args.output_path, char_mode=True)
    convert_image_to_flat_16x16(args.input_path, args.output_path)

