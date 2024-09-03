from aiogram.fsm.state import (
    StatesGroup,
    State
)


class AnalyzeParamsState(StatesGroup):
    scores = State()
