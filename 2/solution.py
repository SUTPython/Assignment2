<<<<<<< HEAD
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
=======
# Customer list
list_moshtari = []  # [["First Name", "Last Name", "Phone Number", "Address", ["Previous Purchases"]]]

# Admin list
list_admin = []  # [["First Name", "Last Name", "Phone Number", "Address", Salary, "Position"]]

# Influencer list
list_influenser = []  # [["First Name", "Last Name", "Phone Number", "Address", [("Post", Price)], "Page Address"]]

def add_customer(customer_data):
    list_moshtari.append(customer_data)

def add_admin(admin_data):
    list_admin.append(admin_data)

def add_influencer(influencer_data):
    list_influenser.append(influencer_data)

def dismiss_admins():
    total_salary = sum(admin[4] for admin in list_admin)
    for admin in list_admin:
        print(f"Name: {admin[0]}, Last Name: {admin[1]}, Phone: {admin[2]}, Address: {admin[3]}, Salary: {admin[4]}, Position: {admin[5]}")
    print(f"Total Salary: {total_salary}")
    list_admin.clear()

def geometric_mean(posts, earnings):
    if posts > 0 and earnings > 0:
        return (posts * earnings) ** 0.5
    return float('inf')

def select_best_influencer():
    best_influencer = None
    min_geometric_mean = float('inf')
    for influencer in list_influenser:
        total_posts = len(influencer[4])
        total_earnings = sum(post[1] for post in influencer[4])
        gm = geometric_mean(total_posts, total_earnings)
        if gm < min_geometric_mean:
            min_geometric_mean = gm
            best_influencer = influencer
    if best_influencer:
        print(best_influencer[5])

def process_command(command):
    if "New customer" in command:
        customer_data = eval(command.split("New customer")[0].strip())
        add_customer(customer_data)
    elif "New admin" in command:
        admin_data = eval(command.split("New admin")[0].strip())
        add_admin(admin_data)
    elif "New Influencer" in command:
        influencer_data = eval(command.split("New Influencer")[0].strip())
        add_influencer(influencer_data)
    elif command == "Dismissal of admins":
        
            dismiss_admins()
        
            select_best_influencer()

while True:
    command = input()
    if command == "exit":
        break
    process_command(command)
>>>>>>> origin/main
