import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def pif(array: list) -> bool:
    try:
        sorted_array = sorted(array)

        for num in range(len(sorted_array)-2):
            first_leg = sorted_array[num]
            second_leg = sorted_array[num+1]
            hypotenuse = sorted_array[num+2]

            if first_leg ** 2 + second_leg ** 2 == hypotenuse ** 2:
                logging.info(f'Треугольник найден: {first_leg}, {second_leg}, {hypotenuse} !')
                return True

        logging.info('Треугольник не найден!')
        return False

    except Exception as exc:
        logging.error(f'Произошла ошибка: {exc}')


assert pif([5, 3, 4]) == True
assert pif([6, 8, 10]) == True
assert pif([100, 3, 65]) == False


