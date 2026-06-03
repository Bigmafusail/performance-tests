from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict

from clients.http.gateway.documents.schema import DocumentSchema
from tools.fakers import fake


class OperationType(StrEnum):
    """Типы операций."""
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    """Статусы операций."""
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики по операции.
    """
    spent_amount: float=Field(alias="spentAmount")
    received_amount: float= Field(alias="receivedAmount")
    cashback_amount: float= Field(alias="cashbackAmount")


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операции по operation_id.
    """
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека по операции по operation_id
    """
    receipt: DocumentSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций для определенного счета
    """
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение статистики по операциям для определенного счета
    """
    summary: OperationsSummarySchema


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float= Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    pass


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции комиссии
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции пополнения.
    """
    pass


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции пополнения.
    """
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции кэшбэка.
    """
    pass


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции перевода.
    """
    pass


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str =Field(default_factory=fake.category)


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    pass


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции оплаты по счету.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции снятия наличных.
    """
    pass


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции снятия наличных.
    """
    operation: OperationSchema
