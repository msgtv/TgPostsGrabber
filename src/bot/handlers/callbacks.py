from aiogram import F, Router
from aiogram.types import (
    CallbackQuery,
)
from aiogram.fsm.context import FSMContext

from src.bot.keyboard import (
    get_post_manage_kb
)


router = Router()


@router.callback_query(F.data.startswith('CardAdd_'))
async def add_card_number(callback: CallbackQuery, state: FSMContext):
    card_number = int(callback.data.split('_')[1])

    state_data = await state.get_data()

    scores = state_data.get('scores', {1: 0, 2: 0, 3: 0})

    scores[card_number] += 1

    await state.update_data(scores=scores)

    kb = await get_post_manage_kb(card_number)

    await callback.message.edit_reply_markup(reply_markup=kb)


@router.callback_query(F.data.startswith('CardReject_'))
async def callback_reject_card_number(callback: CallbackQuery, state: FSMContext):
    card_number = int(callback.data.split('_')[1])

    await reject_card_number(state, card_number)

    kb = await get_post_manage_kb()

    await callback.message.edit_reply_markup(reply_markup=kb)


async def reject_card_number(state: FSMContext, card_number: int):
    state_data = await state.get_data()

    scores = state_data.get('scores', None)
    if scores is None:
        scores = {1: 0, 2: 0, 3: 0}
    else:
        card_scores = scores[card_number]
        if card_scores > 0:
            card_scores = card_scores - 1
            scores[card_number] = card_scores

    await state.update_data(scores=scores)


@router.callback_query(F.data.startswith('Delete'))
async def delete_post(callback: CallbackQuery, state: FSMContext):
    if '_' in callback.data:
        card_number = int(callback.data.split('_')[1])
        await reject_card_number(state, card_number)

    await callback.message.delete()
