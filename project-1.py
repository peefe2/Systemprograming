# HEX 값을 이진수로 변환하고 출력하는 프로그램
#20214256 전인철

def hex_to_binary(hex_value):
    # HEX 값을 이진수로 변환
    return bin(int(hex_value, 16))[2:].zfill(24)  # 24비트로 맞추기

def extract_opcode(binary_value):
    # 이진 값에서 Opcode를 추출 (앞 6비트)
    return binary_value[:6]

def extract_flag_bit(binary_value):
    # 이진 값에서 Flag bit를 추출 (다음 6비트)
    return binary_value[6:12]

def extract_disp_addr(binary_value):
    # 이진 값에서 Disp/Addr을 추출 (다음 12비트)
    return binary_value[12:24]

def extract_target_address(binary_value):
    # 타겟 주소는 Disp/Addr의 뒤 12비트를 사용
    return "0x" + hex(int(binary_value[12:], 2))[2:].zfill(6)

def extract_register_A_value(target_address):
    # 레지스터 A 값 계산 (여기서는 단순히 예시로 target_address 사용)
    return hex(int(target_address, 16) + 0x3000)

# 메인 프로그램

hex_input = "032600"  # 예시로 주어진 HEX 값

# HEX를 이진수로 변환
binary_code = hex_to_binary(hex_input)

# 각 항목 추출
opcode = extract_opcode(binary_code)
flag_bit = extract_flag_bit(binary_code)
disp_addr = extract_disp_addr(binary_code)
target_address = extract_target_address(binary_code)
register_A_value = extract_register_A_value(target_address)

# 출력
print(f"Hex 입력: {hex_input}")
print(f"Binary code: {binary_code}")
print(f"Opcode: {opcode}")
print(f"Flag bit: {flag_bit}")
print(f"Disp/Addr: {disp_addr}")
print(f"Target Address: {target_address}")
print(f"Register A value: {register_A_value}")
