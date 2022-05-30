class Matrix:
    def __init__(self, month, year, day = None) -> None:
        self.__day = str(day)
        self.__month = str(month)
        self.__year = str(year)
            
    def get_line_matrix(self):
        matrix = list(self.__day) + list(self.__month) + list(self.__year)

        def sum():
            last_elem = list(matrix[-1])
            x = 0
            if not len(last_elem) == 1:
                for i in last_elem:
                    x += int(i)
                matrix.append(str(x))
            return x

        x9 = 0
        for i in matrix:
            x9 += int(i)
        matrix.append(str(x9))

        x10 = sum()

        x11 = int(matrix[8]) - int(matrix[0]) * int(matrix[0])
        if x11 < 1: x11 = 1 # test
        
        matrix.append(str(x11))

        x12 = sum()

        matrix.append(str(x9 + x11))
        matrix.append(str(x10 + x12))

        return matrix

    
    def get_matrix(self):
        matrix = []
        input_data = self.get_line_matrix()
        
        last_elems = [input_data[-2], input_data[-1]]

        index = 0
        pop_list = []
        for elem in last_elems:
            if len(elem) == 2 and int(elem) > 12:
                pop_list.append(index)
                new_elems = list(elem)
                last_elems += new_elems
                index += 1

        for pop in reversed(pop_list):
            last_elems.pop(pop)

        input_data.pop(-2)
        input_data.pop(-1)

        nulls = ''
        for num in input_data:
            if '0' in str(num) and not '10' in str(num):
                nulls += '0'

        add_nulls = ''
        for elem in last_elems:
            if '0' == elem:
                add_nulls += '0'
        if add_nulls:
            nulls = f'{nulls}({add_nulls})'

        for rows in range(0,4):
            add = []
            index = 0
            sum = 0
            sum_end = 0

            for i in range(1 + (rows * 3), 4 + (rows * 3)):
                last_num = ''
                for elem in last_elems:
                    new_elem = str(i)
                    if new_elem == elem:
                        sum_end += int(new_elem)
                        last_num += new_elem

                def add_elem(elem, is_add: bool = True):
                    in_list = False
                    for num in add:
                        if str(i) in num:
                            in_list = True
                            if is_add:
                                add[index] += str(i)
                            elif last_num:
                                add[index] += f'({last_num})'
                    if not in_list:
                        if not is_add and last_num:
                            add.append(f'({last_num})')
                        else:
                            add.append(elem)
                        
                for j in input_data:
                    if str(i) == j:
                        sum += i
                        add_elem(j)
                    elif int(j) > 12:
                        for x in list(j):
                            if str(i) == x:
                                sum += i
                                add_elem(x)
                add_elem("-", False)
                index += 1
            result = ''

            if sum > 12:
                sum_str = str(sum)
                sum = 0
                for x in sum_str:
                    sum += int(x)

            if not sum_end == 0:
                if sum_end > 12:
                    sum_str = str(sum_end)
                    sum_end = 0
                    for x in sum_str:
                        sum_end += int(x)
                result = f'{sum}({sum_end})'
            else:
                result = f'{sum}'
            add.append(result)
            matrix.append(add)
        
        matrix = [['-', nulls, '-', '-']] + matrix

        index = 0
        for rows in matrix:
            matrix[index] = tuple(rows)
            index += 1

        return matrix

    def get_num_matrix(self, num):
        line_matxs = self.__month_line_matx()

        matrix = []
        for line in line_matxs:
            count = 0
            for nums in line:
                if int(nums) > 12:
                    for j in list(nums):
                        if str(num) == str(j):
                            count += 1
                else:
                    if str(num) == nums:
                        count += 1
            matrix.append(count)
        
        index = 1
        data = []
        for num in matrix:
            data.append((index, num))
            index += 1

        return data

    def get_month_matrix(self):
        line_matxs = self.__month_line_matx()

        data = []
        for i in range(1, 13):
            row = []
            for line in line_matxs:
                count = 0
                for num in line:
                    if int(num) > 12:
                        for j in list(num):
                            if str(i) == str(j):
                                count += 1
                    else:
                        if str(i) == num:
                            count += 1
                row.append(count)
            data.append(row)
        
        index = 0
        for row in data:
            row = [f"[color=#ff0303]{index + 1}[/color]"] + row
            data[index] = tuple(row)
            index += 1

        return data

    def __month_line_matx(self):
        input_day = lambda x: list(x) if len(x) == 2 else ['0', x]
        line_matxs = []
        for i in range(1, 31):
            matrix = input_day(str(i)) + list(self.__month) + list(self.__year)
            def sum():
                last_elem = list(matrix[-1])
                x = 0
                if not len(last_elem) == 1:
                    for i in last_elem:
                        x += int(i)
                    matrix.append(str(x))
                return x

            x9 = 0
            for i in matrix:
                x9 += int(i)
            matrix.append(str(x9))

            x10 = sum()

            x11 = int(matrix[8]) - int(matrix[0]) * int(matrix[0])
            if x11 < 1: x11 = 1 # test

            matrix.append(str(x11))

            x12 = sum()

            matrix.append(str(x9 + x11))
            matrix.append(str(x10 + x12))
            line_matxs.append(matrix)

        return line_matxs