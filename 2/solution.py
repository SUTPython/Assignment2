def list_maker(a):
    last_bracket = a.rfind(']')
    return eval(a[:last_bracket+1])
admins = []
influencers = {}
while True:
    a = input()
    if not a:
        continue
    elif 'exit' in a:
        break
    elif 'New customer' in a:
        continue
    elif 'New admin' in a:
        admins.append(list_maker(a))
    elif 'New Influencer' in a:
        list_of_influencer = list_maker(a)
        Sum_influence_money = 0
        for i in range(len(list_of_influencer[4])):
            Sum_influence_money += list_of_influencer[4][i][1]

        influencers[(len(list_of_influencer[4])*Sum_influence_money)**(1/2)] = list_of_influencer[-1]
    elif a == 'Dismissal of admins':
        if admins:
            Sum = 0
            for i in range(len(admins)):
                Sum += int(admins[i][4])
                print(f'Name: {admins[i][0]}, Last Name: {admins[i][1]}, Phone: {admins[i][2]}, Address: {admins[i][3]}, Salary: {admins[i][4]}, Position: {admins[i][5]}')
        if len(admins) == 0:
            print('Total Salary: 0')
        else:
            print(f'Total Salary: {Sum}')
        if influencers:
            if min(influencers) == 0:
                min_influence = min(k for k in influencers if k != 0)
                print(influencers[min_influence])
            else:
                min_influence = min(influencers)
                print(influencers[min_influence])
        admins.clear()
