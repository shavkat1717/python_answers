#Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing:
def maximum(x, y, z):
    """Ushbu funksiya uchta son qabul qilib, ulardan eng kattasini qaytaradi"""
    max = x
    if y>=max:
        max=y
    if z>=max:
        max=z
    return max
print(maximum(-7, 10, 74))