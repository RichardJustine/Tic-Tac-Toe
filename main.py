import os
from random import randrange

player_turn = False
turn_counter = 0
game_ended = False


def initialize_winning_combinations():
  return [
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "123",
      "computer_value": "123"
    },
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "456",
      "computer_value": "456"
    },
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "789",
      "computer_value": "789"
    },
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "147",
      "computer_value": "147"
    },
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "258",
      "computer_value": "258"
    },
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "369",
      "computer_value": "369"
    },
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "159",
      "computer_value": "159"
    },
    {
      "player_match": 0,
      "computer_match": 0,
      "player_value": "357",
      "computer_value": "357"
    },
  ]


class RockPaperScissors:
  options = [{
    "id": 1,
    "choice": "Rock"
  }, {
    "id": 2,
    "choice": "Paper"
  }, {
    "id": 3,
    "choice": "Scissors"
  }]

  def get_choices(self):
    print("Enter a choice")
    for o_item in self.options:
      print(f"[{o_item['id']}] {o_item['choice']}")
    player_choice = input("Which one: ")
    while not player_choice.isdigit() or int(player_choice) > 3 or int(
        player_choice) < 1:
      player_choice = input("No option selected. Choose again: ")
    player_choice = int(player_choice)
    computer_choice = randrange(1, 3)
    choices = {
      "player": self.options[player_choice - 1]["choice"],
      "computer": self.options[computer_choice - 1]['choice']
    }
    return self.check_win(choices["player"].lower(),
                          choices["computer"].lower())

  def check_win(self, player, computer):
    print(f"You chose {player.title()}, computer chose {computer.title()}")
    if player == computer:
      print("It's a tie! Let's play again\n")
      self.get_choices()
    elif player == "rock":
      if computer == "scissors":
        print("Rock smaches scissors! You win!")
        return True
      else:
        print("Paper covers rock! You lose.")
        return False
    elif player == "paper":
      if computer == "rock":
        print("Paper covers rock! You win!")
        return True
      else:
        print("Scissors cuts paper! You lose.")
        return False
    elif player == "scissors":
      if computer == "paper":
        print("Scissors cuts paper! You win!")
        return True
      else:
        print("Rock smashes scissord! You lose.")
        return False


class TicTacToe:
  rcp = RockPaperScissors()

  def __init__(self, player_turn, turn_counter, game_ended):
    self.player_turn = player_turn
    self.chosen_positions = [{"type": "", "choice": 0}] * 9
    self.chosen_positions_values = []
    self.player_positions = []
    self.computer_positions = []
    self.turn_counter = turn_counter
    self.game_ended = game_ended
    self.winning_combinations = initialize_winning_combinations()

  def start(self):
    print("*" * 30)
    print("Let's play Tic-Tac-Toe!")
    print("*" * 30)
    print()
    self.player_turn = self.rcp.get_choices()

    print()
    if self.player_turn:
      input("Press any key to start.")
      print("|___||___||___|\n|___||___||___|\n|___||___||___|")
    else:
      print("Computer plays first.")
    self.print_board()

  def print_board(self, placeholder="_"):
    if self.player_turn:
      player_choice = input("\nChoose position from 1 to 9: ")
      while not player_choice.isdigit() or int(player_choice) > 9 or int(
          player_choice) < 1 or int(
            player_choice) in self.chosen_positions_values:
        player_choice = input(
          "\nInvalid position. Choose another position from 1 to 9: ")
      player_choice = int(player_choice)
      self.chosen_positions_values.append(player_choice)
      self.player_positions.append(player_choice)
      self.chosen_positions[player_choice - 1] = {
        "type": "player",
        "choice": player_choice
      }
      self.update_table()
      self.check_winner(self.player_positions, "player")
      self.turn_counter += 1
      self.player_turn = False
    else:
      computer_choice = self.get_computer_choice()
      while computer_choice in self.chosen_positions_values:
        computer_choice = self.get_computer_choice()
      print(f"\nComputer choose {computer_choice}")
      self.chosen_positions_values.append(computer_choice)
      self.computer_positions.append(computer_choice)
      self.chosen_positions[computer_choice - 1] = {
        "type": "computer",
        "choice": computer_choice
      }
      self.update_table()
      self.check_winner(self.computer_positions, "computer")
      self.turn_counter += 1
      self.player_turn = True

    while self.turn_counter < 10 and self.game_ended == False:
      self.print_board(self.chosen_positions)

  def update_table(self):
    table = ""
    for cp_index, cp_item in enumerate(self.chosen_positions):
      table += "\n" if cp_index % 3 == 0 else ""
      if cp_item["choice"] == cp_index + 1:
        if cp_item["type"].lower() == "player":
          table += "|_X_|"
        else:
          table += "|_O_|"
      else:
        table += "|___|"

    print(table)

  def get_computer_choice(self):
    return randrange(1, 9)

  def check_winner(self, positions, type):
    for p_item in positions:
      for wc_index, wc_item in enumerate(self.winning_combinations):
        if wc_item[type + "_value"].find(str(p_item)) >= 0:
          old_value = self.winning_combinations[wc_index][type + "_value"]
          new_value = old_value.replace(str(p_item), "")
          self.winning_combinations[wc_index].update(
            {type + "_value": new_value})
          self.winning_combinations[wc_index].update({
            type + "_match":
            self.winning_combinations[wc_index][type + "_match"] + 1
          })

    for wc_item in self.winning_combinations:
      if wc_item[type + "_match"] == 3:
        self.game_ended = True
        if self.player_turn:
          print("Congrats! You win.")
        elif self.player_turn == False:
          print("Computer win! You lose.")
        else:
          print("Tie! No winner.")
        self.ask_player()

  def ask_player(self):
    print()
    print("*" * 30)
    print("Do you want to play again? ")
    print("[1] Yes")
    print("[2] No")
    player_choice = input("Which one? ")
    print("*" * 30)
    while not player_choice.isdigit() or int(player_choice) > 2 or int(
        player_choice) < 1:
      player_choice = input("\nNo option selected. Choose again: ")
    player_choice = int(player_choice)
    if player_choice == 1:
      clear = lambda: os.system("clear")
      clear()
      self.winning_combinations = initialize_winning_combinations()
      new_game = TicTacToe(player_turn, turn_counter, game_ended)
      new_game.start()
    else:
      print("Goodbye! Thanks for playing.")


game = TicTacToe(player_turn, turn_counter, game_ended)
game.start()
