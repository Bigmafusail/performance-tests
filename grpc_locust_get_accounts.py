from locust import task, User, between

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountResponse


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    Нагрузочный сценарий, который:
    1. Создаёт нового пользователя.
    2. Открытие депозитного счёта для этого пользователя
    3. Получение списка всех счетов, связанных с пользователем

    Использует базовый GatewayGRPCTaskSet и уже созданных в нём API клиентов.
    """

    # Shared state — сохраняем результаты запросов для дальнейшего использования
    create_user_response: CreateUserResponse | None = None
    open_deposit_account_response: OpenDepositAccountResponse | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что предыдущий шаг был успешным.
        """
        if not self.create_user_response:
            return  # Если пользователь не был создан, нет смысла продолжать

        self.accounts_gateway_client.open_deposit_account(user_id=self.create_user_response.user.id)

    @task(6)
    def get_accounts(self):
        """
        Запрашивает список всех счетов для текущего пользователя.
        """
        if not self.create_user_response:
            return  # Если пользователь не был создан, нет смысла продолжать

        self.accounts_gateway_client.get_accounts(user_id=self.create_user_response.user.id)


class GetAccountsScenarioUser(User):
    """
    Пользователь Locust, исполняющий сценарий получение списка всех счетов, связанных с пользователем.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)  # Имитируем паузы между выполнением сценариев
