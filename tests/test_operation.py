from httpx import AsyncClient


async def test_add_specific_operation(ac: AsyncClient):
    response = await ac.post("/operations", json={
        "id": 1,
        "quantity": "test_quantity",
        "figi": "testFigi",
        "instrument_type": "test_instrument_type",
        "date": "2023-02-01T00:00:00",
        "type": "testType",
    })

    assert response.status_code == 200
