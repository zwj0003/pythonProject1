import os
import time

ab_file = "/Users/sz/PycharmProjects/pythonProject1/testdir_file"


def red_file(base_filename, new_filename):
    with open(f"{base_filename}", mode="r", encoding="utf-8") as f1, \
            open(f"{new_filename}", mode="w", encoding="utf-8") as f2:
        for line in f1:
            line = line.strip()
            if line.startswith("wang"):
                line = "zhang" + line[1:]
            f2.write(line)
            f2.write("\n")
    time.sleep(3)
    os.remove(f"{base_filename}")
    time.sleep(3)
    os.rename(f"{new_filename}", f"{base_filename}")


red_file(ab_file+"/d1.txt", ab_file+"/fuben.txt")

