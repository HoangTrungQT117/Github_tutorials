def predict(x, w, b):
    return x*w + b

def gradient(z,y,x):
    dw = 2*x*(z-y)
    db = 2*(z-y)
    return(dw, db)
def update_weight(w, b, n, dw, db):
    w_new = w - n*dw
    b_new = b - n*db
  #c the code has changed here..