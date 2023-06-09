from PySide6.QtCore import QObject, Signal, Slot, Property

from common.api.v1.schemas.payments import PaymentCreateSchema
from desktop.src.services.WalletService import WalletService


class WalletLogic(QObject):
    def __init__(self, wallet_service: WalletService):
        super().__init__()

        self._wallet_service = wallet_service

        self._balance = 0.00
        self._amount = 0.00

    balance_changed = Signal()

    @Property(float, notify=balance_changed)
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_value: float):
        if self._balance != new_value:
            self._balance = new_value
            self.balance_changed.emit()

    amount_changed = Signal()

    @Property(float, notify=amount_changed)
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_value: float):
        if self._amount != new_value:
            self._amount = new_value
            self.amount_changed.emit()

    @Slot()
    def map(self):
        self._wallet_service.load()

        self.balance = self._wallet_service.balance

    @Slot()
    def top_up(self):
        payment = PaymentCreateSchema(
            card_number="string",
            validity_month=0,
            validity_year=0,
            cvv_cvc=0,
            amount=self.amount
        )

        response = self._wallet_service.top_up(payment)

        if response.ok:
            self.balance = self._wallet_service.balance

        self.amount = 0
