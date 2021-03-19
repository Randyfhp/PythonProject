import os


def get_file_name(file):
    return os.path.basename(file)


def get_file_size(file):
    return os.path.getsize(file)


def get_file_suffix(file, lower=True):
    if not file:
        return ''
    src_suffix = os.path.splitext(file)[-1]
    return src_suffix.lower() if lower else src_suffix


def get_file_content_type(file):
    suffix = get_file_suffix(file)
    content_type = ''
    if suffix == '.jpg':
        # jpg图片
        content_type = 'image/jpg'
    if suffix == '.png':
        # png图片
        content_type = 'image/png'
    if suffix == '.bmp':
        # bmp图片
        content_type = 'image/bmp'
    if suffix == '.amr':
        # amr音频
        content_type = 'voice/amr'
    if suffix == '.mp4':
        # mp4视频
        content_type = 'video/mp4'
    else:
        # 普通文件
        content_type = 'application/octet-stream'
    return content_type


if __name__ == '__main__':
    print("./hello_world.txt".split('/')[-1][0])
