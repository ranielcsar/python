import time


def calculate_execution_time(function):
    def wrapper():
        inital_time = time.time()
        function()
        end_time = time.time()

        print(
            "[{function}] Tempo total de execução: {totalTime}".format(
                function=function.__name__, totalTime=str(end_time - inital_time)
            )
        )

    return wrapper


@calculate_execution_time
def main():
    for n in range(0, 10000000):
        pass


main()
