print('hello, welcome to trivial!')

ans = input ('are u ready to play(yes/no): ')

score = 0
total_q = 5
if ans.lower() == 'yes':
    ans = input('1.what is the best programming language? ')
    if ans.lower() == 'python':
        score += 1
        print('correct')
    else:
        print('incorrect')

    ans = input('2.what is 2 + 8 + 9 - 1 ?  ')
    if ans.lower() == '10':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('3.what is the  chemical formula for Gold?  ')
    if ans == 'Au':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('4.how many layers does our skin have? ')
    if ans.lower() == '3 layers' or ans.lower() == '3':
        score += 1
        print('correct')
    else:
        print('incorrect')


    ans = input('5.Lowest layer of atmosphere? ')
    if ans.lower() == 'troposphere':
        score += 1
        print('correct')
    else:
        print('incorrect')
print('Thank you for playing, you got ',score, 'questions correct. ')
mark = (score/total_q) * 100

print('Mark: ', str(mark) + '%')
print('Goodbye')


        













        
        
