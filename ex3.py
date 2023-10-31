def digital_root(n):
    def recursive_digital_root(number):
        if number < 10:
            return number
        else:
            digit_sum = 0
            while number > 0:
                digit_sum += number % 10
                number //= 10
            return recursive_digital_root(digit_sum)

    if n < 0:
        raise ValueError("O número deve ser não negativo")
    return recursive_digital_root(n)

