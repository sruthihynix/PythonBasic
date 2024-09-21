x = "sruthi"
y='vinod'

def wife():
    print(x)
    global w
    w='vihu'
    print('my baby',w)
def hus():
    print(y)
    print(w)    # global
def kid():
    print('kuttumani',w)

print('family')

wife()
hus()
kid()

print('outside',w)
