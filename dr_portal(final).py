from graphics import *
import pandas as pd
import matplotlib.pyplot as plt

def new_data(new_entry):
    df = pd.read_csv("dr_portal3.csv")
    df_length = len(df)
    df.loc[df_length] = new_entry

    main(df)

def login():
    df = pd.read_csv("dr_portal3.csv")

    win = GraphWin("DR. Portal", 800, 600)
    win.setCoords(0.0, 0.0, 400, 300)
    cross1 = Rectangle(Point(20, 260), Point(50, 270))
    cross1.setFill("firebrick")
    cross1.setOutline("firebrick")
    cross1.draw(win)
    cross2 = Rectangle(Point(30, 250), Point(40, 280))
    cross2.setFill("firebrick")
    cross2.setOutline("firebrick")
    cross2.draw(win)
    name = Text(Point(120, 265), "Dr. Portal")
    name.setFace("courier")
    name.setSize(36)
    name.draw(win)

    welcome = Text(Point(200, 200), "Welcome to Dr. Portal!")
    welcome.setFace("courier")
    welcome.setSize(27)
    welcome.draw(win)

    user = Text(Point(100, 150), "Username:")
    user.setFace("courier")
    user.setSize(16)
    user.draw(win)
    password = Text(Point(100, 130), "Password:")
    password.setFace("courier")
    password.setSize(16)
    password.draw(win)
    user2 = Entry(Point(180, 150), 30)
    user2.draw(win)
    password2 = Entry(Point(180, 130), 30)
    password2.draw(win)

    login = Rectangle(Point(200, 110), Point(240, 95))
    login.setFill("tan")
    login.draw(win)
    login2 = Text(Point(220, 102.5), "Login")
    login2.setFace("courier")
    login2.draw(win)

    login3 = win.getMouse()
    if login3.getX() >= 200 and login3.getX() <= 240 and login3.getY() <= 110 and login3.getY() >= 95:
        win.close()
        main(df)

