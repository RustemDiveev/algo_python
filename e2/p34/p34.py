from os.path import splitext
from collections import Counter

from matplotlib import pyplot 


class FileLetterCounter:

    def __init__(self, path: str): 
        """
            path: Путь к текстовому файлу 
        """
        self.path = path 
        self.validate_input()
        self.counter = Counter()
        self.process_file()

    def validate_input(self):
        """
            Проверка типа данных path 
            Проверка существования файла 
        """
        if not isinstance(self.path, str):
            raise TypeError("Параметр path должен быть строкой")
        
        _, file_extension = splitext(self.path)
        if file_extension != ".txt":
            raise ValueError("Указанный файл должен иметь расширение txt")
        
    def process_file(self):
        """
            Обработка файла и подсчет букв
        """
        try:
            with open(self.path) as file:
                for line in file: self.process_line(line.upper())
        except FileNotFoundError:
            raise FileNotFoundError("Указанный файл не найден, проверьте путь к файлу")
        
    def process_line(self, line: str):
        """
            Обработка отдельной строчки файла и заполнение счетчика
        """
        for letter in line: 
            if letter.isalpha(): self.counter[letter] += 1

    def build_bar_chart(self):
        sorted_counter = sorted(self.counter.items())
        x, y = zip(*sorted_counter)
        pyplot.bar(x, y)
        for index, data in enumerate(y):
            pyplot.text(x=index, y=data, s=data, fontdict=dict(fontsize=20))
        pyplot.show()

# a = FileLetterCounter("e2/p34/example.txt")
# a.build_bar_chart()