from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.icon="calculator-icon.png"
        self.operators=["/","*","+","-"]
        self.last_was_operator=None
        self.last_button=None

        main_layout=BoxLayout(orientation="vertical")
        self.solution=TextInput(background_color="black", foreground_color="lime",font_size=55, multiline=False,
                                halign="right", readonly=True)

        main_layout.add_widget(self.solution)

        buttons=[
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","+"],
            [".","0","C","-"]
        ]

        backspace_button=Button(text="Backspace", font_size=30, background_color="grey",
            pos_hint={"center_x":0.5, "center_y":0.5})
        
        backspace_button.bind(on_press=self.on_clearc)
        main_layout.add_widget(backspace_button)

        for row in buttons:
            h_layout=BoxLayout()
            for label in row:
                button=Button(
                    text=label, font_size=40, background_color="grey",
                    pos_hint={"center_x":0.5, "center_y":0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        

        equal_button=Button(text="=", font_size=30, background_color="grey",
            pos_hint={"center_x":0.5, "center_y":0.5})
        
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout
    
    def on_clearc(self, instance):
        currnet=self.solution.text
        new_text=currnet[:-1]
        self.solution.text=new_text
        self.last_button=new_text[-1:]
        self.last_was_operator=new_text[-1:] in self.operators

    
    def on_button_press(self, instance):
        current=self.solution.text
        button_text=instance.text

        if button_text=='C':
            self.solution.text=""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current=="" and button_text in self.operators:
                return
            else:
                new_text=current+button_text
                self.solution.text=new_text
        self.last_button=button_text
        self.last_was_operator=self.last_button in self.operators

    def on_solution(self, instance):
        text=self.solution.text
        if text:
            if text[-1:] not in self.operators:       
                solution=str(eval(self.solution.text))
                self.solution.text=solution



if __name__=="__main__":
    app=CalculatorApp()
    app.run()
