def find_average(mark_list):
    try:
        total = 0
        for i in range(0, len(mark_list)+1):
            total += mark_list[i]
            mark_avg = total / len(mark_list)
            return mark_avg
    except TypeError:
        print("Handle type error")
    except IndexError:
        print("Index error has been handled")

#m_list = ['1',2,3,4]
m_list = []
print("Average marks:", find_average(m_list))