from aiogram.fsm.state import (
    StatesGroup,
    State
)


class ParsingParamsState(StatesGroup):
    hours = State()
