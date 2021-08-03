from fastapi import APIRouter


class ConfigurationEnvironment:
    @staticmethod
    def get_endpoints():
        base = APIRouter()

        @base.post("/")
        async def configuration_environment_root():
            return "Loading environment..."
        return base

