from random import shuffle

#classes
class Card():

    suits=("spades", "hearts","diamonds", "clubs")
    
    values=(None,None,"2","3","4","5","6","7","8","9",
            "10","Jack","Queen","King","Ace")

    def __init__(self, v,s):
        """Suit + Value are ints"""
        self.value=v
        self.suit=s

    def __lt__(self,c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v=self.values[self.value]+ " of "+ self.suits[self.suit]
        return v

class Deck():
    
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards)==0:
            return None
        return self.cards.pop()

class Player(): 
    
    def __init__(self,name):
        self.win=0
        self.card=None
        self.name=name

class Game():
    def __init__(self):
        name1=input("Player 1 name: ")
        name2=input("Player 2 name: ")
        self.deck=Deck()
        self.player1=Player(name1)
        self.player2=Player(name2)
    
    def wins(self,winner):
        w=f"{winner} wins this round"
        print(w) 

    def draw(self, p1_name, p1_card, p2_name, p2_card):
        d=f"{p1_name} drew {p1_card} and {p2_name} drew {p2_card}"
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("Let the War Begin!")
        while len(cards)>=2:
            play=input("q to quit. Any key to play: ")
            if play=="q":
                break
            p1_card=self.deck.rm_card()
            p2_card=self.deck.rm_card()
            p1_name=self.player1.name
            p2_name=self.player2.name
            self.draw(p1_name,p1_card,p2_name,p2_card)
            if p1_card>p2_card:
                self.player1.win+=1
                self.wins(self.player1.name)
            else:
                self.player2.win+=1
                self.wins(self.player2.name)
    
        win=self.winner(self.player1, self.player2)
        print("War is over. {} wins". format(win))

    def winner(self,player1,player2):
        if player1.win>player2.win:
            return player1.name
        if player1.win<player2.win:
            return player2.name
        return "It was a tie"