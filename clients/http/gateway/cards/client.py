from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для создания виртуальной карты.
    """

    userId: str
    accountId: str

class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для создания физической карты.
    """

    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Создание виртуальной карты.

        :param request: Словарь с данными для создания виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)


    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
         Создание физической карты.

         :param request: Словарь с данными для создания физической карты.
         :return: Ответ от сервера (объект httpx.Response).
         """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
