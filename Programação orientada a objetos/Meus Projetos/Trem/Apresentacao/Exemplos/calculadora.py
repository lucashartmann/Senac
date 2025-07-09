from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Input

# python calculadora.py

class CalculadoraApp(App):
    CSS = """
        #display {
            background: #29508a;
            color: white;
            height: 3;
            content-align: right middle;
            border: none;
            margin: 1 1 1 1;
            padding: 0 2;
        }

        Button {
            background: #222;
            color: white;
            border: none;
            margin: 0 1 1 0;
            width: 100%;
            height: 3;
        }

        Button#add, Button#sub, Button#mul, Button#div, Button#eq {
            background: orange;
            color: black;
        }

        Button#clear, Button#negate, Button#percent {
            background: #29508a;
            color: white;
        }

        Vertical {
            width: 100%;
            height: 100%;
            margin: 1 1 1 1;
            align: center middle;
        }

        Horizontal {
            height: 3;
            min-width: 100%;
            content-align: center middle;
        }
        
        Horizontal > Button {
            width: 1fr;
        }
        
        Button#n0 {
            width: 2fr;
        }
    """

    def compose(self) -> ComposeResult:
        yield Vertical(
            Input(id="display", placeholder="0"),
            Horizontal(
                Button("C", id="clear"),
                Button("+/-", id="negate"),
                Button("%", id="percent"),
                Button("+", id="add"),
            ),
            Horizontal(
                Button("7", id="n7"), Button("8", id="n8"), Button("9", id="n9"), Button("-", id="sub"),
            ),
            Horizontal(
                Button("4", id="n4"), Button("5", id="n5"), Button("6", id="n6"), Button("*", id="mul"),
            ),
            Horizontal(
                Button("1", id="n1"), Button("2", id="n2"), Button("3", id="n3"), Button("/", id="div"),
            ),
            Horizontal(
                Button("0", id="n0"),
                Button(".", id="dot"),
                Button("=", id="eq"),
            )
        )

    def on_mount(self):
        self.reset()

    def reset(self):
        self.display_input = self.query_one("#display", Input)
        self.display_input.value = ""
        self.operand = None
        self.operator = None
        self.waiting_new = False

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn = str(event.button.label)
        if btn in "0123456789":
            if self.waiting_new:
                self.display_input.value = ""
                self.waiting_new = False
            self.display_input.value += btn
        elif btn == ".":
            if "." not in self.display_input.value:
                if self.display_input.value == "" or self.waiting_new:
                    self.display_input.value = "0."
                    self.waiting_new = False
                else:
                    self.display_input.value += "."
        elif btn in ["+", "-", "*", "/"]:
            if self.display_input.value:
                self.operand = float(self.display_input.value)
                self.operator = btn
                self.waiting_new = True
        elif btn == "=":
            if self.operator and self.display_input.value:
                try:
                    n2 = float(self.display_input.value)
                    if self.operator == "+":
                        res = self.operand + n2
                    elif self.operator == "-":
                        res = self.operand - n2
                    elif self.operator == "*":
                        res = self.operand * n2
                    elif self.operator == "/":
                        res = self.operand / n2 if n2 != 0 else "Erro"
                    self.display_input.value = str(res)
                except Exception:
                    self.display_input.value = "Erro"
                self.operator = None
                self.waiting_new = True
        elif btn == "C":
            self.reset()
        elif btn == "+/-":
            if self.display_input.value and self.display_input.value != "0":
                if self.display_input.value.startswith("-"):
                    self.display_input.value = self.display_input.value[1:]
                else:
                    self.display_input.value = "-" + self.display_input.value
        elif btn == "%":
            if self.display_input.value:
                try:
                    self.display_input.value = str(float(self.display_input.value) / 100)
                except Exception:
                    self.display_input.value = "Erro"

if __name__ == "__main__":
    CalculadoraApp().run()