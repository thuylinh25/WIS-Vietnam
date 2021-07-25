# Bài 1: Yêu cầu người dùng cung cấp một chuỗi và cho biết đó có phải một palindrome không (palindrome là một chuỗi có thể được viết xuôi hay viết ngược vẫn chỉ cho ra chính nó).

input_string = input("Mời nhập chuỗi: ")
if input_string == input_string[::-1]:
    print("Đây là chuỗi Palindrome ")
else:
    print("Đây không phải là chuỗi Palindrome")

# Bài 2: Viết chương trình hỏi người dùng cần tạo bao nhiêu số trong dãy Fibonacci và tạo chúng. Chuỗi Fibonacci là một dãy số trong đó số tiếp theo trong dãy là tổng của hai số trước đó. Ví dụ của một chuỗi Fibonacci như sau: 1, 1, 2, 3, 5, 8, 13,…

def create_fibo(n):
    if n <= 0:
        return False
    if n == 1:
        return 1
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs
n = int(input("Bạn cần tạo bao nhiêu số trong dãy Fibonacci: "))
print(create_fibo(n))

# Bài 3: Yêu cầu người dùng nhập một số và xác định xem đó có phải là số nguyên tố hay không.
num = int(input("Mời nhập số cần kiểm tra: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "không là số nguyên tố")
            break
    else:
        print(num, "là số nguyên tố")
else:
    print(num, "không là số nguyên tố")

# Bài 4: Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
# Ví dụ: đầu vào là: 0100,0011,1010,1001
# 	Đầu ra sẽ là: 1010

value = []
items=[x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    intp = int(p, 2)
    if intp%5 == 0:
        value.append(p)
print (','.join(value))

# Bài 5 : Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
def check_value(n):
    if n%2 == 0:
        print ("Đây là một số chẵn")
    else:
       print ("Đây là một số lẻ")
check_value(int(input("Mời bạn nhập số:")))

# Bài 6: Nhập một số, in ra giai thừa của số đó. Lưu ý: Không sử dụng for trong bài tập này.
def factorial_cal(x):
    if x == 0:
        return 1
    return x * factorial_cal(x - 1)
x = int(input("Mời bạn nhập số: "))
print('giai thừa của',x, 'là:',  factorial_cal(x))

# Bài 7: Tạo trò chơi “Cows and Bulls” với cách thức hoạt động như sau:
# 1.	Tạo ngẫu nhiên một con số có 4 chữ số. Yêu cầu người chơi đoán con số đó.
# 2.	Khi người chơi đoán đúng một chữ số nào đó ở đúng vị trí, họ sẽ có một “Cow”. Với mỗi chữ số sai, họ sẽ có một “Bull”.
# 3.	Mỗi khi người dùng đưa ra phỏng đoán, hãy cho họ biết họ có bao nhiêu “Cows” và “Bulls”. Khi người dùng đoán đúng số, trò chơi kết thúc. Theo dõi số lần đoán mà người dùng thực hiện trong suốt trò chơi và họ biết khi kết thúc.
# Ví dụ: Giả sử, máy tính tạo ra một con số là 1038. Một tương tác sẽ diễn ra như sau:
#  	Welcome to the Cows and Bulls Game!
#  	Enter a number:
#   	>>> 1234
#   	2 cows, 0 bulls
#   	>>> 1256
#   	1 cow, 1 bull
#   	...
import random
def game():
    print('Welcome to the Cows and Bulls Game!')
    numb = str(random.randint(1000,9999))
    playing = True
    cow = 0
    bull = 1
    while playing:
        player_guess = int(input("Enter your guess: "))
        if player_guess < 1000 or player_guess > 9999:
            print("Enter a 4 digits number only. Try again.")
            continue
        player_guess = str(player_guess)
        cow = sum([1 if numb[i] == player_guess[i] else 0 for i in range(4)])
        print('{} cows, {} bulls'.format(cow,bull))
        bull += 1
        if cow == 4:
            print("Your guess is right after",bull,"times guess")
            playing = False
game()

# Bài 8: Viết một chương trình để chuyển đổi số nguyên N sang hệ cơ số B (2 <= B <= 32) bất kỳ.
def convert_number(numb, base):
    if numb == 0:
        return 0
    digits = []
    while numb:
        digits.append((int(numb % base)))
        numb //= base
    digits = digits[::-1]
    ans = [str(digit) if digit <= 9 else chr(ord('A')+digit-10) for digit in digits ]
    return ''.join(ans)

n = int(input("Nhập số nguyên dương n = "))
print("Hệ cơ số 2 của số nguyên ", n, "là:", convert_number(n, 2))
print("Hệ cơ số 32 của số nguyên ", n, "là:", convert_number(n, 32))

