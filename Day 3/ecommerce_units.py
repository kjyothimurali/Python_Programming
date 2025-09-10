def apply_discount(price,discount_percent):
    return price*(discount_percent/100)

def add_gst(price, gst_percent=18):
    return price+(price*gst_percent/100)

def generate_invoice(cart, discount_percent, gst_percent=18):
    print("------ INVOICE ------")
    tot=0
    for i,j in cart.items():
        print(f"{i}         : ₹{j}")
        tot+=j
    print("---------------------")
    print("Subtotal: ₹",tot)
    t=tot-apply_discount(tot,discount_percent)
    print("After 10% discount: ₹",(t))
    print("After 18% GST: ₹",(t+add_gst(t,gst_percent)))
    print("---------------------")
    print("Thank you for shopping with us!")

