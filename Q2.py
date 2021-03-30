# Numeric Filter

if __name__ == '__main__':
    try:
        num = int(input('Please input a number:'))
        if num<0:
            print('The input number less than zero.')
        elif num>=0:
            count = 0
            for i in range(1,num+1):
                if i%3==0 and i%5==0:
                    count+=1
                elif i%3==0 or i%5==0:
                    pass
                else:
                    count+=1
            print('Result = {count}'.format(count=count))
    except:
        print('The input data format is not a number.')