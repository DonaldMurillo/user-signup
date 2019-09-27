from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

class SignupInfo():

    def __init__(self, my_info):

        self.user_name = my_info["username"]#[1]
        self.password = my_info["password"]#[1]
        self.veri_password = my_info["veripassword"]#[1]
        self.email = my_info["email"]#[1]
        error_dict = {}
        self.is_verified = False
        if self.password == self.veri_password:
            self.is_verified = True

        for data in my_info:
            
            if len(my_info[data]) == 0 :
                error_dict.update({str(data)+ "_is_empty" : True })
                print({str(data)+ "_is_empty" : True})

            if (len(my_info[data]) < 3 or len(my_info[data]) > 20) and len(my_info[data]) > 0:
                error_dict.update({str(data)+ "_bad_length" : True})
            
        if my_info["email"].count("@") != 1 and my_info["email"].count(".") != 1 and my_info["email"].count(" ") != 1:
            error_dict.update({"email_invalid_char" : True})
            print({"email_invalid_char" : True})

        self.errors= error_dict.copy()
        self.has_data = True
        self.redirect = False
        if len(self.errors) == 0:
            self.redirect = True

    def print_all(self):
        print("""username: {0}
        password: {1}
        verify password: {2}
        email: {3}
        """.format(self.user_name,self.password, self.veri_password, self.email))


@app.route("/", methods=["POST", "GET"])
def index():

    new_signup = ""

    if request.method == "POST":

        new_signup = SignupInfo(request.form)
        
        new_signup.print_all()

        if new_signup.redirect:
            return render_template("/confirmation.html", name= new_signup.user_name)

        return render_template("signup.html", tittle = "Signup", new_signup = new_signup)

    if request.method == "GET":
        new_signup = None
        return render_template("signup.html", tittle = "Signup", is_verified = True)

# @app.route("/error", methods=["POST"])
# def error():

#     return render_template()
    

app.run()