def insert_data():
    win = GraphWin("DR. Portal", 800, 600)
    win.setCoords(0.0, 0.0, 400, 300)
    cross1 = Rectangle(Point(20, 260), Point(50, 270))
    cross1.setFill("firebrick")
    cross1.setOutline("firebrick")
    cross1.draw(win)
    cross2 = Rectangle(Point(30, 250), Point(40, 280))
    cross2.setFill("firebrick")
    cross2.setOutline("firebrick")
    cross2.draw(win)
    name = Text(Point(120, 265), "Dr. Portal")
    name.setFace("courier")
    name.setSize(36)
    name.draw(win)

    welcome = Text(Point(200, 230), "Insert the Daily Information:")
    welcome.setFace("courier")
    welcome.setSize(20)
    welcome.draw(win)

    mes = Text(Point(200, 220), "Insert ALL values as numbers to continue.")
    mes.setFace("courier")
    mes.draw(win)

    patients = Text(Point(118, 200), "Number of Patients:")
    patients.setFace("courier")
    patients.draw(win)
    patients2 = Entry(Point(210, 200), 30)
    patients2.draw(win)
    doctors = Text(Point(120, 180), "Number of Doctors:")
    doctors.setFace("courier")
    doctors.draw(win)
    doctors2 = Entry(Point(210, 180), 30)
    doctors2.draw(win)
    n_patients = Text(Point(112, 160), "Number of New Patients:")
    n_patients.setFace("courier")
    n_patients.draw(win)
    n_patients2 = Entry(Point(210, 160), 30)
    n_patients2.draw(win)
    lab = Text(Point(106, 140), "Average Time Spent in Lab:")
    lab.setFace("courier")
    lab.draw(win)
    lab2 = Entry(Point(210, 140), 30)
    lab2.draw(win)
    emergency = Text(Point(95, 120), "Average Time Spent in Emergency:")
    emergency.setFace("courier")
    emergency.draw(win)
    emergency2 = Entry(Point(210, 120), 30)
    emergency2.draw(win)
    xray = Text(Point(100, 100), "Average Time Spent in X-Rays:")
    xray.setFace("courier")
    xray.draw(win)
    xray2 = Entry(Point(210, 100), 30)
    xray2.draw(win)
    surgery = Text(Point(100, 80), "Average Time Spent in Surgery:")
    surgery.setFace("courier")
    surgery.draw(win)
    surgery2 = Entry(Point(210, 80), 30)
    surgery2.draw(win)
    consult = Text(Point(100, 60), "Average Time Spent in Consult:")
    consult.setFace("courier")
    consult.draw(win)
    consult2 = Entry(Point(210, 60), 30)
    consult2.draw(win)

    done = Rectangle(Point(250, 30), Point(310, 45))
    done.setFill("tan")
    done.draw(win)
    done2 = Text(Point(280, 37.5), "Save")
    done2.setFace("courier")
    done2.draw(win)

    saved = win.getMouse()
    if saved.getX() >= 250 and saved.getX() <= 310 and saved.getY() <= 45 and saved.getY() >= 30:
        saving2 = Text(Point(280, 25), "Saved!")
        saving2.setFace("courier")
        saving2.draw(win)
        done2.setText("Done")

        patients3 = float(patients2.getText())
        doctors3 = float(doctors2.getText())
        n_patients3 = float(n_patients2.getText())
        lab3 = float(lab2.getText())
        emergency3 = float(emergency2.getText())
        xray3 = float(xray2.getText())
        surgery3 = float(surgery2.getText())
        consult3 = float(consult2.getText())

        n = 40
        if patients2 == True:
            n = n + 1

        new_entry = [n, patients3, doctors3, n_patients3, lab3, emergency3, xray3, surgery3, consult3]

        win.getMouse()
        win.close()

        win = GraphWin("DR. Portal", 800, 600)
        win.setCoords(0.0, 0.0, 400, 300)
        cross1 = Rectangle(Point(20, 260), Point(50, 270))
        cross1.setFill("firebrick")
        cross1.setOutline("firebrick")
        cross1.draw(win)
        cross2 = Rectangle(Point(30, 250), Point(40, 280))
        cross2.setFill("firebrick")
        cross2.setOutline("firebrick")
        cross2.draw(win)
        name = Text(Point(120, 265), "Dr. Portal")
        name.setFace("courier")
        name.setSize(36)
        name.draw(win)

        welcome = Text(Point(200, 220), "Graph of the Day:")
        welcome.setFace("courier")
        welcome.setSize(20)
        welcome.draw(win)
        values = [patients3, doctors3]
        colors = ["darksalmon", "navajowhite"]
        labels = ["Patients", "Doctors"]
        explode = (0, 0)

        next1 = Rectangle(Point(300, 30), Point(360, 45))
        next1.setFill("tan")
        next1.draw(win)
        t_next = Text(Point(330, 37.5), "Next")
        t_next.setFace("courier")
        t_next.draw(win)

        rec = Rectangle(Point(20, 30), Point(100, 45))
        rec.setFill("tan")
        rec.draw(win)
        rec2 = Text(Point(60, 37.5), "Recommendations")
        rec2.setFace("courier")
        rec2.draw(win)

        plt.pie(values, colors=colors, labels=labels,
                explode=explode, autopct="%1.1f%%",
                counterclock=False, shadow=False)
        plt.title("Patients vs. Doctors for the Day")
        plt.savefig("Graph.png", format="png", dpi= 70)
        plt.show()
        graph_d = Image(Point(200, 130), "Graph.png")
        graph_d.draw(win)

        next2 = win.getMouse()

        if next2.getX() >= 300 and next2.getX() <= 360 and next2.getY() <= 45 and next2.getY() >= 30:
            win.close()
            new_data(new_entry)
        elif next2.getX() >= 20 and next2.getX() <= 100 and next2.getY() <= 45 and next2.getY() >= 30:
            win.close()
            win = GraphWin("DR. Portal", 800, 600)
            win.setCoords(0.0, 0.0, 400, 300)
            cross1 = Rectangle(Point(20, 260), Point(50, 270))
            cross1.setFill("firebrick")
            cross1.setOutline("firebrick")
            cross1.draw(win)
            cross2 = Rectangle(Point(30, 250), Point(40, 280))
            cross2.setFill("firebrick")
            cross2.setOutline("firebrick")
            cross2.draw(win)
            name = Text(Point(120, 265), "Dr. Portal")
            name.setFace("courier")
            name.setSize(36)
            name.draw(win)

            welcome = Text(Point(200, 220), "Recommendations")
            welcome.setFace("courier")
            welcome.setSize(20)
            welcome.draw(win)

            next1 = Rectangle(Point(300, 30), Point(360, 45))
            next1.setFill("tan")
            next1.draw(win)
            t_next = Text(Point(330, 37.5), "Next")
            t_next.setFace("courier")
            t_next.draw(win)

            if patients3 - doctors3 >= 30:
                warning = Rectangle(Point(100, 150),Point(300,200))
                warning.setFill("indianred")
                warning.draw(win)
                warning2 = Text(Point(200,180), "WARNING!")
                warning2.setFace("courier")
                warning2.setSize(18)
                warning2.draw(win)
                warning3 = Text(Point(200,160), "There are a lot more patients than doctors.")
                warning3.setFace("courier")
                warning3.draw(win)

                textbox = Rectangle(Point(100, 140), Point(300, 50))
                textbox.setFill("oldlace")
                textbox.draw(win)
                text1 = Text(Point(200,125), "There are currently 30 or more patients than doctors.")
                text1.setSize(12)
                text1.setFace("courier")
                text1.draw(win)
                text2 = Text(Point(200,110), "Dr. Portal suggests the following:")
                text2.setSize(12)
                text2.setFace("courier")
                text2.draw(win)
                text3 = Text(Point(200,80), "Hire more doctors to make the hospital more efficient.")
                text3.setSize(12)
                text3.setFace("courier")
                text3.draw(win)
            elif patients3 - doctors3 <= 0:
                warning = Rectangle(Point(100, 150),Point(300,200))
                warning.setFill("khaki")
                warning.draw(win)
                warning2 = Text(Point(200,180), "WATCH OUT!")
                warning2.setFace("courier")
                warning2.setSize(18)
                warning2.draw(win)
                warning3 = Text(Point(200,160), "There are a more doctors than patients.")
                warning3.setFace("courier")
                warning3.draw(win)

                textbox = Rectangle(Point(100, 140), Point(300, 50))
                textbox.setFill("oldlace")
                textbox.draw(win)
                text1 = Text(Point(200,125), "There are currently more doctors than patients.")
                text1.setSize(12)
                text1.setFace("courier")
                text1.draw(win)
                text2 = Text(Point(200,110), "Dr. Portal suggests the following:")
                text2.setSize(12)
                text2.setFace("courier")
                text2.draw(win)
                text3 = Text(Point(200,80), "Decrease the amount of staff to increase efficiency.")
                text3.setSize(12)
                text3.setFace("courier")
                text3.draw(win)
            else:
                warning = Rectangle(Point(100, 150), Point(300, 200))
                warning.setFill("darkseagreen")
                warning.draw(win)
                warning2 = Text(Point(200, 180), "CONGRATULATIONS")
                warning2.setFace("courier")
                warning2.setSize(18)
                warning2.draw(win)
                warning3 = Text(Point(200, 160), "There is an efficient amount of patients per doctor.")
                warning3.setFace("courier")
                warning3.draw(win)

                textbox = Rectangle(Point(100, 140), Point(300, 50))
                textbox.setFill("oldlace")
                textbox.draw(win)
                text1 = Text(Point(200, 125), "There is an efficient ratio of patients to doctors.")
                text1.setSize(12)
                text1.setFace("courier")
                text1.draw(win)
                text2 = Text(Point(200, 110), "Dr. Portal suggests the following:")
                text2.setSize(12)
                text2.setFace("courier")
                text2.draw(win)
                text3 = Text(Point(200, 80), "Continue with current numbers to maintain efficiency.")
                text3.setSize(12)
                text3.setFace("courier")
                text3.draw(win)

            next2 = win.getMouse()

            if next2.getX() >= 300 and next2.getX() <= 360 and next2.getY() <= 45 and next2.getY() >= 30:
                win.close()
                new_data(new_entry)


