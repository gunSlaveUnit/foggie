from PySide6.QtCore import QObject, Slot

from desktop.src.services.CartService import CartService


class CartLogic(QObject):
    def __init__(self, cart_service: CartService):
        super().__init__()

        self._cart_service = cart_service

    @Slot(int)
    def add(self, game_id: int):
        self._cart_service.add(game_id)

    @Slot(int)
    def delete(self, record_id: int):
        self._cart_service.delete(record_id)

    @Slot()
    def pay(self):
        self._cart_service.pay()
