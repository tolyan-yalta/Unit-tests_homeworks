class СompareAverage:

    @staticmethod
    def get_average_list(list_):
        average = sum(list_) / len(list_)
        return average

    @staticmethod
    def comparison_average_lists(list1, list2):
        average1 = СompareAverage.get_average_list(list1)
        average2 = СompareAverage.get_average_list(list2)
        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average1 < average2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
