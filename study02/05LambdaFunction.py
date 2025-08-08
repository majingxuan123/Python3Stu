def testFunction1(compute):
    result = compute(1,2)
    print("result:" + str(result))
testFunction1(lambda a,b:a+b)
