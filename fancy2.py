def fancy_divide(list_of_numbers,index):
        try:    
            denom=list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i]/=denom
        except IndexError:
            print('-1')
        else:
            print('1')
        finally:
            print('0')

fancy_divide([0,2,4],1)
fancy_divide([0,2,4],4)
fancy_divide([0,2,4],0)