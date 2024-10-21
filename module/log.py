"""로그 작성"""


import os


def write_log(folder_path, file_path, e):
    """로그 작성"""
    log_path = os.path.join(folder_path, 'log.txt')
    with open(log_path, 'a', encoding='UTF-8') as file:
        file.write(f"{file_path} : {e}")
