from fpdf import FPDF


class Shirt(FPDF):
    def header(self):
        self.ln(28)
        self.set_font("helvetica", "", 48)
        self.cell(0, 0, "CS50 Shirtificate", align="C")
        self.ln(28)


def main():
    # input
    name = input("Name: ")

    shirt = Shirt(orientation="portrait", format="A4")
    shirt.add_page()
    shirt.image("./shirtificate.png", w=shirt.epw)
    shirt.image("./iron-man.png", w=shirt.epw/4, x=shirt.epw/2-12, y=shirt.eph/2+10)

    shirt.set_font("helvetica", size=24)
    shirt.set_text_color(255, 255, 255)
    shirt.text(shirt.epw/3, shirt.eph/2, txt=f"{name} took CS50")
    shirt.output("shirtificate.pdf")


if __name__ == "__main__":
    main()