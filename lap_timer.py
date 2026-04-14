# lap_timer.py
# Libreria de funciones para registrar tiempos de vuelta en una carrera.
#
# Estructura del diccionario (timer):
#   - 'max':   numero maximo de vueltas permitidas (int)
#   - 'times': lista con los tiempos de cada vuelta (list)
#   - 'total': tiempo acumulado de todas las vueltas (float)


def init(max_laps):
    timer = {}
    timer["max"] = max_laps
    timer["times"] = []
    timer["total"] = 0.0
    return timer


def add_lap(timer, time):
    if len(timer["times"]) < timer["max"]:
        timer["times"].append(time)
        timer["total"] = timer["total"] + time
    return timer


def count(timer):
    return len(timer["times"])


def cumulative_time(timer):
    return timer["total"]


def format_laps(timer):
    return str(timer["times"])


def fastest_lap(timer):
    times = timer["times"]
    if len(times) == 0:
        return 0

    fastest = times[0]
    for t in times:
        if t < fastest:
            fastest = t
    return fastest


def fastest_multi_lap(timer, k):
    times = timer["times"]

    if len(times) < k:
        return 0

    best = 999999

    i = 0
    while i <= len(times) - k:
        suma = 0
        j = 0
        while j < k:
            suma = suma + times[i + j]
            j = j + 1

        if suma < best:
            best = suma

        i = i + 1

    return best


def longest_decreasing_streak(timer):
    times = timer["times"]

    if len(times) == 0:
        return 0

    max_streak = 1
    current = 1

    i = 1
    while i < len(times):
        if times[i] < times[i - 1]:
            current = current + 1
            if current > max_streak:
                max_streak = current
        else:
            current = 1

        i = i + 1

    return max_streak



def main():
    # crear un cronometro para el record mundial de 100m de Usain Bolt,
    # dividiendo la carrera en 10 segmentos (o "vueltas")
    timer = init(10)
    timer = add_lap(timer, 1.85)
    timer = add_lap(timer, 1.02)
    timer = add_lap(timer, 0.91)
    timer = add_lap(timer, 0.87)
    timer = add_lap(timer, 0.85)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.82)
    timer = add_lap(timer, 0.83)
    timer = add_lap(timer, 0.90)

    # imprimir estadisticas
    print("numero de vueltas =", count(timer))                    # 10
    print("tiempo acumulado =", cumulative_time(timer))           # 9.69
    print("vuelta mas rapida =", fastest_lap(timer))              # 0.82
    print("50m mas rapidos =", fastest_multi_lap(timer, 5))       # 4.14
    print("racha mas larga =", longest_decreasing_streak(timer))  # 6

    # imprimir tiempos
    # [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.9]
    print(format_laps(timer))


if __name__ == "__main__":
    main()
