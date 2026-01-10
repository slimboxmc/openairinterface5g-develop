import sys
import os

def check_unreachable(file_name):
    # 检查文件是否存在
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return False

    # 打开并读取文件内容
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            # 检查是否包含 '1 unreachable'
            if '1 unreachable' in content:
                #print(f"The file '{file_name}' contains '1 unreachable'.")
                return True
            else:
                #print(f"The file '{file_name}' does not contain '1 unreachable'.")
                return False
    except Exception as e:
        #print(f"Error: Could not read the file '{file_name}'. Reason: {e}")
        return False

if __name__ == "__main__":
    # 检查是否提供了文件名参数
    if len(sys.argv) != 2:
        print("Usage: python check_unreachable.py <file_name>")
        sys.exit(1)
    
    # 获取文件名
    input_file = sys.argv[1]

    # 检查文件内容
    result=check_unreachable(input_file)
    if result:print("1")
    else:print("0")
