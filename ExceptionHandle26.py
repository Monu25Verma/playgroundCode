def find_average(mark_list):
    try:
        total = 0
        for i in range(0, len(mark_list)):
            total += mark_list[i]
            mark_avg = total / len(mark_list)
            return mark_avg
    except NameError:
        print("the type error occuped in variable")


m_list = [1,2,3,4]
print("Average marks:", find_average(m_list))