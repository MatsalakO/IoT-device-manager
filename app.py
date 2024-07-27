from aiohttp import web
from playhouse.shortcuts import model_to_dict
from models import db, Device, ApiUser, Location

routes = web.RouteTableDef()


@routes.post('/users')
async def create_device(request):
    data = await request.json()
    device = ApiUser.create(**data)
    return web.json_response(model_to_dict(device))


@routes.post('/locations')
async def create_device(request):
    data = await request.json()
    device = Location.create(**data)
    return web.json_response(model_to_dict(device))


@routes.post('/devices')
async def create_device(request):
    data = await request.json()
    device = Device.create(**data)
    return web.json_response(model_to_dict(device))


@routes.get('/devices')
async def get_devices(request):
    devices = [model_to_dict(device) for device in Device.select()]
    return web.json_response(devices)


@routes.get('/devices/{id}')
async def get_device(request):
    device_id = int(request.match_info['id'])
    device = Device.get_or_none(Device.id == device_id)
    if device:
        return web.json_response(model_to_dict(device))
    else:
        return web.HTTPNotFound()


@routes.put('/devices/{id}')
async def update_device(request):
    device_id = int(request.match_info['id'])
    data = await request.json()
    query = Device.update(**data).where(Device.id == device_id)
    query.execute()
    device = Device.get_by_id(device_id)
    return web.json_response(model_to_dict(device))


@routes.delete('/devices/{id}')
async def delete_device(request):
    device_id = int(request.match_info['id'])
    query = Device.delete().where(Device.id == device_id)
    query.execute()
    return web.HTTPNoContent()


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8080)