def graph1(df):
    win = GraphWin("DR. Portal", 800, 600)
    win.setCoords(0.0, 0.0, 400, 300)
    cross1 = Rectangle(Point(20, 260), Point(50, 270))
    cross1.setFill("firebrick")
    cross1.setOutline("firebrick")
    cross1.draw(win)
    cross2 = Rectangle(Point(30, 250), Point(40, 280))
    cross2.setFill("firebrick")
    cross2.setOutline("firebrick")
    cross2.draw(win)
    name = Text(Point(120, 265), "Dr. Portal")
    name.setFace("courier")
    name.setSize(36)
    name.draw(win)

    welcome = Text(Point(200, 220), "New Patients Per Day")
    welcome.setFace("courier")
    welcome.setSize(20)
    welcome.draw(win)

    days = df['Day'].tolist()
    new_patients = df['New_Patients'].tolist()
    plt.plot(days, new_patients)
    plt.xlabel("Days")
    plt.ylabel("New Patients")
    plt.savefig("Line1.png", format="png", dpi= 70)
    plt.show()
    graph1_d = Image(Point(200,130),"Line1.png" )
    graph1_d.draw(win)

    next1 = Rectangle(Point(300, 30), Point(360, 45))
    next1.setFill("tan")
    next1.draw(win)
    t_next = Text(Point(330, 37.5), "Next")
    t_next.setFace("courier")
    t_next.draw(win)


    next2 = win.getMouse()

    if next2.getX() >= 300 and next2.getX() <= 360 and next2.getY() <= 45 and next2.getY() >= 30:
        win.close()
        graph2(df)

