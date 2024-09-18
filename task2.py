import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def battle(plants: list, zombies: list) -> bool:
    try:
        survival_zombies = 0
        survival_plants = 0

        count_zombies = len(zombies)
        count_plants = len(plants)

        for i in range(max(count_plants, count_zombies)):
            plant = plants[i] if i < count_plants else None
            zombie = zombies[i] if i < count_zombies else None

            if plant is not None and zombie is not None:
                if plant > zombie:
                    survival_plants += 1
                elif plant < zombie:
                    survival_zombies += 1

            elif plant is not None:
                survival_plants += 1

            elif zombie is not None:
                survival_zombies += 1

        logging.info(f'Кол-во выживших растений: {survival_plants};\n'
                     f'Кол-во выживших зомби: {survival_zombies};')

        if survival_plants > survival_zombies:
            return True
        elif survival_plants < survival_zombies:
            return False
        else:
            total_plant_attack = sum(plants)
            total_zombie_attack = sum(zombies)

            if total_plant_attack > total_zombie_attack:
                return True
            elif total_plant_attack < total_zombie_attack:
                return False
            else:
                return True
    except Exception as exc:
        logging.error(f'Произошла ошибка: {exc}')


assert battle(plants=[2, 4, 6, 8], zombies=[1, 3, 5, 7]) == True
assert battle(plants=[2, 4], zombies=[1, 3, 5, 7]) == False
assert battle(plants=[2, 4, 0, 8], zombies=[1, 3, 5, 7]) == True
assert battle(plants=[1, 2, 1, 1], zombies=[2, 1, 1, 1]) == True
