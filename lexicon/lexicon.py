from dataclasses import dataclass

@dataclass
class LEXICON_RU:
    start: str = 'Начнем играть в игру "Камень, ножницы, бумага"?'
    help: str = ('Это бот с игрой "Камень, ножницы, бумага"\nбумага побеждает камень,\n камень побеждает ножницы,\n '
                 'а ножницы побеждают бумагу')
    stupid: str = 'Я пока глуп и умею играть только в игру 😁'
    game_win: str = 'У меня {comp_figure}\n{first_name} вы выиграли!\nсчет {wins}:{lose}'