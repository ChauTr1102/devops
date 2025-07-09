import random
import datetime
import math


def generate_and_analyze_numbers():
    # Tạo danh sách 10 số ngẫu nhiên từ 1 đến 100
    numbers = [random.randint(1, 100) for _ in range(10)]

    # Tính toán thống kê
    total = sum(numbers)
    average = total / len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)

    # Lấy thời gian hiện tại
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # In kết quả
    print(f"Thời gian: {current_time}")
    print(f"Danh sách số ngẫu nhiên: {numbers}")
    print(f"Tổng: {total}")
    print(f"Trung bình: {average:.2f}")
    print(f"Số lớn nhất: {max_num}")
    print(f"Số nhỏ nhất: {min_num}")
    print(f"Độ lệch chuẩn: {std_dev:.2f}")


if __name__ == "__main__":
    generate_and_analyze_numbers()