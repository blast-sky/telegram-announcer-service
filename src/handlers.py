#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aiohttp
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from constants import CREATE_URL, GET_URL, REMOVE_URL

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я отвечаю за рассылку вакансий с сайта hh.\n"
                     "Ты можешь подписаться для получения новых вакансий с помощью команды:\n "
                     "/subscribe [список фильтров через пробел]")


@router.message(Command("subscribe"))
async def subscribe_handler(msg: Message):
    filters = msg.text.split()[1:]

    if len(filters) < 1:
        return await msg.answer("Для подписки нужно указать хотя бы один фильтр")

    create_subscription_json = {
        "userId": msg.from_user.id,
        "subscriptionType": "telegram",
        "filters": filters
    }

    async with aiohttp.ClientSession() as session:
        response = await session.post(CREATE_URL, json=create_subscription_json, verify_ssl=False)
        if response:
            return await msg.answer("Подписка успешно оформлена. Чтобы посмотреть активные подписки: /subscriptions")
        else:
            return await msg.answer(f"Ошибка при создании подписки: ${response.content}")


@router.message(Command("subscriptions"))
async def subscriptions_handler(msg: Message):
    async with aiohttp.ClientSession() as session:
        response = await session.get(GET_URL.format(user_id=msg.from_user.id), verify_ssl=False)
        if response:
            json = await response.json()
            subscriptions_text = str()
            for subscription in json:
                subscriptions_text += f"\n- {subscription['subscriptionType']}: {' '.join(subscription['filters'])}"
            return await msg.answer(f"Ваши активные подписки:{subscriptions_text}")
        else:
            return await msg.answer("Ошибка при обращении к сервису.")


@router.message(Command("remove"))
async def subscriptions_handler(msg: Message):
    async with aiohttp.ClientSession() as session:
        response = await session.get(REMOVE_URL.format(user_id=msg.from_user.id), verify_ssl=False)
        if response:
            return await msg.answer(f"Подписки успешно удалены.")
        else:
            return await msg.answer("Ошибка при обращении к сервису.")