def graph2(df):
    win = GraphWin("DR. Portal", 800, 600)
    win.setCoords(0.0, 0.0, 400, 300)
    cross1 = Rectangle(Point(20, 260), Point(50, 270))
    cross1.setFill("firebrick")
    cross1.setOutline("firebrick")
    cross1.draw(win)
    cross2 = Rectangle(Point(30, 250), Point(40, 280))
    cross2.setFill("firebrick")
    cross2.setOutline("firebrick")
    cross2.draw(win)
    name = Text(Point(120, 265), "Dr. Portal")
    name.setFace("courier")
    name.setSize(36)
    name.draw(win)

    welcome = Text(Point(200, 220), "Average Time (Hospital Sections)")
    welcome.setFace("courier")
    welcome.setSize(20)
    welcome.draw(win)
    next1 = Rectangle(Point(300, 30), Point(360, 45))
    next1.setFill("tan")
    next1.draw(win)
    t_next = Text(Point(330, 37.5), "Menu")
    t_next.setFace("courier")
    t_next.draw(win)

    days = df['Day'].tolist()
    time_lab = df['Time_Lab'].tolist()
    time_emergency = df['Time_Emergency'].tolist()
    time_xray = df['Time_XRay'].tolist()
    time_surgery = df['Time_Surgery'].tolist()
    time_consult = df['Time_Consult'].tolist()
    plt.plot(days, time_lab)
    plt.plot(days, time_emergency)
    plt.plot(days, time_xray)
    plt.plot(days, time_surgery)
    plt.plot(days, time_consult)
    plt.xlabel("Days")
    plt.ylabel("Average Time")
    plt.legend(["Lab", "Emergency","X-Ray", "Surgery", "Consult"], loc=2)
    plt.savefig("Line2.png", dpi= 70)
    plt.show()
    graph2_d = Image(Point(200, 130), "Line2.png")
    graph2_d.draw(win)

    next2 = win.getMouse()

    if next2.getX() >= 300 and next2.getX() <= 360 and next2.getY() <= 45 and next2.getY() >= 30:
        win.close()
        main(df)

def main(df):
    # Logo
    win = GraphWin("DR. Portal", 800, 600)
    win.setCoords(0.0, 0.0, 400, 300)
    cross1 = Rectangle(Point(20, 260), Point(50, 270))
    cross1.setFill("firebrick")
    cross1.setOutline("firebrick")
    cross1.draw(win)
    cross2 = Rectangle(Point(30, 250), Point(40, 280))
    cross2.setFill("firebrick")
    cross2.setOutline("firebrick")
    cross2.draw(win)
    name = Text(Point(120, 265), "Dr. Portal")
    name.setFace("courier")
    name.setSize(36)
    name.draw(win)

    welcome = Text(Point(200, 220), "Welcome to the Mayo Clinics Management Website!")
    welcome.setFace("courier")
    welcome.setSize(20)
    welcome.draw(win)

    # Choose one of the options available.
    new_data = Rectangle(Point(50, 50), Point(175, 200))
    new_data.setFill("wheat")
    new_data.draw(win)
    consult_data = Rectangle(Point(225, 50), Point(350, 200))
    consult_data.setFill("wheat")
    consult_data.draw(win)
    daily = Text(Point(112, 125), "Insert Daily Log Here")
    daily.setFace("courier")
    daily.setSize(16)
    daily.draw(win)
    consult = Text(Point(287, 125), "See Hospital Management")
    consult.setFace("courier")
    consult.setSize(16)
    consult.draw(win)

    # quit
    next1 = Rectangle(Point(20, 25), Point(80, 40))
    next1.setFill("tan")
    next1.draw(win)
    t_next = Text(Point(50, 32.5), "Quit")
    t_next.setFace("courier")
    t_next.draw(win)

    click1 = win.getMouse()

    if click1.getX() >= 50 and click1.getX() <= 175 and click1.getY() <= 200 and click1.getY() >= 50:
        win.close()
        insert_data()
    elif click1.getX() >= 225 and click1.getX() <= 350 and click1.getY() <= 200 and click1.getY() >= 50:
        win.close()
        graph1(df)
    elif click1.getX() >= 20 and click1.getX() <= 80 and click1.getY() <= 40 and click1.getY() >= 25:
        win.close()


login()