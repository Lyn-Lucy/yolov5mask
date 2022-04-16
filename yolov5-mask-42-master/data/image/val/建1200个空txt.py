# 文件个数
num = 400


def main():
    # txt文件的存放路径
    desktop_path = "./labels/"
    count = 1
    for i in range(num):
        # 命名格式
        full_path = desktop_path + "val_" + str(count) + '.txt'
        file = open(full_path, 'w')
        count+=1

main()