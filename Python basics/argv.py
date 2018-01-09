def test_var_args(ga,pa,ca, *argv):
    print(*argv)
    print ("first normal arg:", ga)
    print(pa)
    print(ca)
    print(argv)
    for arg in argv:
        print ("arg through *argv :", arg)


test_var_args('yasoob','python','eggs','test')
# used for passing no. of arguments