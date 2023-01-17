def BMR(s, w, a, h):
    if s == 'female':
        return 655.1 + (9.567 * w) + (1.85 * h) + (-4.68 * a)
    else:
        return 66.47 + (13.7 * w) + (5 * h) + (-6.76 * a)


def BMI(w, h):
    return w / (h / 100) ** 2


def export_to_txt(data):
    f = open("your_data.txt", "w")
    for i in data:
        line = i.cget("text")
        f.write(line + "\n")
    f.close()