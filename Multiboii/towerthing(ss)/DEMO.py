# malikvivaan@gmail.com yeetboii
# samantshourya@gmail.com ILOVEU3000
import multiplayer

user=None
run=True
while run:
    opt=input('CREATEACC/LOGINACC/RESETPASS [C/L/R]')
    if opt.lower()=='c':
        email=input('Email: ')
        PASS1=input('Password: ')
        PASS2=input('Confirm Password: ')
        username=input('Username: ')
        AUTH=multiplayer.auth()
        status=AUTH.create_account(username, email, PASS1, PASS2)
        print(status)
        run=False
    elif opt.lower()=='l':
        email=input('Email: ')
        PASS=input('Password: ')
        AUTH=multiplayer.auth()
        status, user=AUTH.sign_in(email, PASS)
        print(status)
        run=False
    elif opt.lower()=='r':
        PASS1=input('New Password: ')
        PASS2=input('Confirm New Password: ')
        print(AUTH.reset_pass(PASS1, PASS2))
        run=False
    else:
        pass
    if not run:
        rerun=input('Redo? [y/n]')
        if rerun.lower()=='y':
            run=True
