def convert(number):
    sounds: list = ["Pling", "Plang", "Plong"]
    rain_melody = ""
    for index, num in enumerate([3, 5, 7]):
        if number % num == 0:
            rain_melody += sounds[index]
    return rain_melody if rain_melody else str(number)
