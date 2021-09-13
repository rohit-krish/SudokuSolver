from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from colorama import Back, Fore, Style
from kivy.lang import Builder
from solver import *

Builder.load_file('design.kv')


class MyLayout(GridLayout):
    text = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.textinputs = {}
        count = 0
        for i in range(9):
            for j in range(9):
                self.textinputs["key%s" % count] = TextInput(
                    size_hint=(.11, .11), on_text_validate=self.on_enter,
                    multiline=False, background_color=(99/255, 156/255, 194/255, 1), cursor_color=(0, 0, 0, 0),
                    input_filter=lambda text, from_undo: text if (
                        text.isdigit() and len(self.text) == 0 and 0 < int(text) < 10) else "",
                    font_size='30dp', halign='center')

                if 0 <= i and i <= 2 and 0 <= j and j <= 2:
                    self.textinputs['key%s' % count].background_color = (
                        160/255, 197/255, 222/255, 1)  # light
                if 6 <= i and i <= 8 and 6 <= j and j <= 8:
                    self.textinputs['key%s' % count].background_color = (
                        160/255, 197/255, 222/255, 1)  # light
                if 6 <= i and i <= 8 and 0 <= j and j <= 2:
                    self.textinputs['key%s' % count].background_color = (
                        160/255, 197/255, 222/255, 1)  # light
                if 0 <= i and i <= 2 and 6 <= j and j <= 8:
                    self.textinputs['key%s' % count].background_color = (
                        160/255, 197/255, 222/255, 1)  # light
                if 3 <= i and i <= 5 and 3 <= j and j <= 5:
                    self.textinputs['key%s' % count].background_color = (
                        160/255, 197/255, 222/255, 1)  # light

                self.textinputs["key%s" % count].bind(focus=self.focus)
                self.ids.layout_id.add_widget(self.textinputs["key%s" % count])
                count += 1

    def find_board(self):

        count = 0
        board = []
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(self.textinputs["key%s" % count].text)
                count += 1
            board.append(temp)

        # putting zero whereever there is no text
        for i in range(9):
            for j in range(9):
                if board[i][j] == '':
                    board[i][j] = 0

        # before giving it convert the str to int
        for i in range(9):
            for j in range(9):
                board[i][j] = int(board[i][j])
        return board

    def find_pos(self, text):
        # print(pos)
        # print(self.width/10 - (self.width/.11))
        count = 0
        textinputs_pos = {}
        for i in range(9):
            for j in range(9):
                textinputs_pos['i{}j{}'.format(
                    i, j)] = self.textinputs['key%s' % count]
                count += 1
        for i in range(9):
            for j in range(9):
                if text == textinputs_pos['i{}j{}'.format(i, j)].text:
                    return (i, j)

    def on_enter(self, instance):
        # print('value is ', args[0].text)
        instance.focus = False
        instance.text = instance.text[0]
        # print('focus=False')

    def focus(self, instance, state):
        self.instance = instance
        if state:
            # print('focus',args)
            if len(instance.text) != 0:
                instance.text = instance.text[0]
        else:
            # now every time if the focus of each input turned to false we can get it's value
            text = instance.text
            if text.isnumeric() or len(text) == 0:
                # print('it is numbers')
                # instance.background_color = (1, 1, 1, 1)
                if len(instance.text) != 0:
                    instance.text = instance.text[0]

            # getting the position for to check if it is valid
            if instance.text != '':
                cur_pos = self.find_pos(instance.text)
                board = self.find_board()

                if not valid(board, int(instance.text), cur_pos):
                    instance.text = ''

    def clearButton(self):
        count = 0
        for i in range(9):
            for j in range(9):
                self.textinputs["key%s" % count].text = ''
                # self.textinputs["key%s"%count].background_color=(1,1,1,1)
                count += 1

    def solveIt(self):
        # here i'm pasting the thing in the on_focus() when it is not focused

        # now every time if the focus of each input turned to false we can get it's value
        text = self.instance.text
        if text.isnumeric() or len(text) == 0:
            # print('it is numbers')
            # self.instance.background_color = (1, 1, 1, 1)
            if len(self.instance.text) != 0:
                self.instance.text = self.instance.text[0]

        # getting the position for to check if it is valid
        if self.instance.text != '':
            cur_pos = self.find_pos(self.instance.text)
            board = self.find_board()

            if not valid(board, int(self.instance.text), cur_pos):
                self.instance.text = ''

        board = self.find_board()
        print(Fore.GREEN+'\nPROCESSING...')
        solve(board)
        risk=print_board(board)
        print(Fore.RED+'\n'+'-> TOTAL COUNT: '+str(risk)+'\n')
        print(Fore.BLUE+'---------------------')

        count = 0
        for i in range(9):
            for j in range(9):
                self.textinputs['key%s' % count].text = str(board[i][j])
                count += 1


class Sudoku(MDApp):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


Sudoku().run()
