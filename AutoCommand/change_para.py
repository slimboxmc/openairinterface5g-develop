

import yaml



import re

def read_conf(filename):
    """
    逐行讀取 .conf 文件，解析為可修改的數據結構，同時保留原始行。
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    for line in lines:
        # 保留注釋行
        if line.strip().startswith('#') or not line.strip():
            parsed_data.append({'type': 'comment', 'content': line})
        else:
            # 匹配 key = value; 格式的參數行
            match = re.match(r'(\s*)([a-zA-Z0-9_]+)\s*=\s*(.+?);', line)
            if match:
                parsed_data.append({
                    'type': 'parameter',
                    'indent': match.group(1),
                    'key': match.group(2),
                    'value': match.group(3).strip(),
                    'original': line
                })
            else:
                # 保留無法解析的行
                parsed_data.append({'type': 'unknown', 'content': line})

    return parsed_data


def modify_conf(data, key_to_modify, new_value):
    """
    修改指定的 key 的值，保留其他內容。
    """
    for entry in data:
        if entry['type'] == 'parameter' and entry['key'] == key_to_modify:
            entry['value'] = new_value
            # 更新原始行
            entry['original'] = f"{entry['indent']}{entry['key']} = {entry['value']};\n"
    return data


def save_conf(data, filename):
    """
    將修改後的數據結構寫回 .conf 文件。
    """
    with open(filename, 'w') as file:
        for entry in data:
            if entry['type'] in ['comment', 'unknown']:
                file.write(entry['content'])
            elif entry['type'] == 'parameter':
                file.write(entry['original'])

def cange_and_save_conf(filename,key_to_modify,new_value):

    # 讀取文件
    conf_data = read_conf(filename)

    # 修改指定的參數
    conf_data = modify_conf(conf_data, key_to_modify, new_value)
    #print(conf_data)

    # 保存回文件
    save_conf(conf_data, filename)

# 示例：讀取、修改、保存





def change_the_related_parameter(delay):
    ntn_ta=delay*2
    # 讀取 YAML 文件
    # 讀取 YAML 文件
    path='/home/tonic/CCW/openairinterface5g-develop/ci-scripts/yaml_files/5g_f1_rfsimulator_rach_less/docker-compose.yaml'
    #path='test.yaml'
    with open(path, 'r') as file:
        config = yaml.safe_load(file)

    # 修改參數
    content=f'--rfsim --rfsimulator.serveraddr 192.168.71.181 \
                                        --rfsimulator.prop_delay {delay}'
    config['services']['oai-du1']['environment']['USE_ADDITIONAL_OPTIONS'] = content

    content=f'--rfsim --rfsimulator.serveraddr 192.168.71.181  \
                                        --rfsimulator.prop_delay {delay}'
    config['services']['oai-du2']['environment']['USE_ADDITIONAL_OPTIONS'] = content

    content=f'--rfsim -r 106 --numerology 1 -C 3450720000 --ssb  \
                    516 --uicc0.imsi 208990100001100 --rfsimulator.serveraddr server --rfsimulator.prop_delay  \
                    {delay} --ntn-koffset {ntn_ta} --ntn-ta-common {ntn_ta}'
    config['services']['oai-nr-ue']['environment']['USE_ADDITIONAL_OPTIONS'] = content

    # 寫回 YAML 文件
    with open(path, 'w') as file:
        yaml.safe_dump(config, file,indent=4)


    du1 = '/home/tonic/CCW/openairinterface5g-develop/ci-scripts/conf_rach_less/gnb-du.sa.band78.106prb.rfsim.pci0.conf'
    du2 = '/home/tonic/CCW/openairinterface5g-develop/ci-scripts/conf_rach_less/gnb-du.sa.band78.106prb.rfsim.pci1.conf'
    cange_and_save_conf(du1,'cellSpecificKoffset_r17',ntn_ta)
    cange_and_save_conf(du2,'cellSpecificKoffset_r17',ntn_ta)


import sys

# 接收參數
delay = int(sys.argv[1])



change_the_related_parameter(delay)

with open("/home/tonic/CCW/openairinterface5g-develop/AutoCommand/example.txt", "w") as file:
    for i in range(2):
        file.write(f"{sys.argv[i+2]}\n")






