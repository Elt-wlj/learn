import asyncio


async def wget(host):
    print('wget…… ' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET /HTTP/1.0\r\nhost:%s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await  writer.drain()
    while True:
        line = await  reader.readline()
        if line == r'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com', 'www.baidu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
