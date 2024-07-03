from dataclasses import dataclass
import pickle
import logging



logger = logging.getLogger(__name__)
@dataclass(slots=True)
class Player:
    id_player: int
    name_player: str
    games_figure: str | None = None
    n_games: int = 0
    n_wins: int = 0
    n_lose: int = 0

def read_pickle_db() -> dict:
    try:
        with open('db.pickle', 'rb') as file:
            PLAYERS = pickle.load(file)
            return PLAYERS
    except FileNotFoundError as e:
        logger.error(f'Возникла ошибка {e} при открытии файла db.pickle')

        # бесконечно пытаемся загрузить файл!!!
        read_pickle_db()


def write_pickle_db(players: dict):
    try:
        with open('db.pickle', 'wb') as file:
            pickle.dump(players, file)
            logger.info('Запись в db.pickle прошла успешно')
    except FileNotFoundError as e:
        logger.error(f'Возникла ошибка {e} при записи в файл db.pickle')
        # бесконечно пытаемся записать файл!!!
        write_pickle_db(players)


PLAYERS: dict[int, Player] = read_pickle_db()
#PLAYERS: dict[int, Player] = {}

[print(player) for player in PLAYERS.values()]
