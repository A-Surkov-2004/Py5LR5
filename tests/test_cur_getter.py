import src.curgetter
import time


def test1():
    # given
    mc = src.curgetter.CurGetter()
    mc.delay = 0
    mc.tracking_currencies = ['R01035', 'R01335', 'R01700J']

    # when
    ans = mc.get_currencies()

    # then
    assert (list(ans[0].keys())) == ['GBP']
    assert (list(ans[1].keys())) == ['KZT']
    assert (list(ans[2].keys())) == ['TRY']


def test2():
    # given
    mc = src.curgetter.CurGetter()
    mc.delay = 0
    cur = 'Hello world'

    # when
    ans = mc.get_currency(cur)

    # then
    assert ans == [{'R9999': None}]


def test3():
    # given
    mc1 = src.curgetter.CurGetter()
    mc2 = src.curgetter.CurGetter()
    mc2.delay = 0
    mc1.delay = 1
    time.sleep(1)
    cur = 'R01035'

    # when
    ans1 = mc1.get_currency(cur)
    ans2 = mc2.get_currency(cur)

    # then
    print(ans2)
    assert (list(ans1[0].keys())) == ['GBP']
    assert type(ans2[0]) == str  # 'Please, wait n seconds'
    mc1.delay = 0


def test4():
    # given
    mc = src.curgetter.CurGetter()
    mc.delay = 0
    mc.tracking_currencies = ['R01035', 'R01335', 'R01700J']

    # when
    ans = mc.get_currencies()

    # then
    mc.visualize_currencies()

test1()
test2()
test3()
test4()
